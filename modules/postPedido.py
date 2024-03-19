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



    peticion = requests.post("http://172.16.104.23:5503/pedidos", data=json.dumps(pedido))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Pedido eliminado"
    return res


def deletePedido(id):
    data = gP.getPedidoCodigo(id)
    if (len(data)):
        peticion = requests.delete(f"http://172.16.104.23:5503/pedidos/{id}")
        if(peticion.status_code == 204):
            data.append({"message" : "producto eliminado correctamente"})
            return{
                "data" : data,
                "status" : peticion.status_code,
            }
    else : 
        return {
            "body" : [{
                "menssage" : "producto no  encontrado",
                "id": id
            }],
            "status" : 400
        }
    
    # peticion = requests.delete("http://172.16.104.23:5503/pedidos/{id}")
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto eliminado"
    return res



def menu():
    while True: 
        os.system
        print(f"""

    _      _       _      _    _               _               _                    _ _    _        
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   _ __  ___ __| (_)__| |___ ___
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) | '_ \/ -_) _` | / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| | .__/\___\__,_|_\__,_\___/__/
                                                                      |_|                           

            1. Agregar un nuevo pedido
            2. Eliminar un pedido
            0. Salir
              
              """)

        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=2):
                if (opcion == 1):
                    print(tabulate(postPedido(), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                    break
                elif (opcion == 2):
                    id = int(input("Ingrese el codigo del pedido que desea eleminar"))
                    print(tabulate(deletePedido(id), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                elif (opcion == 0):
                    break