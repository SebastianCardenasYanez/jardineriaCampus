import storage.empleado as em

def getAllNombresApellidosEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleados:
        if (val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append({
                "nombre" : val.get("nombre"),
                "apellidos" : f"{val.get('apellido1')}{val.get('apellido2')}",
                "email" : val.get("email"),
                "jefe": val.get("codigo_jefe")
            })
    return nombreApellidoEmail