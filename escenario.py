import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Ellipse, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(14, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Escenarios', 
        fontsize=18, fontweight='bold', ha='center')

# System boundary
system_box = FancyBboxPatch((2, 1), 6, 6, 
                            boxstyle="round,pad=0.1", 
                            edgecolor='black', 
                            facecolor='lightblue', 
                            alpha=0.2, 
                            linewidth=2)
ax.add_patch(system_box)

# Actors
# User (left)
user_circle = Ellipse((1, 4), 0.3, 0.4, color='lightcoral', ec='black', linewidth=2)
ax.add_patch(user_circle)
ax.plot([1, 1], [3.8, 3.2], 'k-', linewidth=2)
ax.plot([1, 0.7], [3.2, 2.7], 'k-', linewidth=2)
ax.plot([1, 1.3], [3.2, 2.7], 'k-', linewidth=2)
ax.plot([1, 0.7], [3.5, 3], 'k-', linewidth=2)
ax.plot([1, 1.3], [3.5, 3], 'k-', linewidth=2)
ax.text(1, 2.3, 'User', fontsize=11, ha='center', fontweight='bold')

# Administrator (right)
admin_circle = Ellipse((9, 4), 0.3, 0.4, color='lightgreen', ec='black', linewidth=2)
ax.add_patch(admin_circle)
ax.plot([9, 9], [3.8, 3.2], 'k-', linewidth=2)
ax.plot([9, 8.7], [3.2, 2.7], 'k-', linewidth=2)
ax.plot([9, 9.3], [3.2, 2.7], 'k-', linewidth=2)
ax.plot([9, 8.7], [3.5, 3], 'k-', linewidth=2)
ax.plot([9, 9.3], [3.5, 3], 'k-', linewidth=2)
ax.text(9, 2.3, 'Administrator', fontsize=11, ha='center', fontweight='bold')

# Use Cases (Ellipses)
use_cases = {
    # User use cases
    'iniciar_sesion': (3.5, 6, 'Iniciar Sesion'),
    'ver_menu': (3.5, 5, 'Ver Menú'),
    'ver_promociones': (3.5, 4, 'Ver Promociones'),
    'armar_carrito': (3.5, 3, 'Armar Carrito'),
    'comprar_y_ordenar': (3.5, 2, 'Comprar y Ordenar'),
    
    # Admin use cases
    'modify_stock': (6.5, 6, 'Modificar Stock'),
    'manage_orders': (6.5, 5, 'Gestionar Ordenes'),
    'update_menu': (6.5, 4, 'Altualizar Menú'),
    'generate_discounts': (6.5, 3, 'Generar Descuentos'),
}

# Draw use case ellipses
for key, (x, y, label) in use_cases.items():
    ellipse = Ellipse((x, y), 1.2, 0.6, color='white', ec='black', linewidth=1.5)
    ax.add_patch(ellipse)
    ax.text(x, y, label, fontsize=9, ha='center', va='center')

# Connections - User to use cases
user_connections = ['iniciar_sesion', 'ver_menu', 'ver_promociones', 'armar_carrito', 'comprar_y_ordenar']
for uc in user_connections:
    x, y, _ = use_cases[uc]
    ax.plot([1.15, x - 0.6], [4, y], 'k-', linewidth=1, alpha=0.7)

# Connections - Admin to use cases (all use cases)
for key, (x, y, _) in use_cases.items():
    if key in ['modify_stock', 'manage_orders', 'update_menu', 'generate_discounts']:
        ax.plot([8.85, x + 0.6], [4, y], 'k-', linewidth=1, alpha=0.7)

# Legend
legend_y = 1.2

plt.tight_layout()
plt.savefig('use_case_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Use Case Diagram generated successfully!")
print("\nUser capabilities:")
print("- Login, View/Edit Profile, View Content, Submit Request, View Reports")
print("\nAdministrator capabilities:")
print("- All User capabilities (inherited)")
print("- Manage Users, Manage Content, View Analytics, Configure System, Handle Requests, Generate Reports")