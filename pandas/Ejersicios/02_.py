import pandas as pd

datos = {
    "Vendedor": ["Ana", "Luis", "Pedro", "Sofia", "Ana", "Luis", "Pedro", "Sofia", "Ana", "Luis"],
    "Ciudad": ["CDMX", "Madrid", "Lima", "CDMX", "Lima", "Madrid", "Lima", "CDMX", "CDMX", "Madrid"],
    "Ventas": [120, 200, 300, 150, 180, 250, 400, 100, 220, 270],
     "Mes": ["Enero", "Enero", "Enero", "Enero", "Febrero", "Febrero", "Febrero", "Febrero", "Marzo", "Marzo"]
}

df = pd.DataFrame(datos)
print("\t Tabla de los Datos")
print(df)

# Ejercicio 1 – Series y filtrado simple
# Crea una Serie que solo contenga las ventas mayores a 200 y muestra los índices y valores.

print(df["Ventas"][df["Ventas"] > 200])

# Ejercicio 2 – Filtrado con DataFrame
# Filtra el DataFrame para obtener todas las filas donde:
# La ciudad sea "CDMX" Y las ventas sean mayores a 150

print(df[(df["Ciudad"] == "CDMX") & (df["Ventas"] > 150)])

# Ejercicio 3 – sort_values
# Ordena el DataFrame primero por Mes ascendente y luego por Ventas descendente.

print(df.sort_values(by=["Mes", "Ventas"], ascending=[True, False]))

# Ejercicio 4 – groupby + suma
# Encuentra el total de ventas por cada Vendedor y Ciudad. Luego muestra quién tiene la mayor venta total y su ciudad.

total_ventas = df.groupby(["Vendedor", "Ciudad"])["Ventas"].sum().reset_index()

# Encontrar el mayor
mayor = total_ventas.loc[total_ventas["Ventas"].idxmax()]

print(total_ventas)
print("\nVendedor con mayor venta total:")
print(mayor)
