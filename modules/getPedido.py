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
    pedidoEntregado = []
    for val in ped.pedido:
        if val.get("estado")== "Entegado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get ("fecha_esperada")
        if val.get("estado")== "Entregado":
                date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
                date2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
                start = datetime.strptime(date1, "%d/%m/%Y")
                end = datetime.strptime(date2, "%d/%m/%Y")
                diff =  end.date() - start.date()
                if(diff.days < 0):
                     pedidoEntregado.append({
                          "codigo_de_pedido": val.get("codigo_pedido"),
                          "codigo_de_cliente": val.get("codigo_cliente"),
                          "fecha_esperada": val.get("fecha_esperada"),
                          "fecha_de_entrega": val.get("fecha_entregada")
                     })

    return pedidoEntregado

