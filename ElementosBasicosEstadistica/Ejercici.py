import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Archivos/housing.csv')

media = df["median_house_value"].mean()
mediana = df["median_house_value"].median()
moda = df["median_house_value"].mode()[0] 
rango = media - mediana
varianza = df["median_house_value"].var()
desviacion = df["median_house_value"].std()

tabla = pd.DataFrame({
    "Opción": ["Media", "Mediana", "Moda", "Rango", "Varianza", "Desviación Estándar"],
    "Valor": [media, mediana, moda, rango, varianza, desviacion]
})

print(tabla)

plt.scatter(df['median_house_value'][:10], df['total_bedrooms'][:10])
plt.xlabel("Costo promedio")
plt.ylabel("Cuartos")

plt.title("Grafico de dispersion de costo pormedios y cuartos")
plt.show()

plt.scatter(df['median_house_value'][:10], df['population'][:10])
plt.xlabel("Costo promedio")
plt.ylabel("Popularidad")

plt.title("Grafico de dispersion de costo pormedios y popularidad")
plt.show()