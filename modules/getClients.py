import storage.cliente as cli
from tabulate import tabulate

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
    print(""" 

  ___                   _               _          _ _         _          
 | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   __| (_)___ _ _| |_ ___ ___
 |   / -_| '_ \/ _ \ '_|  _/ -_|_-< / _` / -_| / _| | / -_) ' \  _/ -_|_-<
 |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| \__|_|_\___|_||_\__\___/__/
         |_|                                                              

          1. obtener todos los clientes (codigo y nombre)
          2. obtener un cliente por el codigo (codigo y nombre)
          3. obtener toda la informacion de un cliente segun su limite de credito y ciudad perteneciente ()
""")
    opcion = int(input("\nSeleccione una de las opciones: "))
    if (opcion == 1):
        print(tabulate(getAllClientName(), headers="keys",  tablefmt = 'rounded_grid'))
    elif (opcion == 2):
        codigoCliente = int(input("Ingrese el codigo del cliente: "))
        print(tabulate(getOneClientCodigo(codigoCliente), headers="keys",  tablefmt = 'rounded_grid'))
    elif (opcion == 3):
        limite = float(input("ingrese el limite de credito de los clientes vque deseas visualisar: "))
        ciudad = input("ingrese el nomnbre de la ciudad que deseas filtrar los cliente:")
        print(tabulate(getAllCLientCreditCiudad(limite, ciudad), headers="keys",  tablefmt = 'rounded_grid'))