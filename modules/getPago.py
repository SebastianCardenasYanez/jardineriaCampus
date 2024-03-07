import storage.pago as pag
#ejercicio 8
def getAllCodigoClienteAñoPago() :
    codigoPago = set()
    for val in pag.pago:
        año = val.get("fecha_pago")
        if año.startswith("2008"):
            codigoPago.add(val.get('fecha_pago'))
            codigoPago.add(val.get('codigo_cliente'))
    return codigoPago
        
#ejercicio 13
def getAllFormaDePago() :
    formaPago = []
    #sorted ()reverse = true
    for val in pag.pago:
        año = val.get("fecha_pago")
        forma = val.get("forma_pago")
        if año.startswith("2008") and forma == "PayPal":
            formaPago.append(val)
    return formaPago
        
#ejercicio 14