import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x y la función coseno
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = np.cos(x)

# Crear la gráfica con el código similar al formato de Mathematica
plt.figure(figsize=(8,5))
plt.plot(x, y, label="Cos[x]", color='black')

# Agregar título con el formato de Mathematica
plt.text(-2*np.pi, 1.2, 'In[4]:= Plot[Cos[x], {x, -2π, 2π}, Ticks → None];', 
         fontsize=12, color="blue", family="monospace")

# Definir los ticks del eje X e Y para que se vean correctamente
x_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
x_labels = [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
y_ticks = [-1, -0.5, 0, 0.5, 1]
y_labels = ['-1', '-0.5', '0', '0.5', '1']

plt.xticks(x_ticks, x_labels)  # Configurar ticks del eje x
plt.yticks(y_ticks, y_labels)  # Configurar ticks del eje y

# Agregar ejes en (0,0)
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

# Mostrar la gráfica
plt.show()

