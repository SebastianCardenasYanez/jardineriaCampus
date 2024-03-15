from tabulate import tabulate
import requests
import json

def getAllDataPagos():
    peticion = requests.get("http://172.16.100.126:5501") #falta arreglar las url el visual no deja crearlos
    #json-server storage/producto.json -b 5504
    data = peticion.json()
    return data



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

