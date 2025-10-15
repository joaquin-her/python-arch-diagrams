from diagrams.aws.compute import EC2

from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
from diagrams import Diagram, Cluster, Edge
from diagrams.generic.os import Android, IOS, Windows
from diagrams.aws.network import APIGateway


with Diagram("diagrama_de_procesos", show=False, outformat='png', direction='LR', curvestyle="curved"):
    
    # Define the load balancer and backend servers
    lb = APIGateway("Reverse Proxy")
    api_server = EC2("API Server (Backend)")
    frontend_server = EC2("Frontend Server")
    
    # Add database server
    db_server = RDS("Database Server")
    
    # Add user management services
    android_user_mgmt = Android("User (Android)")
    web_user_mgmt = Windows("User (Web)")
    ios_user_mgmt = IOS("User (iOS)")

    # Connect user management to backend servers
    android_user_mgmt >> lb
    web_user_mgmt >> Edge(label="Morfiuba.com") >> lb
    ios_user_mgmt >> lb

    
    # Define ports for communication
    lb >> Edge(label="HTTPS, Port 8080") >> api_server
    lb << api_server
    lb >> Edge(label="HTTPS, Port 80") >> frontend_server
    lb << frontend_server
    
    # Define ports for database connections
    api_server >> Edge(label="PostgreSQL, Port 5432") >> db_server