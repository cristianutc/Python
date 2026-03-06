import pandas as pd
from pathlib import Path

# Ubicacion del script
script = Path(__file__).resolve().parent
carpeta = script / "Ejersicios/Archivos"

# Buscamos archivos
archivos_csv = list(carpeta.glob("ventas_*.csv"))

if not archivos_csv:
    print("No se econtraron archivos.")
else:
    lista_df = []

    for archivo in archivos_csv:
        try:
            df = pd.read_csv(archivo)
            df["origen_archivo"] = archivo.name # util para trazabilidad
            lista_df.append(df)
        except Exception as e:
            print(f"Error leyendo {archivo.name}: {e}")

    df_total = pd.concat(lista_df, ignore_index=True)

    print(df_total.head())
    print(f"\nTotal filas: {df_total.shape[0]}")
    
    # Verificamos la estructura:
    print(df_total.info())

    # Revisar nulos:
    print("\n", df_total.isnull().sum())

    # Verificamos duplicados de filas
    print("\n", df_total.duplicated().sum())

    # Vereficamos duplicados de solo una columna
    print(df_total.duplicated(subset=["origen_archivo"]).sum())
    print("\n", df_total)

