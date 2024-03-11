import storage.cliente as cli
from tabulate import tabulate
import sys

def getAllClientName():
    clienteName = []
    for i,val in enumerate(cli.clientes):
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
    return clienteName

def getOneClientCodigo(codigo):
    for i,val in enumerate(cli.clientes):
        if(val.get('codigo_cliente')== codigo):
            return [{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }]

def getAllCLientCreditCiudad(limitCredit, ciudad) :
    clienteCredic= list()
    for val in cli.clientes :
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad) :
            clienteCredic.append({
                "codigo": val.get('codigo_cliente'),
                "Responsable" : (val.get('nombre_contacto'), val.get('apellido_contacto')),
                "Director" : val.get('codigo_cliente'),
                "Telefono" : val.get('telefono'),
                "Fax" : val.get('fax'),
                "Direcciones" : (val.get('linea_direccion1'), val.get('linea_direccion2')),
                "Origen" : (val.get('pais'), val.get('ciudad')),
                "Codigo del asesor" : val.get('codigo_empleado_rep_ventas'),
                "Credito" : val.get('limite_credito')
            })
    return clienteCredic
    
def getAllClientPaisRegionCiudad(pais, region, ciudad):
    clientZone = list()
    for val in cli.clientes :
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) or 
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ) :
            clientZone.append(val)
    return clientZone

    #mis 5 filtros agregados

def getAllClienteCodigoPostal():
    clienteCode = []
    for i, val in enumerate(cli.clientes):
        clienteCode.append({
            "codigo_postal": val.get('codigo_postal')
        })
    return clienteCode

def getAllClienteFax():
    clienteFax = []
    for i, val in enumerate(cli.clientes):
        clienteFax.append({
            "fax" : val.get('fax')
        })
    return clienteFax

def getAllClientePhone():
    clientePhone = []
    for i, val in enumerate(cli.clientes):
        clientePhone.append({
            "telefono" : val.get('telefono')
        })
    return clientePhone

def getAllClienteContactoDatos():
    datosContacto = []
    for i, val in enumerate(cli.clientes):
        datosContacto.append({
            "nombre_contacto" : val.get('nombre_contacto'),
            "apellido_contacto": val.get('apellido_contacto')
        })
    return datosContacto

def getAllClienteRepVentas(repVentas):
    clienteRepVentas = []
    for i, val in enumerate(cli.clientes):
       if (val.get("codigo_empleado_rep_ventas") == repVentas):
           clienteRepVentas.append(val)
    return clienteRepVentas

#ejercicio 6
def getAllClienteNombrePais(Spain):
    clienteNamePais = []
    for val in cli.clientes:
        if (val.get("pais") == "Spain"):
            clienteNamePais.append({
                "nombre_cliente": val.get('nombre_cliente'),
                "Spain" : val.get("pais")
            })
    return clienteNamePais

def menu():
    while True: 
        print(""" 

  ___                   _               _          _ _         _          
 | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   __| (_)___ _ _| |_ ___ ___
 |   / -_| '_ \/ _ \ '_|  _/ -_|_-< / _` / -_| / _| | / -_) ' \  _/ -_|_-<
 |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| \__|_|_\___|_||_\__\___/__/
         |_|                                                              

          0. Resgresar al menu principal
          1. Obtener todos los clientes (codigo y nombre)
          2. Obtener un cliente por el codigo (codigo y nombre)
          3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad perteneciente ()
          4. Obtener el pais, region y ciudad de los clientes
          5. Obtener todos los codigos postales de los clientes
          6. Obtener los Faxs de los clientes 
          7. Obtener todos los nuemros de telefomo de los clientes
          8. Obtener los nombres y apellidos de los contactos de los clientes
          9. Obtener el representante de ventas
          10.Obtener los clientes de España
""")
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllClientName(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 2):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            codigoCliente = int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClientCodigo(codigoCliente), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 3):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            limite = float(input("ingrese el limite de credito de los clientes vque deseas visualisar: "))
            ciudad = input("ingrese el nomnbre de la ciudad que deseas filtrar los cliente:")
            print(tabulate(getAllCLientCreditCiudad(limite, ciudad), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 4):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            pais = input("Ingrese el pais: ")
            region = input("Ingrese la region: ")
            ciudad = input("Ingrese la cudad: ")
            print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 5):
            print(tabulate(getAllClienteCodigoPostal(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 6):
            print(tabulate(getAllClienteFax(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 7):
            print(tabulate(getAllClientePhone(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 8):
            print(tabulate(getAllClienteContactoDatos(), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 9):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            repVentas = int(input("Ingrese el codigo del representante de ventas: "))
            print(tabulate(getAllClienteRepVentas(repVentas), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 10):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            codigoCliente = int(input("Ingrese el codigo del cliente: "))
            Spain = input("Ingrese el pais: ")
            print(tabulate(getAllClienteNombrePais(Spain), headers="keys",  tablefmt = 'rounded_grid'))
            break
        elif (opcion == 0):
            break