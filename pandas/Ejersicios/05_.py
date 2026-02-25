from pathlib import Path
import pandas as pd

#---------------------------
#--- Preparación inicial ---
#---------------------------

script = Path(__file__).resolve().parent
carpeta = script / "Archivos"
archivo_csv = carpeta / "dataset.csv"

df = pd.read_csv(archivo_csv, encoding="utf-8")

#print(df.info())
#print(df)

#pd.set_option('display.max_columns', None)  # muestra todas las columnas
#print(df.head())  # solo las primeras 5 filas

# Ver nombres de todas las columnas
#print(df.columns)

# Ver primeras 5 filas completas
#print(df.head())

# Ver últimas 5 filas
#print(df.tail())

# Revisar cuántos valores faltan por columna (nulos)
#print(df.isnull().sum())

#--------------------------
#--- Exploración básica ---
#--------------------------

#Mostrar solo los títulos de las primeras 10 recetas:
#print(df["title"].head(10))

#Contar cuantas recetas hay:
#print(f"Total de recetas: {len(df)}")

#Ver cuantos titulos faltan:
#print("Total faltantes de titulos: ", df["title"].isnull().sum())
#print("Total faltantes de url: ", df["url"].isnull().sum())
#print("Total faltantes de ingredientes: ", df["ingredients"].isnull().sum())
#print("Total faltantes de intrucciones: ", df["steps"].isnull().sum())
#print("Total faltantes de uuid: ", df["uuid"].isnull().sum())

#Rellenar titulos vacios con "Sin titulo"
#df["title"] = df["title"].fillna("Sin titulo")
#df["ingredients"] = df["ingredients"].fillna("Sin ingredinte")
#df["uuid"] = df["uuid"].fillna("Sin uuid")
#print(df.isnull().sum())

#---------------------------
#--- Filtrado de recetas ---
#---------------------------

#Buscar recetas que contengan “pollo” en los ingredientes:
#pollo = df[df["ingredients"].str.contains("pollo", case=False, na=False)]
#print(pollo[["title", "ingredients"]].head())

#Buscar recetas que contengan “chocolate” y “huevo”:
#choco_huevo = df[df["ingredients"].str.contains("chocolate", case=False, na=False) &
#                 df["ingredients"].str.contains("huevo", case=False, na=False)]
#print(choco_huevo[["title", "ingredients"]].head())

#-----------------------------
#--- Conteo y estadísticas ---
#-----------------------------

#Contar cuántas recetas tienen “queso”:
#ueso_count = df["ingredients"].str.contains("queso", case=False, na=False).sum()
#print(f"Recetas con queso: {queso_count}")

#Contar las recetas por longitud de pasos:
# Crear columna con longitud de pasos
#df["len_steps"] = df["steps"].str.len()
#Ver las 5 recetas con pasos mas largos
#print(df.sort_values("len_steps", ascending=False)[["title", "len_steps"]].head())

#----------------------------------------
#--- Limpieza y selección de columnas ---
#----------------------------------------

#Crear un DataFrame con solo title e ingredients:
#df_simple = df[["title", "ingredients"]]
#print(df_simple.head())

#Eliminar filas con ingredients vacíos:
#df_simple = df.dropna(subset=["ingredients"])

#Contar cuántas recetas tienen la palabra “sopa” en el título
sopa_count = df["title"].str.contains("sopa", case=False, na=False).sum()
print(f"Recetas de sopa: {sopa_count}")

"""Ejercicios extra (intermedio)

Crear un DataFrame con recetas que tengan menos de 5 ingredientes

Crear un DataFrame de recetas que contengan “arroz” o “pollo”

Ordenar recetas alfabéticamente por título

Contar cuántas recetas tienen la palabra “sopa” en el título"""