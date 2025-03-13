import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores de x
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = np.sin(x)

# Crear la gráfica
plt.figure(figsize=(8,5))
plt.plot(x, y, label="sin(x)")

# Agregar título y etiquetas
plt.title("FUNCIÓN SENO")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Agregar ejes en (0,0)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Agregar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
