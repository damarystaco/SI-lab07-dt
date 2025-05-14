#Crear un Grafico lineal 02
import numpy as np
import matplotlib.pyplot as plt
#Definir datos
x1=[3, 4, 5, 6 ]
y1=[5, 6, 3, 4 ]
x2=[2, 5, 8 ]
y2=[3, 4, 3 ]

plt.bar(x1, y1, label= 'Linea 1', linewidth=4, color='red')
plt.bar(x2, y2, label= 'Linea 2', linewidth=4, color='green')

plt.title('Diagrama barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

plt.legend()
plt.grid()
plt.show()