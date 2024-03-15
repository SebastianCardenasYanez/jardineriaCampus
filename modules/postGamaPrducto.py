import json
import re
import requests
from tabulate import tabulate
import os

def postGamaProducto():
    oficina = {}
    while True:
        try:
            if(not oficina.get("codigo_oficina")):
                codigo = input("Ingrese el codigo de la oficina: ")
                if (re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigo)is not None):
                    oficina['codigo_Oficina'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if (not oficina.get("ciudad")):
                ciudad = input("Ingrese la ciudad de la ofcina: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', ciudad)is not None):
                    oficina["nombre"] = ciudad
                    break
                else:
                        raise Exception("El nombre no comple con el estandar establecido")
        except Exception as error: 
            print(error)
        print(oficina)


    peticion = requests.post("http://172.16.100.126:5501", data=json.dumps(oficina))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res


def menu():
    while True: 
        os.system
        print(f"""


    _      _       _      _    _               _               _            __ _    _           
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   ___ / _(_)__(_)_ _  __ _ 
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) / _ \  _| / _| | ' \/ _` |
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| \___/_| |_\__|_|_||_\__,_|
                                                                                                

            1. Agregar una nueva gama de un producto
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postGamaProducto(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion == 0):
            break