# Traza una recta tangente a una función ejemplo en un punto determinado:

import matplotlib.pyplot as plt
import numpy as np

def funcion_ejemplo(x):
    return x ** 2

def derivada_ejemplo(x):
    return 2 * x

# Punto en el que se trazará la recta tangente
x_punto = 2
y_punto = funcion_ejemplo(x_punto)

# Rango de valores x alrededor del punto
rango_x = np.linspace(x_punto - 1, x_punto + 1, 100)

# Función de la recta tangente
recta_tangente = derivada_ejemplo(x_punto) * (rango_x - x_punto) + y_punto

# Gráfica de la función original
plt.plot(rango_x, funcion_ejemplo(rango_x), label='Función')

# Gráfica de la recta tangente
plt.plot(rango_x, recta_tangente, label='Recta Tangente')

# Punto de interés
plt.scatter(x_punto, y_punto, color='red', label='Punto')

# Títulos y etiquetas de los ejes
plt.title('Recta Tangente a un Punto')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Leyenda
plt.legend()

# Mostrar la gráfica
plt.show()