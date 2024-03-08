from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getPago as pago
import modules.getGamaProducto as gama
import modules.getProducto as producto

#print(tabulate(pago.getAllFormaDePago2008(), tablefmt = 'rounded_grid'))

def menu():
    print(f""" 
        
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                

                                1. cliente
                                2. oficina
                                3. cliente
                                4. pedidos
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        cliente.menu()
    elif (opcion == 2):
        oficina.menu()
    elif (opcion == 3):
        empleado.menu()
    elif (opcion == 4):
        pedidos.menu()

menu()

#import sys
#for nombre, objeto in sys.modules.items():
#    if nombre.startswith("modules"):
#        print (nombre)
#        modulo = getattr(objeto,"__name__", None)
#        file = modulo.split(("get")[-1])
#        print(file)
