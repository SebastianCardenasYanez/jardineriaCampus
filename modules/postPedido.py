import json
import re
import requests
from tabulate import tabulate
import os
import modules.getPedido as gP


def postPedido():
    pedido = {}
    while True:
        try:
            if(not pedido.get("codigo_pedido")):
                codigo = int(input("Ingrese el codigo del pedido: "))
                if codigo is not None:
                    data = gP.getPedidoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo que ingreso ya existe ")
                    else: pedido['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
            
            if(not pedido.get("fecha_pedido")):
                date = input("Ingrese fecha en la que se realizo el pedido")
                if (re.match(r'^[0-9]{4}-[0-9]{2}-[0-1]{1}[0-9]{1}$', date)is not None):
                    pedido['fecha_pedido'] = date

                else :
                    raise Exception("La fecha no cumple con el estandar establecido")

            if(not pedido.get("fecha_esperada")):
                date = input("Ingrese fecha en la que se realizo el pedido")
                if (re.match(r'^[0-9]{4}-[0-9]{2}-[0-1]{1}[0-9]{1}$', date)is not None):
                    pedido['fecha_esperada'] = date

                elif date == None :
                    pedido['fecha_esperada'] = date

                else:
                    raise Exception("La fecha no cumple con el estandar establecido")

            if(not pedido.get("fecha_entrega")):
                dateE = input("Ingrese fecha en la que se realizo el pedido")
                if (re.match(r'^[0-9]{4}-[0-9]{2}-[0-1]{1}[0-9]{1}$', dateE)is not None):
                    pedido['fecha_pedido'] = dateE

                else :
                    raise Exception("La fecha no cumple con el estandar establecido")

            if(not pedido.get("estado")):
                estad = gP.getAllEstadosPedido()[int(input("Selecione el estado:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gP.getAllEstadosPedido())])))]
#no supe como hacer cuando es conjunto, preguntele al profe hermoso
            if (not pedido.get("comentario")):
                com = input("Ingrese un comentario: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', com)is not None):
                    pedido["comentario"] = com
                    break
                elif com == None : 
                    pedido["comentario"] = com
                else:
                    raise Exception("El comentario no comple con el estandar establecido")

            if (not pedido.get("codigo_cliente")):
                cod = int(input("Ingrese el codigo del cliente"))
                if cod is not None:
                    pedido["codigo_cliente"] = cod
                else: 
                    raise Exception("El codigo del cliete no comple con el estandar establecido")

        except Exception as error: 
            print(error)
    print(pedido)



    peticion = requests.post("http://172.16.100.126:5501", data=json.dumps(pedido))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res







def menu():
    while True: 
        os.system
        print(f"""


    _      _       _      _    _               _               _                        _         _          
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   _ __ _ _ ___  __| |_  _ __| |_ ___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` / _| / _ \ ' \  / _` / -_) | '_ \ '_/ _ \/ _` | || / _|  _/ _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| | .__/_| \___/\__,_|\_,_\__|\__\___/__/
                                                                      |_|                                    


            1. Agregar  un nuevo pedido
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postPedido(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion == 0):
            break