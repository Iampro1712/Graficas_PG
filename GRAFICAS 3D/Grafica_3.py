import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Definir la función f(x, y) = sin(x) / (1 + cos(y)^2)
Z = np.sin(X) / (1 + np.cos(Y)**2)

# Crear la figura y el eje 3D con la orientación correcta
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie con límites ajustados en Z
ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='black', alpha=0.8)

# Agregar título con formato de Mathematica
ax.set_title('In[2]:= Plot3D[Sin[x] / (1 + Cos[y]^2), {x, -5, 5}, {y, -5, 5},\n'
             '        AxesLabel → {"Eje X", "Eje Y", "Eje Z"}];',
             fontsize=12, color="blue", fontname="monospace")

# Etiquetas de los ejes personalizadas
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

# Configurar los ticks de los ejes
ax.set_xticks([-5, -2.5, 0, 2.5, 5])
ax.set_yticks([-5, -2.5, 0, 2.5, 5])
ax.set_zticks([-1, -0.5, 0, 0.5, 1])

# Ajustar la vista para que coincida con la imagen original
ax.view_init(elev=30, azim=-40)  # Girado a la derecha correctamente

# Mostrar la gráfica
plt.show()
