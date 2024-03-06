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
#ejercicio 4
def getAllPuestoNombreApellidosEmailJefe(jefe):
    puestoJefe = []
    for val in em.empleados:
        if val.get("puesto") == jefe:
            puestoJefe.append({
                "nombre" : val.get("nombre"),
                "apellidos" : f"{val.get('apellido1')}{val.get('apellido2')}",
                "email" : val.get("email")
            
            })
    return puestoJefe
#ejercicio 5
def getAllPuestoNombreApellidosEmpleados(puesto):
    puestoEmpleado = []
    for val in em.empleados:
        if val.get("puesto") != puesto:
            puestoEmpleado.append({
                "nombre" : val.get("nombre"),
                "apellidos" : f"{val.get('apellido1')}{val.get('apellido2')}"
            })
    return puestoEmpleado            
