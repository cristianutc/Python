#leer multiples archivos
import pandas as pd
from pathlib import Path

#ubicacion de mis archivos
scrip = Path(__file__).resolve().parent
carpeta = scrip / "Ejersicios/Archivos"

#leemos los archivos
archivos_csv = carpeta.glob("ventas_*.csv")

lista_df = [pd.read_csv(archivo) for archivo in archivos_csv]

df_total = pd.concat(lista_df, ignore_index=True)

print(df_total)