import pandas as pd
import os
from pathlib import Path 

ruta_del_archivo = Path(__file__).resolve().parent # ruta de nuestro archivo script
ruta_de_carpeta = ruta_del_archivo / "Ejersicios/Archivos"
ruta_del_archivo_csv = ruta_de_carpeta / "ventas.csv"

df = pd.read_csv(ruta_del_archivo_csv) # leemos el archivo csv

print(df.shape) # tamaño total
print(df.info()) # muestra estructura, tipos y nulos
print(df) # imprimimos los datos del archivo csv

# podemos aser un filtro basico
print(df[(df["Mes"] == "Febrero") & (df["Ventas"] > 200)])
