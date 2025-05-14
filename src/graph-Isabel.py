

##CREAR UN GRAFICO HISTOGRAMA
import matplotlib.pyplot as plt
# Definir datos
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10,55,80,32,40,]
x2 = [0.75,1.75,2.75,3.75,4.75]
y2 = [42,26,10,29,66]

#Aplicar configuracion de caracteristicas del grafico
plt.scatter(x1,y1, label = 'Dato 1', color = 'pink')
plt.scatter(x2,y2, label = 'Dato 2', color = 'purple')

#Definiendo el titulo y los nombres de los ejes
plt.title('Graficos de dispersion')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda y figura(Grafica)
plt.legend()
plt.show()

