from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.programming.language import Java
from diagrams.programming.framework import React, Spring
from diagrams.saas.automation import N8N

graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho"  # Líneas más ordenadas
}
with Diagram("Arquitectura de Aplicación", 
             show=False, 
             outformat='png',
             graph_attr=graph_attr,
             direction="LR"):
    
    # Frontend
    with Cluster("Frontend"):
        react = React("React Client")
    
    # Reverse Proxy (entre Frontend y Backend)
    nginx_proxy = Nginx("nginx-proxy\n(Reverse Proxy)")
    
    # Backend
    with Cluster("Backend - Spring Boot"):
        with Cluster("Spring Boot Application"):
            spring = Spring("REST API")
            
            # Componentes internos de Spring Boot
            with Cluster("Servicios Internos"):
                jwt = Java("JWT Service\n(Spring Security)")
                business = Java("Business Logic")
                
        db = PostgreSQL("PostgreSQL\nDatabase")
    
    # Flujo de comunicación
    react >> Edge(label="HTTPS") >> nginx_proxy
    nginx_proxy >> Edge(label="HTTP") >> spring
    
    # Spring Boot interacciones
    spring >> Edge(label="SQL Query") >> db
    spring - Edge(label="uses", style="dashed") - jwt
    spring - Edge(label="uses", style="dashed") - business
