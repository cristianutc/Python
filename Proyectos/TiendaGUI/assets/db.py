import os
import sqlite3
from contextlib import contextmanager
from db import export_dir

# -------------------------------
# Carpeta fija en AppData
# -------------------------------

APP_NAME = "MiTienda"

base_dir = os.path.join(os.environ["LOCALAPPDATA"], APP_NAME)
db_dir = os.path.join(base_dir, "DB")
export_dir = os.path.join(base_dir, "Archivos_Excel")

os.makedirs(db_dir, exist_ok=True)
os.makedirs(export_dir, exist_ok=True)

DB_FILE = os.path.join(db_dir, "tienda.db")


# -------------------------------
# Context manager para la DB
# -------------------------------
@contextmanager
def open_connect():
    """Abre y cierra automáticamente la conexión a la base de datos"""
    con = sqlite3.connect(DB_FILE)
    try:
        yield con
    finally:
        con.close()

# -------------------------------
# Crear todas las tablas
# -------------------------------
def crear_tablas():
    with open_connect() as con:
        cur = con.cursor()

        # Tabla usuarios
        cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            correo_electronico TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        # Tabla productos
        cur.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            precio REAL,
            stock INTEGER
        )
        """)

        # Tabla ventas
        cur.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            producto_id INTEGER,
            cantidad INTEGER,
            precio_unitario REAL,
            total REAL,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
        """)

        # Tabla altas
        cur.execute("""
        CREATE TABLE IF NOT EXISTS altas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            producto_id INTEGER,
            cantidad INTEGER,
            precio_unitario REAL,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
        """)

        # Tabla merma
        cur.execute("""
        CREATE TABLE IF NOT EXISTS merma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            producto_id INTEGER,
            cantidad INTEGER,
            motivo TEXT,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
        """)

        # Tabla resumen_dia
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_dia (
            fecha TEXT,
            producto_id INTEGER,
            cantidad_total INTEGER,
            ingreso_total REAL,
            PRIMARY KEY (fecha, producto_id)
        )
        """)

        # Tabla resumen_semana
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_semana (
            anio_semana TEXT,
            producto_id INTEGER,
            cantidad_total INTEGER,
            ingreso_total REAL,
            PRIMARY KEY (anio_semana, producto_id)
        )
        """)

        # Tabla resumen_mes
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_mes (
            anio_mes TEXT,
            producto_id INTEGER,
            cantidad_total INTEGER,
            ingreso_total REAL,
            PRIMARY KEY (anio_mes, producto_id)
        )
        """)

        # Tabla resumen_anio
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_anio (
            anio TEXT,
            producto_id INTEGER,
            cantidad_total INTEGER,
            ingreso_total REAL,
            PRIMARY KEY (anio, producto_id)
        )
        """)

        con.commit()
        print("Todas las tablas se han creado correctamente.")

# -------------------------------
# Ejecutar al iniciar el script
# -------------------------------
if __name__ == "__main__":
    crear_tablas()
