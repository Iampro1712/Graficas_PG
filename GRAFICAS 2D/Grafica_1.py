import numpy as np
import matplotlib.pyplot as plt

"""
Integrantes:
María Esther Espinoza López. 
María Natasha Gutierrez Espinoza.
Eduard Antonio Bejarano Carrion.
"""

# Generar datos
x = np.linspace(-4, 4, 500)  # 500 puntos entre -4 y 4
y = x ** 2

# Configurar la gráfica
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
plt.plot(x, y, color="blue", linewidth=2)
plt.title("Gráfica de $y = x^2$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.axhline(0, color="black", linewidth=0.5)  # Eje x
plt.axvline(0, color="black", linewidth=0.5)  # Eje y
plt.xlim(-4, 4)
plt.ylim(0, 16)

# Mostrar gráfica
plt.show()