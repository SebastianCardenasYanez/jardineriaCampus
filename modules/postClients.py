import json
import re
import requests
from tabulate import tabulate
import os
import modules.getClients as gC

def postClients():
    clientes = {}
    while True:
        try:
            if(not clientes.get("codigo_clientes")):
                codigo = int(input("Ingrese el codigo del cliente que realizo el pago: "))
                if codigo is not None:
                   clientes['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if (not clientes.get("nombre_cliente")):
                nombreCli = input("Ingrese el nombre del cliente: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombreCli)is not None):
                    clientes["nombre_cliente"] = nombreCli
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not clientes.get("nombre_contacto")):
                nombreCon = input("Ingrese el nombre del contacto: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombreCon)is not None):
                    clientes["nombre_contacto"] = nombreCon
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not clientes.get("apellido_contacto")):
                apellido = input("Ingrese el primer apellido del empleado: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido)is not None):
                    clientes["apellido_contacto"] = apellido
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if(not clientes.get("telefono")):
                tel = input("Ingrese el numero de telefo: ")
                if (re.match(r'^[0-9]{10}$', tel)is not None):
                        clientes["telefono"] = tel
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("fax")):
                tel = input("Ingrese el fax: ")
                if (re.match(r'^[0-9]{10}$', tel)is not None):
                        clientes["telefono"] = tel
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("linea_direccion1")):
                direc1 = input("Ingrese la linea de direccion 1: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', direc1)is not None):
                        clientes["telefono"] = direc1
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("linea_direccion2")):
                direc2 = input("Ingrese la linea de direccion 2: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', direc2)is not None):
                        clientes["telefono"] = direc2
                        break
                elif direc2 == None :
                    clientes['fecha_esperada'] = direc2

                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("ciudad")):
                ciudad = input("Ingrese la ciudad del cliente: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ciudad)is not None):
                    clientes["nombre"] = ciudad
                    break
                else:
                        raise Exception("La ciudad no comple con el estandar establecido")
                
            if(not clientes.get("region")):
                region = input("Ingrese la region del cliente: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', region)is not None):
                    clientes["region"] = region
                    break
                elif region == None :
                    clientes['fecha_esperada'] = region
                else:
                    raise Exception("La region no comple con el estandar establecido")
            
            if(not clientes.get("pais")):
                pais = input("Ingrese el pais del cliente:  ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', pais)is not None):
                    clientes["pais"] = pais
                    break
                else:
                    raise Exception("El pais no comple con el estandar establecido")
            
            if(not clientes.get("codigo_postal")):
                codpos = input("Ingrese el codigo postal del cliente: ")
                if (re.match(r'^[A-Z]{3}-[A-Z]{2}$', codpos)is not None):
                    clientes['codigo_postal'] = codpos
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")

            if(not clientes.get("codigo_empleado_rep_ventas")):
                codigo = int(input("Ingrese el codigo del representante de ventas del cliente: "))
                if codigo is not None:
                   clientes['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if(not clientes.get("limite_credito")):
                codigo = int(input("Ingrese el limite de credito del cliente: "))
                if codigo is not None:
                   clientes['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
        except Exception as error: 
         print(error)
    print(clientes)


    peticion = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(clientes))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res

def updateCliente(id):
    data = data = gC.getCodigoCLientes(id)
    if data is None:
            print(f"""

Id del Cliente no encontrado. """)
    
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
                if datoModificar == "codigo_empleado_rep_ventas" or "codigo_cliente" or "limite_credito":
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
    
    peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Cliente Modificado"
    return [res]



def deleteClientes(id):
    data = gC.getCodigoCLientes(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente{id}")
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
        os.system
        print(f"""
  
    _      _       _      _    _               _               _          _ _         _          
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   __| (_)___ _ _| |_ ___ ___
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) / _| | / -_) ' \  _/ -_|_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| \__|_|_\___|_||_\__\___/__/
                                                                                                 

            1. Agregar una nueva clientes
            2. Eliminar un cliente
            3. Actulizar
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postClients(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion == 2):
            id = input("Ingrese la id del cliente que desea eliminar: ")
            print(tabulate(deleteClientes(id), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion == 3):
            idCli = input("Ingrese el id del empleado: ")
            print(tabulate(updateCliente(idCli), headers="keys", tablefmt='rounded_grid'))
            input(f"""
    Escriba una tecla para continuar: """)
        elif (opcion == 0):
            break