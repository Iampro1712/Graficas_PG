import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x y la función coseno
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = np.cos(x)

# Crear la gráfica con el código similar al formato de Mathematica
plt.figure(figsize=(8,5))
plt.plot(x, y, label="Cos[x]", color='blue')

# Agregar título con el formato de Mathematica
plt.text(-2*np.pi, 1.2, 'In[3]:= Plot[Cos[x], {x, -2π, 2π}, AxesLabel → {"X", "Y"}];', 
         fontsize=12, color="blue", family="monospace")

# Agregar etiquetas de los ejes
plt.xlabel("X")
plt.ylabel("Y")

# Agregar ejes en (0,0)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Agregar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
