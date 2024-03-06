import storage.pedido as ped
def getAllEstadosPedido():
    pedidoEstados = set()
    for i, val in enumerate(ped.pedido):
        pedidoEstados.add(val.get("pedido"))
        pedidoEstados.add(val.get("estado"))
    return pedidoEstados