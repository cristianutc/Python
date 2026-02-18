"""Filtrado
El filtrado se usa para seleccionar filas que cumplen una condición."""
import pandas as pd
import numpy as np

# Ejemplo:

datos = {
    "Empleados": ["Ana", "Luis", "Pedro", "Ana", "Luis", "Pedro"],
    "Departamento": ["Ventas", "Ventas", "IT", "IT", "IT", "Ventas"],
    "Ventas": [1000, 1500, 2000, 1200, 1800, 1600],
    "Año": [2023, 2023, 2023, 2024, 2024, 2024]
}

df = pd.DataFrame(datos)

print(df, "\n")

# Filtrar por una condición
print("Devuelve solo las filas donde ventas son mayores a 1500: \n")
print(df[df["Ventas"] > 1500])

# AND (&)
print("\n Ventas mayores a 1500 y del año 2024:")
print(df[(df["Ventas"] > 1500) & (df["Año"] == 2024)])

# OR (|)
print("\n Filtra departamentos IT o Ventas mayor a 1800")
print(df[(df["Departamento"] == "IT") | (df["Ventas"] > 1800)])

# Filtrado por texto
print("\n Filtra los datos por texto")
print(df[df["Empleados"] == "Ana"])

# Filtrado usando isin()
print("\n Filtrado usando isin()")
print(df[df["Empleados"].isin(["Ana", "Pedro"])])
