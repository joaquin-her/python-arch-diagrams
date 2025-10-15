from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

graph = {
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
}

icon_usuario = "icons/usuario.png"
icon_menu = "icons/menu.png"
icon_descuento = "icons/descuento.png"
icon_producto = "icons/agregar-producto.png"
icon_orden = "icons/atender.png"
icon_ingrediente = "icons/exportar.png"
icon_stock = "icons/gestion-de-productos.png"
icon_administrador = "icons/usuario.png"
icon_entregas = "icons/entregas.png"
"""
Modelos de dominio, glosarios, diagramas de alto nivel, etc
"""
with Diagram("Vista Dominio", 
             show=False, 
             outformat='png', 
             direction='LR',
             graph_attr=graph):
    
    with Cluster("Servicio a Usuarios"):
        usuarios = Custom("Usuarios", icon_usuario)
        menu = Custom("Menu", icon_menu)

    with Cluster("Modificable por Administradores"):
        producto = Custom("Producto", icon_producto)
        promocion = Custom("Promocion", icon_descuento)

    with Cluster("Servicio a Administradores"):
        ingrediente = Custom("Insumo", icon_ingrediente)
        stock = Custom("Stock", icon_stock)
        administrador = Custom("Administrador", icon_administrador)

    with Cluster("Servicio a Empleados"):
        orden = Custom("Orden", icon_orden)
        entregas = Custom("Pedidos", icon_entregas)
        cocinero = Custom("Cocineros", icon_usuario)
    


    usuarios >> menu
    usuarios >> Edge(label="Realizan pedidos") >> orden

    menu >> Edge(label="contiene") >> producto
    menu >> Edge(label="contiene") >> promocion
    promocion >> Edge(label="contiene 1 o varios en descuento")  >> producto
    orden >> Edge(label="contiene 1 o varias")  >> producto
    orden >> Edge(label="contiene 1 o varias")  >> promocion

    cocinero >> Edge(label="Controlan el estado") >> entregas
    entregas >> Edge(label="contiene varias") >> orden

    ingrediente >> Edge(label="Es usado en") >> producto
    stock >> Edge(label="contiene las cantidades de todos") >> ingrediente
    administrador >> Edge(label="gestiona") >> stock