import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Archivos/housing.csv')

#mostrar las primeras 5 filas
print(df.head())

#mostrar las ultimas 5 filas
print (df.tail())

#mostrar una fila en especifico
print(df.iloc[7])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#obtener media de la columna total _rooms
mediadecuarto = df["total_rooms"].mean()
print('La media total es:', mediadecuarto)

#mediana
medianadecuarto = df['median_house_value'].median()
print('La mediana de la columna valor mediana de la casa es:',mediadecuarto)

#la suma de popular
salariototal = df['population'].sum()
print('El salario total es de:', salariototal)

#para poder filtrar
vamoshacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamoshacerunfiltro)

#vamos hacer un grafico de dispersion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
#nombramos los ejes
plt.xlabel("Proximidad")
plt.ylabel("Precio")

plt.title("Grafico de dispersion de proximidad al oceano vs precio")
plt.show()