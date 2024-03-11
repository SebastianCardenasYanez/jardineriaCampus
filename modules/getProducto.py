import storage.producto as pro
#ejercicio 15
def getAllStockPriceGama (gama, stock):
    condiciones =[]
    for val in pro.producto:
        if val.get("gama") == gama and val.get("precio_venta") >= stock:
            condiciones.append({
                "gama" : val.get("gama"),
                "cantidad_en_stock" : val.get("canditad_en_stock") 
            })
    return condiciones
