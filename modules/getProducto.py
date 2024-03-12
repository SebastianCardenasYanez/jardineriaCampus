import storage.producto as pro
#ejercicio 15
def getAllStockPriceGama (gama, stock):
    condiciones =[]
    for val in pro.producto:
        if (val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
            
            # condiciones.append({
            #     "gama" : val.get("gama"),
            #     "precio de venta" : val.get("precio_venta") 
            # })
            
            #     "gama" : val.get("gama"),
            #     "cantidad_en_stock" : val.get("canditad_en_stock") 
            
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones) : 
        condiciones[i] = {
            "codigo": val.get("codigo_producto"),
            "venta": val.get("precio_venta"),
            "nombre": val.get("nombre"),
            "gama": val.get("gama"),
            "dimensiones" : val.get("dimensiones"),
            "proveedor": val.get("proveedor"), 
            "descripcion": f'(val.get("descripcion")[15])...' if condiciones[1].get("descripcion") else val.get("descripcion"),
            "stock": val.get("cantidad_en_stock"),
            "base" : val.get("precio_proveedor")
        }
        # if val.get("precio_venta") != None:
        #     condiciones.sort(key=price)
            
        # return val.get("precio_venta")
    return condiciones

