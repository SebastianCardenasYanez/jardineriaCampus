import json
import re
import requests
from tabulate import tabulate
import os
import getGamaProducto as gGP

def postGamaProducto():
    gamaProducto = {}
    while True:
        try:
            if (not gamaProducto.get("gama")):
                gama = gGP.getGamas()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gGP.getGamas())])))]
                gamaProducto['gama'] = gama
                break

            if (not gamaProducto.get("descripcion_texto")):
                descript = input("Ingrese la descripcion de texto de la ofcina: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', descript)is not None):
                    gamaProducto["descripcion_texto"] = descript
                    break
                elif descript == None :
                    gamaProducto['fecha_esperada'] = descript
                else:
                    raise Exception("El nombre no comple con el estandar establecido")
            
            if(gamaProducto.get("descripcion_html")):
                descriph = input("Ingrese la descripcion de texto de la ofcina: ")
                if descriph == None:
                    gamaProducto['descripcion_html'] = descriph
            
            if(gamaProducto.get("imagen")):
                imagen = input("Ingrese la descripcion de texto de la ofcina: ")
                if imagen == None:
                    gamaProducto['imagen'] = imagen

            
        except Exception as error: 
            print(error)
        print(gamaProducto)


    peticion = requests.post("http://172.16.100.126:5501", data=json.dumps(gamaProducto))
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