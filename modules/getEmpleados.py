from tabulate import tabulate
import requests
import json
import modules.postEmpleados as postEmp

def getAllDataEmpleados():
    peticion = requests.get("http://154.38.171.54:5003/empleados") #falta arreglar las url el visual no deja crearlos
    #json-server storage/producto.json -b 5506 
    data = peticion.json()
    return data

def getAllCodigoEmp(codigo):
    peticion = requests.get(f"http://154.38.171.54:5003/empleados{codigo}")
    data = peticion.json()
    return data

def getAllPuestos():
    Puestos = set()
    for val in getAllDataEmpleados():
        if(val.get("puesto")):
            Puestos.add(val.get("puesto"))
    return [Puestos]

def getAllNombresApellidosEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in getAllDataEmpleados():
        if (val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append({
                "nombre" : val.get("nombre"),
                "apellidos" : f"{val.get('apellido1')}{val.get('apellido2')}",
                "email" : val.get("email"),
                "jefe": val.get("codigo_jefe")
            })
    return nombreApellidoEmail
#ejercicio 4
def getAllPuestoNombreApellidosEmailJefe(jefe):
    puestoJefe = []
    for val in getAllDataEmpleados():
        if val.get("puesto") == jefe:
            puestoJefe.append({
                "nombre" : val.get("nombre"),
                "apellidos" : f"{val.get('apellido1')}{val.get('apellido2')}",
                "email" : val.get("email")
            
            })
    return puestoJefe
#ejercicio 5
def getAllPuestoNombreApellidosEmpleados(puesto):
    puestoEmpleado = []
    for val in getAllDataEmpleados():
        if val.get("puesto") != puesto:
            puestoEmpleado.append({
                "nombre" : val.get("nombre"),
                "apellidos" : f"{val.get('apellido1')}{val.get('apellido2')}"
            })
    return puestoEmpleado            


def menu():
    while True:
        print(f""" 
            
    ___                   _               _                      _             _        
    | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   ___ _ __  _ __| |___ __ _ __| |___ ___
    |   / -_) '_ \/ _ \ '_|  _/ -_|_-< / _` / -_) / -_) '  \| '_ \ / -_) _` / _` / _ (_-<
    |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| \___|_|_|_| .__/_\___\__,_\__,_\___/__/
            |_|                                             |_|                          

                                    1. Obtener los datos del jefe
                                    2. Obtener los nombres de los empleados
                                    3. Administrar empleados
                                    0. Regresar al menu principal

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllNombresApellidosEmailJefe(1), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 2):
            print(tabulate(getAllPuestoNombreApellidosEmpleados("Representante Ventas"), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif(opcion == 3):
            postEmp.menu()
        elif (opcion == 0):
            break
        input("presione una tecla para continuar")
        break