from tabulate import tabulate
import requests
import json
import modules.postClients as postCli

def getAllDataClientes():
    peticion = requests.get("http://154.38.171.54:5001/cliente") #falta arreglar las url el visual no deja crearlos
    #json-server storage/cliente.json -b 5507 
    data = peticion.json()
    return data

def getCodigoCLientes(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente{codigo}")
    data = peticion.json()
    return data

def getAllDataEmpleados():
    peticion = requests.get("http://172.16.104.23:5506") #falta arreglar las url el visual no deja crearlos
    #json-server storage/empleado.json -b 5506 
    data = peticion.json()
    return data

def getAllDataPagos():
    peticion = requests.get("http://172.16.104.23:5504") #falta arreglar las url el visual no deja crearlos
    #json-server storage/pago.json -b 5504
    data = peticion.json()
    return data

def getAllClientName():
    clienteName = []
    for i,val in enumerate(getAllDataClientes()):
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
            })
    return clienteName

def getOneClientCodigo(codigo):
    variablehhahanose = []
    for val in getAllDataClientes():
        if(val.get('codigo_cliente') == codigo):
            variablehhahanose.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            })
    return variablehhahanose

def getAllCLientCreditCiudad(limitCredit, ciudad) :
    clienteCredic= list()
    for val in getAllDataClientes() :
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
    for val in getAllDataClientes() :
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
    for i, val in enumerate(getAllDataClientes()):
        clienteCode.append({
            "codigo_postal": val.get('codigo_postal')
        })
    return clienteCode

def getAllClienteFax():
    clienteFax = []
    for i, val in enumerate(getAllDataClientes()):
        clienteFax.append({
            "fax" : val.get('fax')
        })
    return clienteFax

def getAllClientePhone():
    clientePhone = []
    for i, val in enumerate(getAllDataClientes()):
        clientePhone.append({
            "telefono" : val.get('telefono')
        })
    return clientePhone

def getAllClienteContactoDatos():
    datosContacto = []
    for i, val in enumerate(getAllDataClientes()):
        datosContacto.append({
            "nombre_contacto" : val.get('nombre_contacto'),
            "apellido_contacto": val.get('apellido_contacto')
        })
    return datosContacto

def getAllClienteRepVentas(repVentas):
    clienteRepVentas = []
    for i, val in enumerate(getAllDataClientes()):
       if (val.get("codigo_empleado_rep_ventas") == repVentas):
           clienteRepVentas.append(val)
    return clienteRepVentas

#ejercicio 6
def getAllClienteNombrePais(Spain):
    clienteNamePais = []
    for val in getAllDataClientes():
        if (val.get("pais") == "Spain"):
            clienteNamePais.append({
                "nombre_cliente": val.get('nombre_cliente'),
                "Spain" : val.get("pais")
            })
    return clienteNamePais

#ejercicio 16
def getAllClienteMadridCodigo():
    clienteCiudad = []
    for val in getAllDataClientes():
        codigoRep = val.get("codigo_empleado_rep_ventas")   
        if (val.get("ciudad") == "Madrid"):
            if codigoRep != None and (codigoRep >= 11 and codigoRep <= 30 ):
                clienteCiudad.append({
                    "ciudad" : val.get("ciudad"),
                    "codigo empleado" : val.get("codigo_empleado_rep_ventas")
                })
    return clienteCiudad

#ejerecicio 1 2da parte
def getAllClienteNombreRepVentas():
    cliNomRep = []
    for val in getAllDataClientes():
        for empl in getAllDataEmpleados():
            if (val.get("codigo_empleado_rep_ventas") == empl.get("codigo_empleado")):
                cliNomRep.append({
                    "nombre del cliente": val.get("nombre_cliente"),
                    "nombre representante" : empl.get("nombre"),
                    "apellido" : empl.get("apellido1") and empl.get("apellido2")
                })
    return cliNomRep

#ejercicio 2 2da parte
def getAllCLientePago():
    clientepago = []
    for val in getAllDataClientes():
        for rep in getAllDataEmpleados():
            for pay in getAllDataPagos():
                if (val.get("codigo_cliente") == pay.get("codigo_cliente") and val.get("codigo_empleado_rep_ventas") == rep.get("codigo_empleado")):
                    clientepago.append({
                        "nombre cliente": val.get("nombre_cliente"),
                        "nombre representante": rep.get("nombre")
                    })
    return clientepago

#ejercicio 3 2da parte
def getAllCLienteNoPago():
    clienteNopago = set()
    for val in getAllDataClientes():
        for rep in getAllDataEmpleados():
            for pay in getAllDataPagos():
                if (val.get("codigo_cliente") != pay.get("codigo_cliente") and val.get("codigo_empleado_rep_ventas") == rep.get("codigo_empleado")):
                    clienteNopago.add(str(val.get("nombre_cliente")))
                    clienteNopago.add(str(rep.get("nombre")))
    return clienteNopago
    
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
          11.Obtener los codigos de los representantes de ventas de Madrid
          12.Obtener el nombre del cliente y de su representante de ventas
          13.Obrtener el nombre del cliente y de su representante de ventas si han hecho un pago
          14.Obrtener el nombre del cliente y de su representante de ventas si no han hecho un pago
          15. Administrar Clientes
""")
        opcion = int(input("\nSeleccione una de las opciones: "))
        if (opcion == 1):
            print(tabulate(getAllClientName(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 2):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            codigo = int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClientCodigo(codigo), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 3):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            limite = float(input("ingrese el limite de credito de los clientes vque deseas visualisar: "))
            ciudad = input("ingrese el nomnbre de la ciudad que deseas filtrar los cliente:")
            print(tabulate(getAllCLientCreditCiudad(limite, ciudad), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 4):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            pais = input("Ingrese el pais: ")
            region = input("Ingrese la region: ")
            ciudad = input("Ingrese la cudad: ")
            print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 5):
            print(tabulate(getAllClienteCodigoPostal(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 6):
            print(tabulate(getAllClienteFax(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 7):
            print(tabulate(getAllClientePhone(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 8):
            print(tabulate(getAllClienteContactoDatos(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 9):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            repVentas = int(input("Ingrese el codigo del representante de ventas: "))
            print(tabulate(getAllClienteRepVentas(repVentas), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 10):
            try:
                entrada = input("Ingresa Ctrl + c para ir a menu: ")
            except KeyboardInterrupt:
                menu()
            codigoCliente = int(input("Ingrese el codigo del cliente: "))
            Spain = input("Ingrese el pais: ")
            print(tabulate(getAllClienteNombrePais(Spain), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 11):
            print(tabulate(getAllClienteMadridCodigo(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 12):
            print(tabulate(getAllClienteNombreRepVentas(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 13):
            print(tabulate(getAllCLientePago(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif (opcion == 14):
            print(tabulate(getAllCLienteNoPago(), headers="keys",  tablefmt = 'rounded_grid'))
            #break
        elif(opcion == 15):
            postCli.menu()
        elif (opcion == 0):
            break
        input("presione una tecla para continuar")
        break