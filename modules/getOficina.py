import storage.oficina as of
from tabulate import tabulate

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono

def menu():
    print(""" 
  ___                   _               _            __ _    _           
 | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   ___ / _(_)__(_)_ _  __ _ 
 |   / -_| '_ \/ _ \ '_|  _/ -_|_-< / _` / -_| / _ \  _| / _| | ' \/ _` |
 |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| \___/_| |_\__|_|_||_\__,_|
         |_|                                                             

          1. obtener todos los codigos y ciudades
          2. obtener los telefonos de las oficinas de españa

""")
    
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys",  tablefmt = 'rounded_grid'))
    elif (opcion == 2):
        print(tabulate(getAllCiudadTelefono("España"), headers="keys",  tablefmt = 'rounded_grid'))
    