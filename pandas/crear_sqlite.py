import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Ejersicios/Archivos"

csv_file = DATA_DIR / "ventas.csv"
db_file = DATA_DIR / "ventas.db"

df = pd.read_csv(csv_file)

conn = sqlite3.connect(db_file) # Creamos la conexion a la base de datos

#Esto crea un archivo SQLite vacío (ventas.db) si no existe.
# Si ya existe, se conecta a él.
df.to_sql("ventas", conn, if_exists="replace", index=False)
# to_sql() toma todo el DataFrame y lo copia dentro de la base.
# "ventas" -> nombre de la tabla que se creará dentro de SQLite.
# if_exists="replace" -> si la tabla ya existía, la reemplaza.
# index=False -> no guarda la columna del índice de pandas en SQLite.

conn.close()
print("Base de datos creada correctamente.")
