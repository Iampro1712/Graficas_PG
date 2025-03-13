import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir el rango de valores de x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Definir la función f(x, y) = sin(x) / (1 + cos(y)^2)
Z = np.sin(X) / (1 + np.cos(Y)**2)

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='black', alpha=0.8)

# Agregar título con formato de Mathematica
ax.set_title("In[1]:= Plot3D[Sin[x] / (1 + Cos[y]^2), {x, -5, 5}, {y, -5, 5}]", fontsize=12, color="blue", fontname="monospace")

# Etiquetas de los ejes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Configurar los ticks de los ejes
ax.set_xticks([-5, -2.5, 0, 2.5, 5])
ax.set_yticks([-5, -2.5, 0, 2.5, 5])
ax.set_zticks([-1, -0.5, 0, 0.5, 1])

# Mostrar la gráfica
plt.show()
