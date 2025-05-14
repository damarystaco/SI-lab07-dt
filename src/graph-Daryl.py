import matplotlib.pyplot as plt
#definir datos
a = [22,55,62,45,21,22,34,42,42,42,102,95,85,55,110,120,70,65,55,111,115,80,75,54,44,43,42,40]
bins = [0,10,20,30,40,50,60,70,80,90,100]
#aplicar configuraciones de caracterisitica del grafico

plt.hist(a, bins, histtype= 'bar', rwidth = 0.8, color = 'blue')

# Definiendo el titulo y nombre de los ejes
plt.title('Histogramas')
plt.ylabel('eje Y')
plt.xlabel('eje X')

#Mostrar leyenda, cuadricula y figura grafica(grafica)
plt.show()