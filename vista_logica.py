from diagrams import Diagram, Cluster, Edge
from diagrams.programming.framework import React, Spring
from diagrams.aws.compute import EC2Instance
graph = {
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
}
"""
Modelos de dominio, glosarios, diagramas de alto nivel, etc
"""
with Diagram("Vista Logica", 
             show=False, 
             outformat='png', 
             direction='LR',
             graph_attr=graph):
    with Cluster("Front"):
        web = EC2Instance("Web Application")
    with Cluster("Back"):
        backend = EC2Instance("Backend API")

    with Cluster("", graph_attr={"labelloc":"c"}):
        rest = EC2Instance("REST Controller")
        service = EC2Instance("Service Layer")
        domain = EC2Instance("Domain Model")
        persistance = EC2Instance("Persistence Layer")

    rest >> service >> domain >> persistance

