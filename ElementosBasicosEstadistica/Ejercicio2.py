import pandas as pd
import matplotlib.pyplot as plt


primero = pd.read_excel("Archivos/proyecto1.xlsx")
segundo = pd.read_excel("Archivos/Catalogo_sucursal.xlsx")

primero_combinado = pd.concat([primero,segundo])

primero_combinado.to_excel("yaunido.xlsx")

yael = pd.read_excel("Archivos/yaunido.xlsx") 

# 1. pa saber cuantas ventas totales hay
totales = yael["ventas_tot"].sum()
print('La suma de las ventas totales es:', totales)

# 2. deudores y no deudores
condeuda = yael[yael["adeudo_actual"] > 0].shape[0]
sindeuda = yael[yael["adeudo_actual"] == 0].shape[0]

porcentajedesiadeudo = (condeuda / len(yael)) * 100
porcentajedenoadeudo = (sindeuda / len(yael)) * 100

print('La cantidad de socios con adeudos:', condeuda, '(', round(porcentajedesiadeudo, 2), '%)')
print('La cantidad de socios sin adeudos:', sindeuda, '(', round(porcentajedenoadeudo, 2), '%)')

#3. grafica de ventas totales respecto al tiempo
plt.figure(figsize=(10, 5))
plt.bar(yael["B_mes"], yael["ventas_tot"], color='yellow')
plt.xlabel("Fecha")
plt.ylabel("Ventas totales")
plt.title("Ventas totales respecto al tiempo")
plt.xticks(rotation=45)
plt.show()

#4. desviación estándar de los pagos respecto al tiempo
std_pagos = yael.groupby("B_mes")["pagos_tot"].std()
plt.figure(figsize=(10, 5))
plt.plot(std_pagos.index, std_pagos.values, marker='o', linestyle='-', color='blue')
plt.xlabel("Fecha")
plt.ylabel("Desviación estándar de pagos")
plt.title("Desviación estándar de pagos respecto al tiempo")
plt.xticks(rotation=45)
plt.show()

# 5. deuda total de los clientes
totaldeuda = yael["adeudo_actual"].sum()
print('La deuda total de los clientes es:', totaldeuda)

# 6. porcentaje de utilidad del comercio respecto del adeudo 
utilidad = totales - totaldeuda
porcentaje_utilidad = (utilidad / totales) * 100 if totales > 0 else 0
print('El porcentaje de utilidad del comercio es:', round(porcentaje_utilidad, 2), '%')

# 7. grafico circular de ventas por sucursal
ventas_sucursal = yael.groupby("suc")[""].sum()
plt.figure(figsize=(8, 8))
plt.pie(ventas_sucursal, labels=ventas_sucursal.index, autopct='%1.1f%%', startangle=140)
plt.title("Ventas por sucursal")
plt.show()

# 8. grafico de cuales son las deudas totales respecto del margen de utilidad de cada sucursal
fig, ax = plt.subplots(figsize=(10, 5))
deudas_sucursal = yael.groupby("suc")["adeudo_actual"].sum()
ax.bar(deudas_sucursal.index, deudas_sucursal.values, color='orange', label='Deuda Total')
ax.set_xlabel("Sucursal")
ax.set_ylabel("Deuda total")
ax.set_title("Deudas totales por sucursal contra margen de utilidad")
plt.xticks(rotation=45)
plt.legend()
plt.show()