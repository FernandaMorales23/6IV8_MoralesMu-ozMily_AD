import pandas as pd
import matplotlib.pyplot as plt


primero = pd.read_excel("Archivos/proyecto1.xlsx")
segundo = pd.read_excel("Archivos/Catalogo_sucursal.xlsx")

primero_combinado = pd.concat([primero,segundo])

primero_combinado.to_excel("yaunido.xlsx")

yael = pd.read_excel("Archivos/yaunido.xlsx") 

#1.pa conocer las ventas totales del comercio 
print('Las ventas totales son:')
print(yael["ventas_tot"])

#2.socios con adeudo y sin
deudores = yael[yael['B_adeudo'] == 'Con adeudo']
print('Las personas con adeudo son:')
print(deudores)

no_deudores = yael[yael['B_adeudo'] == 'Sin aduedo']
print('Las personas sin adeudo son:')
print(no_deudores)

#3.Grafiquita de chava
plt.scatter(yael['ventas_tot'][:10], yael['B_mes'][:10])
plt.xlabel("Ventas totales")
plt.ylabel("Tiempo")

plt.title("Grafico de dispersion de ventas totales por tiempo")
plt.show()