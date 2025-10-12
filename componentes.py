from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.programming.language import Java
from diagrams.saas.identity import Auth0
from diagrams.programming.framework import React, Spring
from diagrams.saas.automation import N8N
from diagrams.onprem.workflow import Airflow

with Diagram("Arquitectura de despliegue", show=False, outformat='png'):
    with Cluster("Web Server"):
        react = React("React + Vite")

    with Cluster("Backend"):
        spring = Spring("Spring Boot REST Service")

    with Cluster("Database"):
        db = PostgreSQL("Postgres DB")

   
    with Cluster("External Services"):
        n8n = N8N("SMPT Service")

    nginx_proxy = Nginx("nginx-proxy")

    # Requests normales
    react >> Edge(label="3. Request + JWT") >> nginx_proxy
    nginx_proxy >> Edge(label="Forward") >> spring

    # Operaciones backend
    spring >> Edge(label="Query") >> db
    spring >> Edge(label="Trigger Email Validation") >> n8n

    n8n >> spring

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
    
    # Servicio externo
    with Cluster("External Services"):
        n8n = Custom("n8n Workflow", "icons/n8n.png") if False else \
              N8N("Mail Validation\nWorkflow")
    
    # Flujo de comunicación
    react >> Edge(label="HTTPS") >> nginx_proxy
    nginx_proxy >> Edge(label="HTTP") >> spring
    
    # Spring Boot interacciones
    spring >> Edge(label="SQL Query") >> db
    spring >> Edge(label="Trigger") >> n8n
    spring - Edge(label="uses", style="dashed") - jwt
    spring - Edge(label="uses", style="dashed") - business
    
    # Respuestas (opcional, para mostrar flujo bidireccional)
    # nginx_proxy << spring
    # react << nginx_proxy   
