#import storage.pedido as ped
from tabulate import tabulate
import requests
import json
import modules.postPedido as postPed

def getAllDataPedidos():
    peticion = requests.get("http://172.16.104.23:5503") #falta arreglar las url el visual no deja crearlos
    #json-server storage/producto.json -b 5503 
    data = peticion.json()
    return data
    

def getPedidoCodigo(codigo):
    peticion = requests.get(f"http://172.16.104.23:5503/pedidos/{codigo}")
    #json-server storage/producto.json -b 5503
    return [peticion.json()] if peticion.ok else []

#ejercicio 7
def getAllEstadosPedido():
    pedidoEstados = set()
    for val in getAllDataPedidos():
        pedidoEstados.add(val.get("estado"))
    return [pedidoEstados]

#ejemplo profesor
from datetime import datetime
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = list()
    for val in getAllDataPedidos():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0:
                pedidosEntregado.append({
                    "codigo de pedido": val.get("codigo_pedido"),
                    "codigo de cliente": val.get("codigo_cliente"),
                    "fecha esperada": val.get("fecha_esperada"),
                    "fecha de entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado
#def getAllPedidosEntregadosAtrasadosDeTiempo():
#    pedidoEntregado = []
#    for val in ped.pedido:
#        if val.get("estado")== "Entegado" and val.get("fecha_entrega") is None:
 #           val["fecha_entrega"] = val.get ("fecha_esperada")
 #       if val.get("estado")== "Entregado":
 #               date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
 #               date2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
 #               start = datetime.strptime(date1, "%d/%m/%Y")
 #               end = datetime.strptime(date2, "%d/%m/%Y")
 #               diff =  end.date() - start.date()
 #               if(diff.days < 0):
 #                    pedidoEntregado.append({
 #                         "codigo_de_pedido": val.get("codigo_pedido"),
 #                         "codigo_de_cliente": val.get("codigo_cliente"),
 #                         "fecha_esperada": val.get("fecha_esperada"),
 #                         "fecha_de_entrega": val.get("fecha_entregada")
 #                    })

 #   return pedidoEntregado


#ejercicio 10
def getAllPedidosEntregadosAntesDeTiempo():
    pedidosEntregadosAntes = list()
    for val in getAllDataPedidos():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2:
                pedidosEntregadosAntes.append({
                    "codigo de pedido": val.get("codigo_pedido"),
                    "codigo de cliente": val.get("codigo_cliente"),
                    "fecha esperada": val.get("fecha_esperada"),
                    "fecha de entrega": val.get("fecha_entrega")
                })
    return pedidosEntregadosAntes

#ejercicio 11
def getAllPedidosRechazados():
    pedidoRechazado = []
    for val in getAllDataPedidos():
        año = val.get("fecha_entrega")
        if (val.get("estado") == "Rechazado" and val.get("fecha_entrega") is not None):
            if año.startswith("2009"):
                pedidoRechazado.append({
                    "codigo": val.get ("codigo_pedido"),
                    "fecha": val.get ("fecha_entrega"),
                    "estado": val.get ("estado")
                })
    return pedidoRechazado

#ejercicio 12
def getAllPedidosEntregados():
    pedidoEntregados = []
    for val in getAllDataPedidos():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") is not None):
                fechaEntregada = "/".join(val.get("fecha_esperada").split("-")[::-1])
                start = datetime.strptime(fechaEntregada, "%d/%m/%Y")
                if start.month == 1 : 
                    pedidoEntregados.append({
                        "codigo pedido": val.get("codigo_pedido"),
                        "estado": val.get("estado"),
                        "fecha de entrega" : val.get("fecha_entrega"),
                        "fecha esperada" : val.get("fecha_esperada")
                    })
    return pedidoEntregados

def menu():
    while True:
        print(f""" 

    ___                   _               _                    _ _    _        
    | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   _ __  ___ __| (_)__| |___ ___
    |   / -_) '_ \/ _ \ '_|  _/ -_|_-< / _` / -_) | '_ \/ -_) _` | / _` / _ (_-<
    |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| | .__/\___\__,_|_\__,_\___/__/
            |_|                                   |_|                           

                                    1. Obtener los estados de los pedidos
                                    2. Obtener los pedidos atrasados
                                    3. Obtener los pedidos entregados antes de tiempo
                                    4. Obtener los pedidos rechazados
                                    5. Obtener los pedidos entregados
                                    6. administrar los pedidos
                                    0. Regresar al menu principal

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllEstadosPedido(),headers = "keys", tablefmt = 'rounded_grid'))
            break
        elif (opcion == 2):
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 3):
            print(tabulate(getAllPedidosEntregadosAntesDeTiempo(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 4):
            print(tabulate(getAllPedidosRechazados(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 5):
            print(tabulate(getAllPedidosEntregados(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 6):
            postPed.menu()
        elif (opcion == 0):
            break