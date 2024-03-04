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