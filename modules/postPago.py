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
                if (re.match(r'^[a-z]{2}-[a-z]{3}-[0-9]{6}$', id)is not None):
                        Pago["id_transaccion"] = id
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")
                
            if (not Pago.get("fecha_pago")):
                fecha = input("Ingrese la fecha en la que se realizo el pago: ")
                if (re.match(r'^[0-9]{4}-[0-9]{2}-[0-1]{1}[0-9]{1}$', fecha)is not None):
                        Pago["id_transaccion"] = id
                        break
                else:
                    raise Exception("La fecha no comple con el estandar establecido")
                
            if(not Pago.get("total")):
                total = int(input("Ingrese el codigo del cliente que realizo el pago: "))
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


def deletePedido(id):
    data = gP.getAllidPagos(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos{id}")
        if(peticion.status_code == 204):
            data.append({"message" : "producto eliminado correctamente"})
            return{
                "data" : data,
                "status" : peticion.status_code,
            }
    else : 
        return {
            "body" : [{
                "menssage" : "producto no  encontrado",
                "id": id
            }],
            "status" : 400
        }
    
    # peticion = requests.delete("http://172.16.104.23:5503/pedidos/{id}")
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto eliminado"
    return res

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
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postPago(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion==2):
            id = input("Ingrese el id del pago que desea eliminar")
            print(tabulate(deletePedido(id), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
        elif (opcion == 0):
            break