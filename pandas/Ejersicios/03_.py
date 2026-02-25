import pandas as pd
from pathlib import Path

# Definir rutas
ruta_del_archivo = Path(__file__).resolve().parent
ruta_de_carpeta = ruta_del_archivo / "Archivos"
ruta_del_archivo_csv = ruta_de_carpeta / "datos.csv"

# Leer CSV
df = pd.read_csv(ruta_del_archivo_csv)

# ----- METADATOS -----
print("----- METADATOS -----")
print(df.info())

# ----- CALIDAD DE DATOS -----
print("\n----- CALIDAD DE DATOS -----")
# Filas con datos faltantes
print(df[df.isnull().any(axis=1)])
# Filas con nombres vacíos
print(df[df["Nombre"].astype(str).str.strip() == ""])

# ----- PRIVACIDAD -----
def ocultar_email(email):
    if isinstance(email, str) and "@" in email:
        partes = email.split("@")
        return email[0] + "***@" + partes[1]
    else:
        return "Sin email"

df["Email_oculto"] = df["Email"].apply(ocultar_email)
print("\n----- DATOS CON PRIVACIDAD -----")
print(df[["Nombre", "Email_oculto"]])

# ----- WORKFLOW DE DATOS -----
print("\n----- WORKFLOW DE DATOS -----")
# Paso 1: Limpiar filas con valores faltantes
df_clean = df.dropna()
# Paso 2: Validar nombres no vacíos
df_clean = df_clean[df_clean["Nombre"].astype(str).str.strip() != ""]
# Paso 3: Mantener solo columnas necesarias y proteger emails
df_clean_protegido = df_clean.copy()
df_clean_protegido["Email"] = df_clean_protegido["Email_oculto"]
df_clean_protegido = df_clean_protegido.drop(columns=["Email_oculto"])  # opcional

# Guardar CSV protegido
df_clean_protegido.to_csv(ruta_de_carpeta / "clientes_limpios_protegido.csv", index=False)
print("Datos limpios y protegidos guardados en clientes_limpios_protegido.csv")


"""astype(str).str.strip() -> evita que nombres con solo espacios se consideren válidos.
isinstance(email, str) -> evita errores si la celda está vacía o no es texto.
Guardamos el CSV limpio en la misma carpeta del script, usando Path, así es más ordenado y portátil.
Cambié el valor de email vacío a "Sin email" para que sea más explícito."""