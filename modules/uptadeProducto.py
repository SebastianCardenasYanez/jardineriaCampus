import json
import requests
import modules.getProducto as gP
from tabulate import tabulate

def updateProducto(codigo):
    while True:
        if(codigo != None ):
            producto = gP.getProductoCodigo2(codigo)
            if (producto):
                print(tabulate(producto,headers="keys", tablefmt="rounded_grid"))
                opc = int(input("""
                ¿ Este es el producto que desea actualizar ?
                            1. Si
                            0. No
"""))
                if (opc):
                    headers = {'Contend-type':'application/json','charset' : 'UTF-8'}

                    producto[0]["nombre"] = input("ingrese el nuevo nombre del producto")

                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers=headers, data=json.dumps(producto))
                    data = peticion.json()
                    return [data]
                    
                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None
        else :
            codigo = input("ingrese el codigo del producto")



#     while True:
#         try:
#             print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
#             datoModificar = input(f"""
# Ingrese el dato que desea modificar: """)
#             print(f"""
# Datos para modificar: """)
#             for i, (val, asd) in enumerate(data[0].items()):
#                 print(f"{i+1}. {val}")

#             opcion = int(input(f"""
# Seleccione una opción: """))
#             datoModificar = list(data[0].keys())[opcion - 1]
#             nuevoValor = input(f"""
# Ingrese el nuevo valor para {datoModificar}: """)
#             if datoModificar in data[0]:
#                 if datoModificar == "cantidadEnStock" or "" or "":
#                 if datoModificar == "cantidadEnStock" or "precio_venta" or "precio_proveedor":
#                     data[0][datoModificar] = int(nuevoValor)
#                     break
#                 else:
#                     data[0][datoModificar] = nuevoValor
#                     print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
#                     break

 