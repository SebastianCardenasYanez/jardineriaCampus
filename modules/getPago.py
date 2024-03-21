from tabulate import tabulate
import requests
import json
import os
import modules.postPago as postPago

def getAllDataPagos():
    peticion = requests.get("http://154.38.171.54:5006/pagos") #falta arreglar las url el visual no deja crearlos
    #json-server storage/producto.json -b 5504
    data = peticion.json()
    return data

def getAllidPagos(codigo):
    peticion = requests.get(f"http://172.16.102.108:5501/productos/{codigo}")
    #json-server storage/producto.json -b 5501 
    return [peticion.json()] if peticion.ok else []



#ejercicio 8
def getAllCodigoClienteAñoPago() :
    codigoPago = set()
    for val in getAllDataPagos():
        año = val.get("fecha_pago")
        if año.startswith("2008"):
            codigoPago.add(val.get('fecha_pago'))
            codigoPago.add(val.get('codigo_cliente'))
    return codigoPago
        
#ejercicio 13
def getAllFormaDePago2008() :
    formaPago = []
    #sorted ()reverse = true
    for val in getAllDataPagos():
        año = val.get("fecha_pago")
        forma = val.get("forma_pago")
        if año.startswith("2008") and forma == "PayPal":
            formaPago.append(val)
    return formaPago
        
#ejercicio 14
def getAllFormaPago() :
    formasDePago = set()
    for val in getAllDataPagos():
        formasDePago.add(val.get("forma_pago"))
        
    return [formasDePago]

def menu():
    while True: 
        os.system("clear")
        print(f"""


   

  ___                   _               _                           
 | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   _ __  __ _ __ _ ___ 
 |   / -_) '_ \/ _ \ '_|  _/ -_|_-< / _` / -_) | '_ \/ _` / _` / _ |
 |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| | .__/\__,_\__, \___/
         |_|                                   |_|        |___/     

            1. Obtener los codigos de los clientes que realizaron pagos en el 2008
            2. Obtener todas las formas de pago en el 2008
            3. Obtener todas las formas de pago
            4. Administrar pagos
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllCodigoClienteAñoPago(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion==2):
            print(tabulate(getAllFormaDePago2008(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
        elif (opcion==3):
            print(tabulate(getAllFormaPago(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
        elif (opcion == 4):
            postPago.menu()
        elif (opcion == 0):
            break