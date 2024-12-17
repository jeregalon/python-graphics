# Crea una gráfica de una función

import matplotlib.pyplot as plt
import numpy as np

class Graficadora:
    def __init__(self):
        self.fig, self.ax = plt.subplots(facecolor='white')

        # límites de la gráfica
        plt.ylim(-3, 3)
        plt.xlim(-50, 50)

    def graficar_funcion(self):

        # Datos de ejemplo
        x1 = np.linspace(-50, 50, 1000)
        y1 = (x1**2-1)/(x1**2+1)

        # x2 = np.linspace(3.0001, 6, 100)
        # y2 = 2*x2 / (x2-3)

        # Estilo de la gráfica
        self.ax.plot(x1, y1, linewidth=2.5, label="f(x)", zorder=1)
        # self.ax.plot(x2, y2, color="blue", linewidth=2.5, zorder=1)
        # plt.scatter(-6, 2, color='white', edgecolors="blue", linewidth=3, s=100, zorder=2)
        
        
        # Leyenda
        self.ax.legend(fontsize="xx-large", loc='upper left', facecolor='black', edgecolor='white', labelcolor='white')

        # Ajustar grosor de ejes y ticks
        self.ax.spines['top'].set_linewidth(1.5)
        self.ax.spines['right'].set_linewidth(1.5)
        self.ax.spines['bottom'].set_linewidth(1.5)
        self.ax.spines['left'].set_linewidth(1.5)
        self.ax.tick_params(width=1.5)

        # Ajustar tamaño de fuente de los ticks
        self.ax.tick_params(axis='x', labelsize=16)
        self.ax.tick_params(axis='y', labelsize=16)
        
        # Agregar rejillas
        self.ax.grid(True)

        # Asegurar que los números de los ejes estén por encima de las rejillas
        self.ax.tick_params(axis='both', which='both')

        # Guardar la gráfica como archivo PNG
        plt.savefig('grafica15.png', format='png')

        # Mostrar la gráfica
        plt.show()