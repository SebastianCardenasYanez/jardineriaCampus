from tabulate import tabulate
import requests
import json

def getAllDataEmpleados():
    peticion = requests.get("http://172.16.100.126:5501") #falta arreglar las url el visual no deja crearlos
    #json-server storage/producto.json -b 5506 
    data = peticion.json()
    return data

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
                                    0. Regresar al menu principal

    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllNombresApellidosEmailJefe(1), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 2):
            print(tabulate(getAllPuestoNombreApellidosEmpleados("Representante Ventas"), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 0):
            break