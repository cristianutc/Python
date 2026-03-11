import pandas as pd

datos = {
    "Empleados": [
        "Ana", "Luis", "Pedro", "Ana", "Luis",
        "Pedro", "Maria", "Juan", "Ana", "Luis",
        "Carlos", "Maria", "Pedro", "Ana", "Luis",
        "Juan", "Carlos", "Maria", "Pedro", "Ana"
    ],
    
    "Departamento": [
        "Ventas", "Ventas", "IT", "IT", "IT",
        "Ventas", "Marketing", "Ventas", "IT", None,
        "Marketing", "IT", "IT", "Ventas", "Ventas",
        "Marketing", None, "Marketing", "IT", "Ventas"
    ],
    
    "Ventas": [
        1000, 1500, 2000, 1200, 1800,
        1600, 1300, None, 1100, 1700,
        1400, 1250, None, 1350, 1550,
        1650, 1450, None, 2100, 1900
    ],
    
    "Año": [
        2023, 2023, 2023, 2024, 2024,
        2024, 2023, 2023, 2024, 2024,
        2023, 2024, 2023, None, 2024,
        2023, 2024, 2024, 2023, None
    ]
}

df = pd.DataFrame(datos)
print(df.isnull().sum())

print(df.duplicated().sum())

print(df.duplicated(subset=["Departamento"]).sum())
print(df[df.isnull().any(axis=1)])
df_limpio = df.dropna()
print(df_limpio)
df_limpio2 = df.dropna(subset=["Ventas"])
print(df_limpio2)

df["Ventas"] = df["Ventas"].fillna(600)
print(df)