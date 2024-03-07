from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedidos
import modules.getPago as pago
print(tabulate(pedidos.getAllPedidosEntregados(), tablefmt = 'rounded_grid'))

