import json
import re
import requests
from tabulate import tabulate
import os
import modules.getOficina as gO


def postOficina():
    oficina = {}
    while True:
        try:
            if(not oficina.get("codigo_oficina")):
                codigo = input("Ingrese el codigo de la oficina: ")
                if (re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigo)is not None):
                    oficina['codigo_oficina'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
            if (not oficina.get("ciudad")):
                ciudad = input("Ingrese la ciudad de la ofcina: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', ciudad)is not None):
                    oficina["nombre"] = ciudad
                    break
                else:
                        raise Exception("La ciudad no comple con el estandar establecido")
            if (not oficina.get("pais")):
                pais = input("Ingrese el pais de la ofcina: ")
                if (re.match(r'^[A-Z][a-z])+$', pais)is not None):
                    oficina["pais"] = pais
                    break
                else:
                    raise Exception("El pais no comple con el estandar establecido")
            if (not oficina.get("region")):
                region = input("Ingrese la region de la ofcina: ")
                if (re.match(r'^[A-Z][a-z])+$', region)is not None):
                    oficina["region"] = region
                    break
                else:
                    raise Exception("La region no comple con el estandar establecido")

            if(not oficina.get("codigo_postal")):
                codpos = input("Ingrese el codigo postal de la oficina: ")
                if (re.match(r'^[A-Z]{3}-[A-Z]{2}$', codpos)is not None):
                    oficina['codigo_postal'] = codpos
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")

            if (not oficina.get("telefono")):
                tel = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[+0-9]{2}\s[0-9]{2}\s[0-9]{7}$', tel)is not None):
                        oficina["telefono"] = tel
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if (not oficina.get("linea_direccion1")):
                direc1 = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[A-Z][a-z][0-9]*\s*)$', direc1)is not None):
                        oficina["telefono"] = direc1
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            if (not oficina.get("linea_direccion2")):
                direc2 = input("Ingrese la id de la transaccion: ")
                if (re.match(r'^[A-Z][a-z][0-9]*\s*)$', direc2)is not None):
                        oficina["telefono"] = direc2
                        break
                else:
                    raise Exception("El id no comple con el estandar establecido")

            
        except Exception as error: 
            print(error)
        print(oficina)

    peticion = requests.post("http://154.38.171.54:5005/oficinas", data=json.dumps(oficina))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res

def deleteOficina(id):
    data = gO.getAllidOfi(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
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
        os.system
        print(f"""


    _      _       _      _    _               _               _            __ _    _           
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   ___ / _(_)__(_)_ _  __ _ 
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) / _ \  _| / _| | ' \/ _` |
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| \___/_| |_\__|_|_||_\__,_|
                                                                                                

            1. Agregar una nueva oficina
            2.Eliminar una oficina
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postOficina(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion ==2):
            id = int(input("Ingrese el codigo del pedido que desea eleminar"))
            print(tabulate(deleteOficina(id), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
        elif (opcion == 0):
            break