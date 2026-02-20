import pandas as pd

datos = {
    "Vendedor": ["Ana", "Luis", "Ana", "Pedro", "Luis", "Ana"],
    "Ciudad": ["CDMX", "Madrid", "CDMX", "Lima", "Madrid", "Lima"],
    "Ventas": [100, 200, 150, 300, 250, 400],
    "Mes": ["Enero", "Enero", "Febrero", "Enero", "Febrero", "Febrero"]
}

tabla = pd.DataFrame(datos)
print("\tTabla de los Datos")
print(tabla)

#Retos
# 1 Filtro basico
# Obten solo las ventas mayores a 200.
print("\t Ventas mayores a 200")
print(tabla[tabla["Ventas"] > 200])

# 2 Filtro doble
# Obtén las ventas de Ana en Febrero.
print("\t Ventas de Ana en Febrero")
print(tabla[(tabla["Mes"] == "Febrero") & (tabla["Vendedor"] == "Ana")])

# 3 Groupby simple
# Calcula el total de ventas por vendedor.
print("\t Total de Ventas por Vendedor")
print(tabla.groupby("Vendedor")["Ventas"].sum())

#Groupby más avanzado
# Calcula el promedio de ventas por ciudad.
print("\t Ventas promedio por ciudad")
print(tabla.groupby("Ciudad")["Ventas"].agg(["sum","mean", "count"]))

# 5 Ordenamiento
# Ordena el DataFrame por ventas de mayor a menor.
print("\t Ventas de mayor a menor")
print(tabla.sort_values("Ventas", ascending=False))

# 6 Ordenamiento
# Ordena el DataFrame por ventas de menor a mayor.
print("\t Ventas de menor a mayor")
print(tabla.sort_values("Ventas", ascending=True))

# ¿Cómo obtendrías el vendedor con MAYOR total de ventas?

total = tabla.groupby(["Vendedor", "Ciudad"])["Ventas"] \
    .sum() \
    .reset_index() 

mayor_vendedor = total.loc[total["Ventas"].idxmax()]

print("\t El vendedor con mayor ventas")
print(mayor_vendedor)

print(tabla.groupby("Vendedor")["Ventas"].sum().idxmax())