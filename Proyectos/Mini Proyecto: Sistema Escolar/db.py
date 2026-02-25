import sqlite3
from contextlib import contextmanager
from pathlib import Path
import os


#----------------------------
# RUTA A LA BASE DE DATOS
#----------------------------
# obtener ruta de la base de datos

ruta_script = Path(__file__).resolve().parent
ruta_db = ruta_script / "db"
archivo_db = ruta_db / "escuela.db"

#----------------------------
# Conexion a la Base de Datos
#----------------------------
# Creando el context manager usando un decorador
@contextmanager
def open_connect():
    con = sqlite3.connect(archivo_db)
    try:
        yield con # Proporcionamos la conexión para su uso
    finally:
        con.close() # Cerramos la conexión cuando se termina el bloque

#-----------------------------
# Funcion para crear tablas
#-----------------------------
def crear_tablas():
    with open_connect() as con:
        cur = con.cursor()

        # CREATE TABLE con IF NOT EXISTS evita errores si ya existen
        cur.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_curso TEXT,
            creditos INTEGER
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS inscripciones (
            id_estudiante INTEGER,
            id_curso INTEGER,
            fecha TEXT,
            FOREIGN KEY(id_estudiante) REFERENCES estudiantes(id_estudiante),
            FOREIGN KEY(id_curso) REFERENCES cursos(id_curso)
        )
        """)

        con.commit()  # Guardar los cambios
        print("Tablas creadas (si no existían).")

#-----------------------------
# Logica principal
#-----------------------------
if not os.path.exists(archivo_db):
    print(f"Base de datos no encontrada en {archivo_db}. Creando base de datos y tablas.")
    # Esto crea el archivo DB vacío
    with open_connect() as con:
        pass
    crear_tablas()
else:
    print(f"Base de datos ya existe en: {archivo_db}.")
    # Opcional: si quieres crear tablas aunque DB exista, descomenta:
    # crear_tablas()

