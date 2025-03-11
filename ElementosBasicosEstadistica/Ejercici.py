import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Archivos/housing.csv')

media = df["median_house_value"].mean()
mediana = df["median_house_value"].median()
moda = df["median_house_value"].mode()[0]
rango = df["median_house_value"].max() - df["median_house_value"].min()  # Corregido el cálculo del rango
varianza = df["median_house_value"].var()
desviacion = df["median_house_value"].std()

tabla = pd.DataFrame({
    "Opción": ["Media", "Mediana", "Moda", "Rango", "Varianza", "Desviación Estándar"],
    "Valor": [media, mediana, moda, rango, varianza, desviacion]
})

print(tabla)

plt.figure(figsize=(12, 6))
sns.histplot(df["median_house_value"], bins=30, kde=True, color="blue", label="median_house_value", alpha=0.6)
sns.histplot(df["total_bedrooms"], bins=30, kde=True, color="red", label="total_bedrooms", alpha=0.6)
sns.histplot(df["population"], bins=30, kde=True, color="green", label="population", alpha=0.6)

plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Histograma de median_house_value comparado con total_bedrooms y population")
plt.legend()
plt.show()
