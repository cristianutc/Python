import pandas as pd

#sort_values()
#Sirve para ordenar filas.


datos = {
    "Empleados": ["Ana", "Luis", "Pedro", "Ana", "Luis", "Pedro"],
    "Departamento": ["Ventas", "Ventas", "IT", "IT", "IT", "Ventas"],
    "Ventas": [1000, 1500, 2000, 1200, 1800, 1600],
    "Año": [2023, 2023, 2023, 2024, 2024, 2024]
}

df = pd.DataFrame(datos)

print(df, "\n")

print("\n Ordenar ascendente (por defecto)")
print(df.sort_values("Ventas"))

print("\n Ordenar descendente")
print(df.sort_values("Ventas", ascending=False))

print("\n Ordenar por múltiples columnas")
print(df.sort_values(["Departamento", "Ventas"], ascending=[True, False]))
# Primero ordena por departamento
# Dentro de cada departamento ordena por ventas descendente

# Combinando Todo (como en la vida real)
# Ejemplo típico de análisis:
# “Quiero ver las ventas totales por departamento en 2024, ordenadas de mayor a menor”
v_totales = df[df["Año"] == 2024] \
    .groupby("Departamento")["Ventas"] \
    .sum() \
    .reset_index() \
    .sort_values("Ventas", ascending=False)

print(v_totales)

#Flujo mental:
# Filtrar año 2024
# Agrupar por departamento
# Sumar ventas
# Ordenar de mayor a menor