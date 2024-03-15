
import modules.postProducto as postPro
import modules.getGamaProducto as gam
import requests
from tabulate import tabulate
import json

def getAllData():
    peticion = requests.get("http://172.16.100.126:5501")
    #json-server storage/producto.json -b 5501 
    data = peticion.json()
   
    return data

def getProductoCodigo (codigo):
    for val in getAllData():
        if (val.get('codigo_producto') == codigo):
            return [val]

#ejercicio 15
def getAllStockPriceGama (gama, stock):
    condiciones =[]
    for val in getAllData():
        if (val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
            
            # condiciones.append({
            #     "gama" : val.get("gama"),
            #     "precio de venta" : val.get("precio_venta") 
            # })
            
            #     "gama" : val.get("gama"),
            #     "cantidad_en_stock" : val.get("canditad_en_stock") 
            
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones) : 
        condiciones[i] = {
            "codigo": val.get("codigo_producto"),
            "venta": val.get("precio_venta"),
            "nombre": val.get("nombre"),
            "gama": val.get("gama"),
            "dimensiones" : val.get("dimensiones"),
            "proveedor": val.get("proveedor"), 
            "descripcion": f'(val.get("descripcion")[15])...' if condiciones[1].get("descripcion") else None,
            "stock": val.get("cantidad_en_stock"),
            "base" : val.get("precio_proveedor")
        }
        # if val.get("precio_venta") != None:
        #     condiciones.sort(key=price)
            
        # return val.get("precio_venta")
    return condiciones

def menu():
    while True: 
        print(f"""

  ___                   _                             _         _          
 | _ \___ _ __  ___ _ _| |_ ___ ___  _ __ _ _ ___  __| |_  _ __| |_ ___ ___
 |   / -_) '_ \/ _ \ '_|  _/ -_|_-< | '_ \ '_/ _ \/ _` | || / _|  _/ _ (_-<
 |_|_\___| .__/\___/_|  \__\___/__/ | .__/_| \___/\__,_|\_,_\__|\__\___/__/
         |_|                        |_|                                    

            1. Obtener todos los productos de una categoría ordenando sus precios de venta, también que su cantidad de inventario sea superior
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            gama = input("Ingrese la gama que deseas filtrar : ")
            stock = int(input("Ingrese las unidades que deseas mostrar : "))
            print(tabulate(getAllStockPriceGama (gama, stock), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif(opcion == 0):
            break
