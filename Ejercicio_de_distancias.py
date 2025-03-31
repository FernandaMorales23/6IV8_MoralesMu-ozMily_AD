#Calcularemos las distancias entre todos los pares de puntos y determinaremos cuáles están más aljados entre sí y cuáles están más cercanos utilizando las distancias Euclidiana, Manhattan y Chebyshev

import numpy as np 
import pandas as pd
from scipy.spatial import distance

#definimos las coordenadas de las puntos 
puntos = {
    'punto A':(2,3),
    'punto B':(5,4),
    'punto C':(1,1),
    'punto D':(6,7),
    'punto E':(3,5),
    'punto F':(8,2),
    'punto G':(4,6),
    'punto H':(2,1)
}

#Convertir los puntos a Dataframe
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X','Y']
print ("Coordenadas de los puntos")
print(df_puntos)

def calcular_distancias(puntos):
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    #Cálculo de las distancias
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i!=j: #No calcula la distancia del mismo punto
                #Distancia Euclidiana
                distancias.loc[i,j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
    return distancias
distancias = calcular_distancias(puntos)
valor_maximo = distancias.values.max()
(punto1,punto2) = distancias.stack().idxmax()
print("Tabla de Distancias")
print(distancias)
print("Distancia máxima", valor_maximo)
print("Entre el punto", punto1, "; y el punto", punto2)

#otra manera
max_value = distancias.max().max()
#obtener la columna que contiene el valor máximo
col_max = distancias.max().idxmax()

#obtener el indice (fila) que contiene el valor máximo
id_max = distancias[col_max].idxmax()

print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Índice: {id_max}")