import json
import re
import requests
from tabulate import tabulate
import os
import modules.getPago as gP

def postPago():
    Pago = {}
    while True:
        try:
            if(not Pago.get("codigo_cliente")):
                codigo = int(input("Ingrese el codigo del cliente que realizo el pago: "))
                if codigo is not None:
                   Pago['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if (not Pago.get("forma_pago")):
                forma = gP.getAllFormaPago()[int(input("Selecione el estado:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gP.getAllFormaPago())])))]
                Pago['forma_pago'] = forma

            if (not Pago.get("id_transaccion")):
                id = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', id)is not None):
                        Pago["id_transaccion"] = id
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")
                
            if (not Pago.get("fecha_pago")):
                fecha = input("Ingrese la fecha en la que se realizo el pago: ")
                if (re.match(r'^\d{4}-\d{2}-\d{2}$', fecha)is not None):
                        Pago["id_transaccion"] = id
                        break
                else:
                    raise Exception("La fecha no comple con el estandar establecido")
                
            if(not Pago.get("total")):
                total = int(input("Ingrese el total del pago: "))
                if total is not None:
                   Pago['codigo_producto'] = total
                else : 
                    raise Exception("El total no comple con el estandar establecido ")

        except Exception as error: 
            print(error)
    print(Pago)


    headers = {'Content-type' : 'aplication/json', 'charset' : 'UTF-8'}
    peticion = requests.post("http://172.16.100.126:5501",headers=headers, data=json.dumps(Pago))
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res

def updatePagos(id):
    data = gP.getAllidPagos(id)
    if data is None:
            print(f"""

Id del pago no encontrado. """)
    
    while True:
        try:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
            print(f"""
Datos para modificar: """)
            for i, (val, asd) in enumerate(data[0].items()):
                print(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if data[0][datoModificar] == data[0]["total"] or data[0][datoModificar] == data[0]["codigo_cliente"]:
                    data[0][datoModificar] = int(nuevoValor)
                    break
                else:
                    data[0][datoModificar] = nuevoValor
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            print(error)
    
    peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pago Modificado"
    return [res]


def deletePago(id):
    data = gP.getAllidPagos(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos{id}")
        if peticion.status_code == 200:
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code
            }
        else:
            return {
                "body": [{"message": "Error al eliminar el producto"}],
                "status": peticion.status_code
            }
    else:
        return {
            "body": [{"message": "Producto no encontrado", "id": id}],
            "status": 404 }
    
    # peticion = requests.delete("http://172.16.104.23:5503/pedidos/{id}")
#falta la url bien hecha ..
    # res = peticion.json()
    # res["Mensaje"] = "Producto eliminado"
    # return res

def menu():
    while True: 
        os.system("clear")
        print(f"""


   
    _      _       _      _    _               _               _                              
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   _ __  __ _ __ _ ___ ___
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) | '_ \/ _` / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| | .__/\__,_\__, \___/__/
                                                                      |_|        |___/        

            1. Agregar un nuevo pago
            2. Eliminar un pago
            3. Actualizar un pago
            0. Salir
              
              """)

        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=3):
                if (opcion == 1):
                    print(tabulate(postPago(), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                    break
                elif (opcion==2):
                    id = input("Ingrese el id del pago que desea eliminar")
                    print(tabulate(deletePago(id), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                elif (opcion ==3):
                    idPedido = input("Ingrese el id del Pedido: ")
                    print(tabulate(updatePagos(idPedido), headers="keys", tablefmt='rounded_grid'))
                    input(f"""
        Escriba una tecla para continuar: """)
                elif (opcion == 0):
                    break