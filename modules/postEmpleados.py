import json
import re
import requests
from tabulate import tabulate
import os
import modules.getEmpleados as gE

def postEmpleados():
    empleados = {}
    while True:
        try:
            if(not empleados.get("codigo_empleado")):
                codigo = int(input("Ingrese el codigo de la empleados: "))
                if  codigo is not None:
                    empleados['codigo_empleados'] = codigo
                else : 
                    raise Exception("El codigo del empleado no comple con el estandar establecido ")
                
            if (not empleados.get("nombre")):
                nombre = input("Ingrese el nombre del empleado: ")
                if (re.match(r'^[A-Z][a-z]*\s*)+$', nombre)is not None):
                    empleados["nombre"] = nombre
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not empleados.get("apellido1")):
                apellido1 = input("Ingrese el primer apellido del empleado: ")
                if (re.match(r'^[A-Z][a-z]*)+$', apellido1)is not None):
                    empleados["apellido1"] = apellido1
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")
            
            if (not empleados.get("apellido2")):
                apellido2 = input("Ingrese el segundo apellido del empleado: ")
                if (re.match(r'^[A-Z][a-z]*)+$', apellido2)is not None):
                    empleados["apellido1"] = apellido2
                    break
                else:
                    raise Exception("El apellido no comple con el estandar establecido")
            
            if (not empleados.get("extension")):
                extension = input("Ingrese la fecha en la que se realizo el pago: ")
                if (re.match(r'^[0-9]{4}$', extension)is not None):
                        empleados["id_transaccion"] = id
                        break
                else:
                    raise Exception("La extension no comple con el estandar establecido")

            if(not empleados.get("email")):
                email = input("Ingrese el nombre del empleado: ")
                if (re.match(r'^[A-Z][a-z@\s]*$', nombre)is not None):
                    empleados["email"] = email
                    break
                else:
                    raise Exception("El email no comple con el estandar establecido")
            if(not empleados.get("codigo_oficina")):
                codofi = input("Ingrese fecha en la que se realizo el pedido")
                if (re.match(r'^[A-Z]{3}-[A-Z]{2}$', codofi)is not None):
                    empleados['codigo_oficiona'] = codofi

                else :
                    raise Exception("El codigo de la oficina no cumple con el estandar establecido")

            if(not empleados.get("codigo_jefe")): 
                codboss = int(input("Ingrese el codigo del jefe") )
                if codboss is not None:
                    empleados['fecha_esperada'] = codboss
                elif codboss == None :
                    empleados['fecha_esperada'] = codboss
                else:
                    raise Exception("El codigo del jefe no cumple con el estandar establecido")

            if (not empleados.get("puesto")):
                puesto = gE.getAllPuestos()[int(input("Selecione el estado:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gE.getAllPuestos())])))]
                empleados['forma_pago'] = puesto
                break
        except Exception as error: 
            print(error)
        print(empleados)


    peticion = requests.post("http://172.16.100.126:5501", data=json.dumps(empleados))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res


def menu():
    while True: 
        os.system
        print(f"""


    _      _       _      _    _               _               _                      _             _        
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ __(_)___ _ _    __| |___   ___ _ __  _ __| |___ __ _ __| |___ ___
  / _ \/ _` | '  \| | ' \| (_-<  _| '_/ _` / _| / _ \ ' \  / _` / -_) / -_) '  \| '_ \ / -_) _` / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_\__|_\___/_||_| \__,_\___| \___|_|_|_| .__/_\___\__,_\__,_\___/__/
                                                                                |_|                          

            1. Agregar un nuevo empleado
            0. Salir
              
              """)

        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(postEmpleados(), headers="keys",  tablefmt = 'rounded_grid'))
            input("Precione una tecla para continuar....")
            break
        elif (opcion == 0):
            break