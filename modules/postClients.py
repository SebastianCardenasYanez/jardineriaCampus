import json
import re
import requests
from tabulate import tabulate
import os
import modules.getClients as cli

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
                nombreCli = input("Ingrese el nombre del empleado: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', nombreCli)is not None):
                    clientes["nombre_cliente"] = nombreCli
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not clientes.get("nombre_contacto")):
                nombreCon = input("Ingrese el nombre del empleado: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', nombreCon)is not None):
                    clientes["nombre_contacto"] = nombreCon
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not clientes.get("apellido_contacto")):
                apellido = input("Ingrese el primer apellido del empleado: ")
                if (re.match(r'^[A-Z][a-z]*)+$', apellido)is not None):
                    clientes["apellido_contacto"] = apellido
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if(not clientes.get("telefono")):
                tel = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[0-9]{10}$', tel)is not None):
                        clientes["telefono"] = tel
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("fax")):
                tel = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[0-9]{10}$', tel)is not None):
                        clientes["telefono"] = tel
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("linea_direccion1")):
                direc1 = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[A-Z][a-z][0-9]*\s*)$', direc1)is not None):
                        clientes["telefono"] = direc1
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("linea_direccion2")):
                direc2 = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[A-Z][a-z][0-9]*\s*)$', direc2)is not None):
                        clientes["telefono"] = direc2
                        break
                elif direc2 == None :
                    clientes['fecha_esperada'] = direc2

                else:
                    raise Exception("El id no comple con el estandar establecido")

            if(not clientes.get("ciudad")):
                ciudad = input("Ingrese la ciudad de la ofcina: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', ciudad)is not None):
                    clientes["nombre"] = ciudad
                    break
                else:
                        raise Exception("La ciudad no comple con el estandar establecido")
                
            if(not clientes.get("region")):
                region = input("Ingrese la region de la ofcina: ")
                if (re.match(r'^[A-Z][a-z])+$', region)is not None):
                    clientes["region"] = region
                    break
                elif region == None :
                    clientes['fecha_esperada'] = region
                else:
                    raise Exception("La region no comple con el estandar establecido")
            
            if(not clientes.get("pais")):
                pais = input("Ingrese el pais de la ofcina: ")
                if (re.match(r'^[A-Z][a-z])+$', pais)is not None):
                    clientes["pais"] = pais
                    break
                else:
                    raise Exception("El pais no comple con el estandar establecido")
            
            if(not clientes.get("codigo_postal")):
                codpos = input("Ingrese el codigo postal de la clientes: ")
                if (re.match(r'^[A-Z]{3}-[A-Z]{2}$', codpos)is not None):
                    clientes['codigo_postal'] = codpos
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")

            if(not clientes.get("codigo_empleado_rep_ventas")):
                codigo = int(input("Ingrese el codigo del cliente que realizo el pago: "))
                if codigo is not None:
                   clientes['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if(not clientes.get("limite_credito")):
                codigo = int(input("Ingrese el codigo del cliente que realizo el pago: "))
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

def deleteClientes(id):
    data = cli.getCodigoCLientes(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente{id}")
    if(peticion.status_code == 204):
        data.append({"message" : "cliente eliminado correctamente"})
        return{
            "data" : data,
            "status" : peticion.status_code,
        }
    else : 
        return {
            "body" : [{
                "menssage" : "cliente no encontrado",
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
        os.system
        print(f"""
  
    _      _       _      _    _               _               _          _ _         _          
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   __| (_)___ _ _| |_ ___ ___
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) / _| | / -_) ' \  _/ -_|_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| \__|_|_\___|_||_\__\___/__/
                                                                                                 

            1. Agregar una nueva clientes
            2. Eliminar un cliente
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
        elif (opcion == 0):
            break