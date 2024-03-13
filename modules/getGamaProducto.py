
import json
import requests

#ejercicio 15
def getAllGama():
    #json-server storage/producto.json -b 5502
    peticion = requests.get("http://172.16.100.126:5502")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama(): 
        if ("gama") == "Ornamentales":
            gamaNombre.append(val.get("gama"))
    return gamaNombre