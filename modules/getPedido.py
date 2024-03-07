import storage.pedido as ped
#ejercicio 7
def getAllEstadosPedido():
    pedidoEstados = set()
    for i, val in enumerate(ped.pedido):
        pedidoEstados.add(val.get("pedido"))
        pedidoEstados.add(val.get("estado"))
    return pedidoEstados

#ejemplo profesor
from datetime import datetime
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0:
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado
#def getAllPedidosEntregadosAtrasadosDeTiempo():
#    pedidoEntregado = []
#    for val in ped.pedido:
#        if val.get("estado")== "Entegado" and val.get("fecha_entrega") is None:
 #           val["fecha_entrega"] = val.get ("fecha_esperada")
 #       if val.get("estado")== "Entregado":
 #               date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
 #               date2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
 #               start = datetime.strptime(date1, "%d/%m/%Y")
 #               end = datetime.strptime(date2, "%d/%m/%Y")
 #               diff =  end.date() - start.date()
 #               if(diff.days < 0):
 #                    pedidoEntregado.append({
 #                         "codigo_de_pedido": val.get("codigo_pedido"),
 #                         "codigo_de_cliente": val.get("codigo_cliente"),
 #                         "fecha_esperada": val.get("fecha_esperada"),
 #                         "fecha_de_entrega": val.get("fecha_entregada")
 #                    })

 #   return pedidoEntregado


#ejercicio 10
def getAllPedidosEntregadosAntesDeTiempo():
    pedidosEntregadosAntes = list()
    for val in ped.pedido:
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") == None):
            val["fecha_entrega"] = val.get("fecha_esperada")
        if (val.get("estado") == "Entregado"):
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days >= 2:
                pedidosEntregadosAntes.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregadosAntes

#ejercicio 11
def getAllPedidosRechazados():
    pedidoRechazado = []
    for val in ped.pedido:
        año = val.get("fecha_entrega")
        if (val.get("estado") == "Rechazado" and val.get("fecha_entrega") is not None):
            if año.startswith("2009"):
                pedidoRechazado.append({
                    "codigo_pedido": val.get ("codigo_pedido"),
                    "fecha_entrega": val.get ("fecha_entrega"),
                    "estado": val.get ("estado")
                })
    return pedidoRechazado
