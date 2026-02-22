import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Ejersicios" / "Archivos"

db_file = DATA_DIR / "ventas.db"

conn = sqlite3.connect(db_file)

df = pd.read_sql("SELECT * FROM Ventas", conn )

conn.close()

print(df)
print(df.head())
print(df.info())