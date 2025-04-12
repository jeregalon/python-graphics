import matplotlib.pyplot as plt
import numpy as np

class Graficadora:
    def __init__(self):
        self.fig, self.ax = plt.subplots(facecolor='white')

        # límites de la gráfica
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-10, 10)

    def graficar_funcion(self):
        x = np.linspace(-5, 5, 1000)

        y1 = 3 * x + 5
        # y2 = 2 + 0 * x
        # y3 = -4 * x

        # Rejilla y estética
        self.ax.grid(True, linestyle='--', alpha=0.5)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.tick_params(width=1.5, labelsize=12)

        # Etiquetas para los ejes
        self.ax.text(5.3, -0.8, "x", fontsize=16)
        self.ax.text(0.3, 10.2, "y", fontsize=16)

        # Dibujar las funciones y guardar las referencias
        line1, = self.ax.plot(x, y1, linewidth=2.5, zorder=1)
        # line2, = self.ax.plot(x, y2, linewidth=2.5, zorder=1)
        # line3, = self.ax.plot(x, y3, linewidth=2.5, zorder=1)

        # Texto sobre las líneas, más grande y rotado según la pendiente
        # self.ax.text(2, 3 * 1.5 + 0.5, "m > 0", fontsize=18, color=line1.get_color(), rotation=45)
        # self.ax.text(-4.5, 2.3, "m = 0", fontsize=18, color=line2.get_color())
        # self.ax.text(0.9, -4 * 1.5 + 0.5, "m < 0", fontsize=18, color=line3.get_color(), rotation=-45)

        # Mostrar y guardar
        plt.savefig('grafica_final.png', format='png')
        plt.show()
