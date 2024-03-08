import storage.oficina as of

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if (val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas" : val.get("cpodigo_oficina"),
                "pais" : val.get("pais") 
            })
    return ciudadTelefono

def menu():
    print(""" 
  ___                   _               _            __ _    _           
 | _ \___ _ __  ___ _ _| |_ ___ ___  __| |___   ___ / _(_)__(_)_ _  __ _ 
 |   / -_) '_ \/ _ \ '_|  _/ -_|_-< / _` / -_) / _ \  _| / _| | ' \/ _` |
 |_|_\___| .__/\___/_|  \__\___/__/ \__,_\___| \___/_| |_\__|_|_||_\__,_|
         |_|                                                             

          1. obtener todos los codigos y ciudad (codigo y nombre)
          2. obtener un cliente por el codigo (codigo y nombre)
          3. obtener toda la informacion de un cliente segun su limite de credito y ciudad perteneciente ()
""")
    
    