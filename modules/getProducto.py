import storage.producto as pro
#ejercicio 15
def getAllGamaProductos ():
    gamaProducto = []
    for val in pro.producto: 
        if val.get("gama") == "Ornamentales" and val.get("cantidad_en_stock") > 100:
            gamaProducto.append({
                "gama" : val.get("gama"),
                "cantidad_en_stock" : val.get("canditad_en_stock") 
            })
    return gamaProducto
