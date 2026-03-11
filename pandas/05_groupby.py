import pandas as pd

# groupby()
# groupby() se usa para agrupar datos y aplicar una función agregada.
# Es como hacer tablas dinámicas.
# Ejemplo:

datos = {
    "Empleados": ["Ana", "Luis", "Pedro", "Ana", "Luis", "Pedro"],
    "Departamento": ["Ventas", "Ventas", "IT", "IT", "IT", "Ventas"],
    "Ventas": [1000, 1500, 2000, 1200, 1800, 1600],
    "Año": [2023, 2023, 2023, 2024, 2024, 2024]
}

df = pd.DataFrame(datos)

print(df, "\n")

# Agrupar por una columna
print("\n Total de ventas por departamento")
print(df.groupby("Departamento")["Ventas"].sum())

# Multiples agregaciones
print("\n Agregamos varias filtros")
print(df.groupby("Departamento")["Ventas"].agg(["sum", "mean", "max", "min", "count"]))

print("\n Agrupar por varias columnas")
print(df.groupby(["Departamento", "Año"])["Ventas"].sum())

print("\n Resetear indice despues de groupby")
print(df.groupby("Departamento")["Ventas"].sum().reset_index())
