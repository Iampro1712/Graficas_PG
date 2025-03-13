import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x para el intervalo [0, 2π]
x = np.linspace(0, 2*np.pi, 400)
y = np.cos(x)

# Crear la gráfica con el código similar al formato de Mathematica
plt.figure(figsize=(8,5))
plt.plot(x, y, label="Cos[x]", color='black')

# Agregar título con el formato de Mathematica
plt.text(0, 1.2, 'In[6]:= Plot[Cos[x], {x, 0, 2π},\n'
                 '        Ticks → {{0, π/2, π, 3π/2, 2π}, {0, -1, 1}}];', 
         fontsize=12, color="blue", family="monospace")

# Definir los ticks del eje X e Y para que se vean correctamente
x_ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
x_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
y_ticks = [-1, 0, 1]
y_labels = ['-1', '0', '1']

plt.xticks(x_ticks, x_labels)  # Configurar ticks del eje x
plt.yticks(y_ticks, y_labels)  # Configurar ticks del eje y

# Agregar ejes en (0,0)
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

# Mostrar la gráfica
plt.show()
