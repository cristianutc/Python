import pandas as pd
from pathlib import Path

archivo_script = Path(__file__).resolve().parent

ruta_carpeta = archivo_script / "Archivos"

ruta_archivo = ruta_carpeta / "AAPL_Stock_Price_Dataset.csv"

df = pd.read_csv(ruta_archivo)

print(pd.DataFrame(df))

# ¿Cuál fue el día con mayor volumen?
print(df.loc[df["Volume"].idxmax()])

# ¿Cuál fue el mayor rendimiento positivo?
print(df["Daily_Return"].max())

# Calcular media móvil de 30 días
df["MA_30"] = df["Close"].rolling(30).mean()

print(df["MA_30"])


