import json
import re
import requests
from tabulate import tabulate
import os
import modules.getGamaProducto as gG
import modules.getProducto as gP


def postProducto():
    producto = {}
    while True:
        try:
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto: ")
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    data = gP.getProductoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo que ingreso ya existe ")
                    else: producto['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if (not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', nombre)is not None):
                    producto["nombre"] = nombre
                    break
                else:
                        raise Exception("El nombre no comple con el estandar establecido")

        except Exception as error: 
            print(error)
    print(producto)





    #producto = {
    #    "codigo_producto": input("Ingrese el codigo del producto: "),
    #    "nombre": input("Ingrese el nombre del producto: "),
    #    "gama": gP.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gP.getAllNombre())])))],
    #    "dimensiones": input("Ingrse la dimensiones del producto: "),
    #    "proveedor": input("Ingrse el proveedor del producto: "),
    #    "descripcion": input("Ingrse el descripcion del producto: "),
    #    "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
    #    "precio_venta": int(input("Ingrse el precio de ventas: ")),
    #    "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    #}
    #headers = {'Content-type' : 'aplication/json', 'charset' : 'UTF-8'}
    #peticion = requests.post("http://172.16.100.126:5501",headers=headers, data=json.dumps(producto))
    #res = peticion.json()
    #res["Mensaje"] = "Producto guardado"
    #return res


def menu():
    while True: 
        os.system
        print(f"""

  ___                   _                             _         _          
 | _ \___ _ __  ___ _ _| |_ ___ ___  _ __ _ _ ___  __| |_  _ __| |_ ___ ___
 |   / -_) '_ \/ _ \ '_|  _/ -_|_-< | '_ \ '_/ _ \/ _` | || / _|  _/ _ (_-<
 |_|_\___| .__/\___/_|  \__\___/__/ | .__/_| \___/\__,_|\_,_\__|\__\___/__/
         |_|                        |_|                                    

            1. Obtener todos los porductos de una categoria ordenando sus precios de venta
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postProducto(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion == 0):
            break