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
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre)is not None):
                    empleados["nombre"] = nombre
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")

            if (not empleados.get("apellido1")):
                apellido1 = input("Ingrese el primer apellido del empleado: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido1)is not None):
                    empleados["apellido1"] = apellido1
                    break
                else:
                    raise Exception("El nombre no comple con el estandar establecido")
            
            if (not empleados.get("apellido2")):
                apellido2 = input("Ingrese el segundo apellido del empleado: ")
                if (re.match(r'^[A-Z][a-zA-Z0-9\s]*$', apellido2)is not None):
                    empleados["apellido1"] = apellido2
                    break
                else:
                    raise Exception("El apellido no comple con el estandar establecido")
            
            if (not empleados.get("extension")):
                extension = input("Ingrese la fecha en la que se realizo el pago: ")
                if (re.match(r'^\d{4}$', extension)is not None):
                        empleados["id_transaccion"] = id
                        break
                else:
                    raise Exception("La extension no comple con el estandar establecido")

            if(not empleados.get("email")):
                email = input("Ingrese el nombre del empleado: ")
                if (re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$', nombre)is not None):
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


    peticion = requests.post("http://154.38.171.54:5003/empleados", data=json.dumps(empleados))
#falta la url bien hecha ..
    res = peticion.json()
    res["Mensaje"] = "Producto guardado"
    return res

def updateEmpleados(id):
    data = gE.getAllCodigoEmp(id)
    if data is None:
            print(f"""

Id del empleado no encontrado. """)
    
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
                if data[0][datoModificar] == data[0]["codigo_empleado"] or data[0][datoModificar]== data[0]["codigo_jefe"]:
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
    
    peticion = requests.put(f"http://154.38.171.54:5003/empleados/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Modificado"
    return [res]

def deleteEmpleados(id):
    data = gE.getAllCodigoEmp(id)
    if (len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5003/empleados{id}")
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
    
    # peticion = requests.delete("http://172.16.104.23:5503/pedidos/{id}")
#falta la url bien hecha ..
    # res = peticion.json()
    # res["Mensaje"] = "Producto eliminado"
    # return res


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
            2. Eliminar un empleado
            3. Actualizar un empleado
            0. Salir
              
              """)

        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=3):
                if (opcion == 1):
                    print(tabulate(postEmpleados(), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                    break
                elif (opcion == 2):
                    id = input("Ingrese el id del empleado que desea eliminar")
                    print(tabulate(deleteEmpleados(id), headers="keys",  tablefmt = 'rounded_grid'))
                    input("Precione una tecla para continuar....")
                elif (opcion == 3):
                    idEmpleado = input("Ingrese el id del empleado: ")
                    print(tabulate(updateEmpleados(idEmpleado), headers="keys", tablefmt='rounded_grid'))
                    input(f"""
        Escriba una tecla para continuar: """)
                elif (opcion == 0):
                    break