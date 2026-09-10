import matplotlib.pyplot as plt

    
def DibujaCurva(ax,x,y):
    
    # Graficar puntos originales y la línea de ajuste
    ax.plot(x, y, label='Ajuste gráfica')
    ax.legend()
    ax.show()


def agregar_curva(ax, x, y, etiqueta, color='blue', estilo='-'):
    """
    Añade una nueva línea a un gráfico (Axes) existente.
    """
    ax.plot(x, y, label=etiqueta, color=color, linestyle=estilo)
    ax.legend() # Actualiza la leyenda automáticamente

