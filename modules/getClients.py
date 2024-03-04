import storage.cliente as cli

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
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }

def getAllCLientCreditCiudad(limitCredit, ciudad) :
    clienteCredic= list()
    for val in cli.clientes :
        if (val.get('limite_credito') >= limitCredit and val.get('ciudad') == ciudad) :
            clienteCredic.append(val)
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
    