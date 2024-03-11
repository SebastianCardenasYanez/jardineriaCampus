import storage.producto as pro
#ejercicio 15
def getAllStockPriceGama (gama, stock):
    condiciones =[]
    for val in pro.producto:
        if (val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append({
                "gama" : val.get("gama"),
                "precio de venta" : val.get("precio_venta") 
            })
            
            #     "gama" : val.get("gama"),
            #     "cantidad_en_stock" : val.get("canditad_en_stock") 
            
    def price(val):
        if val.get("precio_venta") != None:
            condiciones.sort(key=price)
            
        return val.get("precio_venta")
    return condiciones

