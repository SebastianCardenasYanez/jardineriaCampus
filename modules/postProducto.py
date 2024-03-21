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
                if (re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo)is not None):
                    data = gP.getProductoCodigo1 (codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo que ingreso ya existe ")
                    else: 
                        producto['codigo_producto'] = codigo
                else : 
                    raise Exception("El codigo no comple con el estandar establecido ")
                
            if (not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre)is not None):
                    producto["nombre"] = nombre
                else:
                        raise Exception("El nombre no comple con el estandar establecido")
            
            if (not producto.get("gama")):
                gama = input("ingrese la gama del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    gam = gG.getAllNombre()
                    if gam:
                        producto['gama'] = gama
                    else:
                        raise Exception("Gamas validas : (Herbaceas, Herramientas, Aromaticas, Frutales, Ornamentales)")
                else:
                    raise Exception("Gamas validas : (Herbaceas, Herramientas, Aromaticas, Frutales, Ornamentales)")
                #gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))]
            

            if (not producto.get("dimensiones")):
                dim = input("Ingrese las dimensiones del producto: ")
                if (re.match(r'^[0-9]{2}-[0-9]{2}$', dim)is not None):
                    producto['dimensiones'] = dim

            if (not producto.get("proveedor")):
                proveedor = input("Ingrese el nombre del proveedor del producto: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', proveedor)is not None):
                    producto["proveedor"] = proveedor
                    
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("descripcion")):
                descripcion = input("Ingrese la descripcion del producto: ")
                producto["descripcion"] = descripcion
                # if (re.match(r'^[A-Z][a-z]*\s*.*+$', proveedor)is not None):
                #     producto["proveedor"] = proveedor
                #     break
                # else:
                #         raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("cantidadEnStock")):
                stock = int(input("Ingrese el stock del producto: "))
                if stock is not None:
                    producto["cantidadEnStock"] = stock
                    
                else:
                    raise Exception("La cantidad no comple con el estandar establecido")

            if (not producto.get("precio_venta")):
                precio = int(input("Ingrese el precio de venta del producto: "))
                if precio is not None:
                    producto["precio_venta"] = precio
                    
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not producto.get("precio_proveedor")):
                proveedor = int(input("Ingrese el precio del proveedor del producto: "))
                if stock is not None:
                    producto["precio_proveedor"] = proveedor
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

        except Exception as error: 
            print(error)
    print(producto)

    headers = {'Content-type' : 'aplication/json', 'charset' : 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5008/productos",headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res



def updateProducto(id):
            data = gP.getProductoCodigo1(id)
            if data is None:
                print(f"""

Id del producto no encontrado. """)
    
            while True:
                try:
                    print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                    print(f"""
        Datos para modificar: """)
                    for i, (val, asd) in enumerate(data[0].items()):
                        print(f"{i+1}. {val}")

                    opcion = int(input(f"""
        Seleccione una opción: """))
                    datoModificar = list(data[0].keys())[opcion - 1]
                    nuevoValor = input(f"""
        Ingrese el nuevo valor para {datoModificar}: """)
                    if datoModificar in data[0]:
                        if data[0][datoModificar] == data[0]["cantidadEnStock"] or data[0][datoModificar] == data[0]["precio_venta"] or data[0][datoModificar] == data[0]["precio_proveedor"]:
                            data[0][datoModificar] = int(nuevoValor)
                            break
                        else:
                            data[0][datoModificar] = nuevoValor
                            
                            break
                    else:
                        print(f"""
        Seleccion incorrecta""")
                        
                except ValueError as error:
                    print(error)
            
            peticion = requests.put(f"http://154.38.171.54:5008/productos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Producto Modificado"
            return [res]


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
#peticion = requests.delete(f"http://154.38.171.54:5008/productos?id{id}")
def deleteProducto(id):
    
    data = gP.getProductoCodigo1(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        
        if peticion.status_code == 200:
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code
            }
        else:
            return {
                "body": [{"message": "Error al eliminar el producto"}],
                "status": peticion.status_code
            }
    else:
        return {
            "body": [{"message": "Producto no encontrado", "id": id}],
            "status": 404 }




    # else:
    #     return {
    #         "body":[{
    #             "message":"producto no encontrado",
    #             "id": id
    #         }],
    #         "status": 400,
    #         }

    
    # res = dict()
    # res["Mensaje"] = "Producto eliminado"
    # return res



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
            3. Actualizar un producto
            0. Salir
              
              """)

        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=3):
                if (opcion == 1):
                    print(tabulate(postProducto(), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                    break
                elif(opcion == 2):
                    idProducto = input("Ingrese el id del producto que desea eliminar: ")
                    # deleteProducto(idProducto)
                    print(tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt='rounded_grid'))
                elif (opcion ==3):
                    idEmpleado = input("Ingrese el id del Empleado: ")
                    print(tabulate(updateProducto(idEmpleado), headers="keys", tablefmt='rounded_grid'))
                    input(f"""
Escriba una tecla para continuar: """)
                elif (opcion == 0):
                    break