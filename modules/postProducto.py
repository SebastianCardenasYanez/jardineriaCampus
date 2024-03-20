import json
import re
import requests
import os
from tabulate import tabulate
import modules.uptadeProducto as uP
import modules.getGamaProducto as gG
import modules.getProducto as gP




def postProducto():
    producto = {}
    while True:
        try:
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto: ")
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    data = gP.getProductoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo que ingreso ya existe ")
                    else: producto['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if (not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', nombre)is not None):
                    producto["nombre"] = nombre
                    break
                else:
                        raise Exception("El nombre no comple con el estandar establecido")
            
            if (not producto.get("gama")):
                gama = gP.getGamas()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gP.getGamas())])))]
                producto['gama'] = gama
                break

            if (not producto.get("dimensiones")):
                dim = input("Ingrese el codigo del producto: ")
                if (re.match(r'^[0-9]{2}-[0-9]{2}$', dim)is not None):
                    producto['dimensiones'] = dim

            if (not producto.get("proveedor")):
                proveedor = input("Ingrese el nombre del producto: ")
                if (re.match(r'^[A-Z][a-z]*\s*.*)+$', proveedor)is not None):
                    producto["proveedor"] = proveedor
                    break
                else:
                        raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("proveedor")):
                proveedor = input("Ingrese el nombre del producto: ")
                if (re.match(r'^[A-Z][a-z]*\s*.*)+$', proveedor)is not None):
                    producto["proveedor"] = proveedor
                    break
                else:
                        raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("cantidad_en_stock")):
                stock = int(input("Ingrese el nombre del producto: "))
                if stock is not None:
                    producto["cantidad_en_stock"] = stock
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("precio_venta")):
                precio = int(input("Ingrese el nombre del producto: "))
                if precio is not None:
                    producto["precio_venta"] = precio
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("precio_proveedor")):
                proveedor = int(input("Ingrese el nombre del producto: "))
                if stock is not None:
                    producto["precio_proveedor"] = proveedor
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

        except Exception as error: 
            print(error)
    print(producto)

    headers = {'Content-type' : 'aplication/json', 'charset' : 'UTF-8'}
    peticion = requests.post("http://172.16.102.108:5501/productos",headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res


# def deleteProducto(id):
#     data = gP.getProductoCodigo(id)
#     if (len(data)):
#         peticion = requests.delete(f"http://154.38.171.54:5007/pedidos{id}")
#         if(peticion.status_code == 204):
#             data.append({"message" : "producto eliminado correctamente"})
#             return  {
#                 "data" : data,
#                 "status" : peticion.status_code
#             }
#     else: 
#         return {
#             "body" : [{
#                 "menssage" : "producto no encontrado",
#                 "id": id
#             }],
#             "status" : 400,
#         }

def deleteProducto(id):
    data = gP.getProductoCodigo(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code
            }
    else:
        return {
            "body":[{
                "message":"producto no encontrado",
                "id": id
            }],
            "status": 400,
        }

    
    peticion = requests.delete("http://154.38.171.54:5008/productos/{id}")
    res = peticion.json()
    res["Mensaje"] = "Producto eliminado"
    return res



    #producto = {
    #    "codigo_producto": input("Ingrese el codigo del producto: "),
    #    "nombre": input("Ingrese el nombre del producto: "),
    #    "gama": gP.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gP.getAllNombre())])))],
    #    "dimensiones": input("Ingrse la dimensiones del producto: "),
    #    "proveedor": input("Ingrse el proveedor del producto: "),
    #    "descripcion": input("Ingrse el descripcion del producto: "),
    #    "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
    #    "precio_venta": int(input("Ingrse el precio de ventas: ")),
    #    "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    #}
    


def menu():
    while True: 
        os.system
        print(f"""


    _      _       _      _    _               _               _                        _         _          
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   _ __ _ _ ___  __| |_  _ __| |_ ___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` / _| / _ \ ' \  / _` / -_) | '_ \ '_/ _ \/ _` | || / _|  _/ _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| | .__/_| \___/\__,_|\_,_\__|\__\___/__/
                                                                      |_|                                    


            1. Agregar un nuevo producto
            2. Eliminar un producto
            3. actualizar producto
            0. Salir
              
              """)

        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=2):
                if (opcion == 1):
                    print(tabulate(postProducto(), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                    break
                elif( opcion == 2):
                    idProducto = input("Ingrese el id del producto que desea eliminar: ")
                    # deleteProducto(idProducto)
                    print(tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt="github"))
                elif (opcion ==3):
                    
                    uP.updateProductoNom()
                elif (opcion == 0):
                    break