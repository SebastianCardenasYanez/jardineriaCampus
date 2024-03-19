from tabulate import tabulate
import os 
import json
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getPago as pago
import modules.getGamaProducto as gama
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto



#print(tabulate(producto.getAllStockPriceGama("Ornamentales", 100), headers="keys", tablefmt = 'rounded_grid'))
# with open("storage/pago.json", "r") as f:
#     fichero = f.read()
#     data = json.loads(fichero)
#     for i, val in enumerate(data):
#         data[i]["id"] = (i+1)
#     data = json.dumps(data, indent=4).encode("utf-8")
#     with open("storage/pago.json", "wb+") as f1:
#         f1.write(data)
#         f1.close()



# def menuProducto():
#     while True:
#         os.system("clear")
#         print(f""" 

#     ____  _                            _     __               __                                     __   
#    / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __   ____/ /__ 
#   / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ /
#  / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /  / /_/ /  __/
# /_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/ 
#    / __ \_________  ____/ /_  _______/ /_____  _____                                                      
#   / /_/ / ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                                      
#  / ____/ /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                                       
# /_/   /_/   \____/\__,_/\__,_/\___/\__/\____/____/                                                        
                                                                                                          

#                     1. Reportes de los productos
#                     2. Guardar, Actualizar y Eliminar productos
#                     0. Regresar al menu principal
#     """)
#         opcion = int(input("\nSeleccione una de las opciones: "))
#         if (opcion == 1):
#             Repproducto.menu()
#         elif (opcion == 2):
#             CRUDproducto.menu()
#         elif (opcion == 0):
#             break

# if (__name__ == "__main__"):
#     while True:
#         os.system("clear")
#         print(f""" 
            
#         __  ___                    ____       _            _             __
#        /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
#       / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
#      / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
#     /_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
#                                                         /_/                

#                                     1. Cliente
#                                     2. Oficina
#                                     3. Empleados
#                                     4. Pedidos
#                                     5. Producto
#                                     0. Salir
#     """)
#         opcion = int(input("\nSeleccione una de las opciones: "))
#         if (opcion == 1):
#             cliente.menu()
#         elif (opcion == 2):
#             oficina.menu()
#         elif (opcion == 3):
#             empleado.menu()
#         elif (opcion == 4):
#             pedidos.menu()
#         elif (opcion == 5):
#             menuProducto()
#         elif (opcion == 0):
#                     print("""

#          _    _            _                                                   _                _                
#         | |  | |          | |                                     _           | |              (_)_              
#         | |  | |   _  ____| |_   _ ____    ____   ____ ___  ____ | |_  ___    | | _   ____  ___ _| |_  ___   ___ 
#          \ \/ / | | |/ _  ) | | | / _  |  |  _ \ / ___) _ \|  _ \|  _)/ _ \   | || \ / _  )/___) |  _)/ _ \ /___)
#           \  /| |_| ( (/ /| |\ V ( ( | |  | | | | |  | |_| | | | | |_| |_| |  | |_) | (/ /|___ | | |_| |_| |___ |
#            \/  \____|\____)_| \_/ \_||_|  | ||_/|_|   \___/|_| |_|\___)___/   |____/ \____|___/|_|\___)___/(___/ 
#                                         |_|                                                                    

                        
#         """)
#                     break

       

#import sys
#for nombre, objeto in sys.modules.items():
#    if nombre.startswith("modules"):
#        print (nombre)
#        modulo = getattr(objeto,"__name__", None)
#        file = modulo.split(("get")[-1])
#        print(file)
