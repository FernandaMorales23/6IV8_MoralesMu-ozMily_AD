import numpy as np
import matplotlib.pyplot as plt

#vamos a crear una semilla random para reproductilbilidad
np.random.seed(0)

#vamos a buscar los parametros para una distribucion
#meida
media = 0
#desviaciones estándar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#el numeri de muestras para ánalisis
n_muestras = 1000

#vamos a generar los datos de las distribuciones normales
data1 = np.random.normal(media,sigma1, n_muestras)
data2 = np.random.normal(media,sigma2, n_muestras)
data3 = np.random.normal(media,sigma3, n_muestras)

#vamos a configurar la grafica
plt.figure(figsize=(10,6))

#el histograma sirve para ver la frecuencia de los datos
#vamos a cargar las frecuencias a partir de una grafica de histograma
plt.hist(data1, bins=30, color='pink', density=True, label='Desviación estándar = 1')

plt.hist(data2, bins=30, color='yellow', density=True, label='Desviación estándar = 2')

plt.hist(data3, bins=30, color='orange', density=True, label='Desviación estándar = 3')

#a graficarr
plt.title('Comparación de distribuciones normales con una semilla en random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color = 'black', linewidth=0.5, ls='--')
plt.axvline(0, color = 'black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

plt.show()