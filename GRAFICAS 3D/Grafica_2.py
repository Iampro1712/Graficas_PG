import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x e y para la gráfica 3D
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(-2*np.pi, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)

# Definir la función f(x, y) = sin(x)
Z = np.sin(X)

# Crear la figura y el eje 3D con la orientación y estilo adecuado
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie con límites ajustados
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='black', alpha=0.8)

# Agregar título con formato de Mathematica
ax.set_title('In[2]:= Plot3D[Sin[x], {x, -2π, 2π}, {y, -2π, 2π},\n'
             '        AxesLabel → {"Eje X", "Eje Y", "Eje Z"}];',
             fontsize=12, color="blue", fontname="monospace")

# Etiquetas de los ejes personalizadas
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

# Configurar los ticks de los ejes con múltiplos de π
x_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
x_labels = [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
y_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
y_labels = [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
z_ticks = [-1, -0.5, 0, 0.5, 1]
z_labels = ['-1', '-0.5', '0', '0.5', '1']

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)
ax.set_zticks(z_ticks)
ax.set_zticklabels(z_labels)

# Ajustar la vista para que coincida con el estilo de las otras gráficas 3D
ax.view_init(elev=30, azim=-40)  # Ajuste del ángulo de visualización

# Mostrar la gráfica
plt.show()
