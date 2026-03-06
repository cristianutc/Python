import pandas as pd
from pathlib import Path

#ubicacion de los archivos json
scrip = Path(__file__).resolve().parent
carpeta = scrip / "Ejersicios/Archivos"
archivo_enero = carpeta / "ventas_enero.json"
archivo_febrero = carpeta / "ventas_febrero.json"
archivo_marzo = carpeta / "ventas_marzo.json"

#leemos el archivo json
df_enero = pd.read_json(archivo_enero)
print(df_enero)

df_febrero = pd.read_json(archivo_febrero)
print(df_febrero)

df_marzo = pd.read_json(archivo_marzo)
print(df_marzo)

#guardamos el archivo como csv
enero = df_enero.to_csv(carpeta / "ventas_enero.csv", index=False)
febrero = df_febrero.to_csv(carpeta / "ventas_febrero.csv", index=False)
marzo = df_marzo.to_csv(carpeta / "ventas_marzo.csv", index=False)

print(f"Archivo ventas_enero guardado exitosamente. {enero}")
print(f"Archivo ventas_febrero guardado exitosamente. {febrero}")
print(f"Archivo ventas_marzo guardado exitosamente. {marzo}")
