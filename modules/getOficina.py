from tabulate import tabulate
import requests
import json
import modules.postOficina as postOfi

def getAllDataOficina():
    peticion = requests.get("http://154.38.171.54:5005/oficinas") #falta arreglar las url el visual no deja crearlos
    #json-server storage/producto.json -b 5505
    data = peticion.json()
    return data

def getAllidOfi(codigo):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{codigo}")
    #json-server storage/producto.json -b 5501 
    return [peticion.json()] if peticion.ok else []

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllDataOficina():
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAllDataOficina():
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono

def menu():
    while True:
        print(""" 
     ___                   _               _            __ _    _           
    | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   ___ / _(_)__(_)_ _  __ _ 
    |   / -_| '_ \/ _ \ '_|  _/ -_|_-< / _` / -_| / _ \  _| / _| | ' \/ _` |
    |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| \___/_| |_\__|_|_||_\__,_|
            |_|                                                             

            1. obtener todos los codigos y ciudades
            2. obtener los telefonos de las oficinas de españa
            3. administracion de oficina
            0. Regresar al menu principal

    """)
        
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllCodigoCiudad(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 2):
            print(tabulate(getAllCiudadTelefono("España"), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 3):
            postOfi.menu()
        elif (opcion == 0):
            break
        input("presione una tecla para continuar")
        break
    