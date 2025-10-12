import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([('User', 'Login'), ('User', 'View Profile'), 
                  ('Admin', 'Manage Users'), ('Admin', 'Login')])

nx.draw(G, with_labels=True, node_color='lightblue', 
        node_size=3000, font_size=10, arrows=True)
plt.show()