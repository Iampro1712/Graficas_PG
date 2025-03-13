import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x e y para la gráfica 3D en el intervalo [0, 2π]
x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)

# Definir la función f(x, y) = cos(x)
Z = np.cos(X)

# Crear la figura y el eje 3D con la orientación y estilo adecuado
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie con límites ajustados
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='black', alpha=0.8)

# Agregar título con formato de Mathematica
ax.set_title('In[6]:= Plot3D[Cos[x], {x, 0, 2π}, {y, 0, 2π},\n'
             '        Ticks → {{0, π/2, π, 3π/2, 2π}, {0, -1, 1}}];',
             fontsize=12, color="blue", fontname="monospace")

# Etiquetas de los ejes personalizadas
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

# Definir los ticks del eje X con múltiplos de π
x_ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
x_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']

# Definir los ticks del eje Y con múltiplos de π
y_ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
y_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']

# Definir los ticks del eje Z entre -1 y 1
z_ticks = [-1, 0, 1]
z_labels = ['-1', '0', '1']

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
