from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getPago as pago
import modules.getGamaProducto as gama
import modules.getProducto as producto

print(tabulate(producto.getAllStockPriceGama("Ornamentales", 100), tablefmt = 'rounded_grid'))

# def menu():
#     while True:
#         print(f""" 
        
#     __  ___                    ____       _            _             __
#    /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
#   / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
#  / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
# /_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
#                                                     /_/                

#                                 1. Cliente
#                                 2. Oficina
#                                 3. Empleados
#                                 4. Pedidos
#                                 0. Salir
# """)
#         opcion = int(input("\nSeleccione una de las opciones: "))
#         if (opcion == 1):
#             cliente.menu()
#         elif (opcion == 2):
#             oficina.menu()
#         elif (opcion == 3):
#             empleado.menu()
#         elif (opcion == 4):
#             pedidos.menu()
#         elif (opcion == 0):
#             print("""

#  _    _            _                                                   _                _                
# | |  | |          | |                                     _           | |              (_)_              
# | |  | |   _  ____| |_   _ ____    ____   ____ ___  ____ | |_  ___    | | _   ____  ___ _| |_  ___   ___ 
#  \ \/ / | | |/ _  ) | | | / _  |  |  _ \ / ___) _ \|  _ \|  _)/ _ \   | || \ / _  )/___) |  _)/ _ \ /___)
#   \  /| |_| ( (/ /| |\ V ( ( | |  | | | | |  | |_| | | | | |_| |_| |  | |_) | (/ /|___ | | |_| |_| |___ |
#    \/  \____|\____)_| \_/ \_||_|  | ||_/|_|   \___/|_| |_|\___)___/   |____/ \____|___/|_|\___)___/(___/ 
#                                   |_|                                                                    

                  
# """)
#             break

# menu()

#import sys
#for nombre, objeto in sys.modules.items():
#    if nombre.startswith("modules"):
#        print (nombre)
#        modulo = getattr(objeto,"__name__", None)
#        file = modulo.split(("get")[-1])
#        print(file)
