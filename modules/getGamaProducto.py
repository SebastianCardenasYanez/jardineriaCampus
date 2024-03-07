import storage.gama_producto as gam
#ejercicio 15
def getAllGamaProducto ():
    gamaProducto = []
    for val in gam.gama_producto: 
        if ("gama") == "Ornamentales":
            gamaProducto.append(val.get("gama"))
    return gamaProducto