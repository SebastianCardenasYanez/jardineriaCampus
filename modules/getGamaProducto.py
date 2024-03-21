
import json
import requests

#ejercicio 15
def getAllGama():
    #json-server storage/producto.json -b 5502
    peticion = requests.get(f"http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data

def getAllidGP(codigo):
    peticion = requests.get(f"http://154.38.171.54:5004/gama/{codigo}")
    #json-server storage/producto.json -b 5501 
    return [peticion.json()] if peticion.ok else []

# def getAllNombre():
#     gamaNombre = []
#     for val in getAllGama(): 
#         if ("gama") == "Ornamentales":
#             gamaNombre.append(val.get("gama"))
#     return gamaNombre

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre

def getGamas():
    gamas = set()
    for val in getAllGama():
        gamas.add(val.get("gama"))
    return [gamas]