import pandas as pd
import os
from pathlib import Path

ruta_del_archivo = Path(__file__).resolve().parent
carpeta = ruta_del_archivo / "Ejersicios/Archivos"
archivo = carpeta / "ventas.json"

df = pd.read_json(archivo)
print(df.head()) # primeras 5 filas
print(df.tail()) # ultimas 5 filas 
print(df.info()) # muestra estructura, tipos y nulos
print(df.shape) # tamaño total

pd.set_option("display.max_rows", None) # Cambiar configuracion para mostrar todo
print(df)