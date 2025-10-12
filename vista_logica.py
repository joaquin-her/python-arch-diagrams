from diagrams import Diagram, Cluster, Edge
from diagrams.programming.framework import React, Spring
from diagrams.aws.compute import EC2Instance
with Diagram("Vista Logica - Web Presentation", show=False, outformat='png', direction='TB'):
    with Cluster("Front"):
        web = EC2Instance("Web Application")
    with Cluster("Back"):
        backend = EC2Instance("Backend API")

with Diagram("Vista Logica - Backend Layers", show=False, outformat='png'):
    with Cluster(""):
        rest = EC2Instance("REST Controller")
        service = EC2Instance("Service Layer")
        domain = EC2Instance("Domain Model")
        persistance = EC2Instance("Persistence Layer")

        rest >> service >> domain >> persistance

