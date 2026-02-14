from contextlib import contextmanager
import psycopg2
import os

#----------------------------
#---CONFUGURACION DE LA DB---
#----------------------------

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "tienda"), # Nombre de la DB en PostgreSQL
    "user": os.getenv("DB_USER", "pepino"), # Usuario de PostgreSQL
    "password": os.getenv("DB_PASS", "calistenia100"), # Contraseña del usuario
    "host": os.getenv("DB_HOST", "localhost"), # Host (localhost si es local)
    "port": os.getenv("DB_PORT", 5432) # Puerto PostgreSQL
}

class Database:
    """
    Nueva clase Database:
    -Gestiona la conexion a PostgreSQL
    -Uso de context manager para commit/rollback automatico
    -Evita tener codigo repetido de conexion
    """
    def __init__(self, config=DB_CONFIG):
        self.config = config 

    @contextmanager
    def connect(self):
        conn = psycopg2.connect(**self.config)
        try:
            yield conn
            conn.commit() # Guardamos automaticamente al salir del bloque
        except Exception:
            conn.rollback() # Si hay error, revertimos cambios
            raise
        finally:
            conn.close() # Cerramos la conexion al final
        

class InicializadorDB:
    """
    Inicializa todas las tablas necesarias:
    - usuarios
    - productos
    - ventas
    - altas
    - merma
    """

    def __init__(self, db: Database):
        self.db = db

    def crear_tablas(self):
        with self.db.connect() as con:
            cur = con.cursor()

            # Tabla usuarios
            cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre TEXT,
                edad INTEGER,
                correo_electronico TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            """)

            # Tabla productos
            cur.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id SERIAL PRIMARY KEY,
                nombre TEXT UNIQUE,
                precio NUMERIC(10,2),
                stock INTEGER
            )
            """)

            # Tabla ventas
            cur.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                id SERIAL PRIMARY KEY,
                fecha TIMESTAMP DEFAULT NOW(),
                producto_id INTEGER REFERENCES productos(id),
                cantidad INTEGER,
                precio_unitario NUMERIC(10,2),
                total NUMERIC(10,2)
            )
            """)

            # Tabla altas
            cur.execute("""
            CREATE TABLE IF NOT EXISTS altas (
                id SERIAL PRIMARY KEY,
                fecha TIMESTAMP DEFAULT NOW(),
                producto_id INTEGER REFERENCES productos(id),
                cantidad INTEGER,
                precio_unitario NUMERIC(10,2)
            )
            """)

            # Tabla merma
            cur.execute("""
            CREATE TABLE IF NOT EXISTS merma (
                id SERIAL PRIMARY KEY,
                fecha TIMESTAMP DEFAULT NOW(),
                producto_id INTEGER REFERENCES productos(id),
                cantidad INTEGER,
                motivo TEXT
            )
            """)

            cur.close()
            print("Todas las tablas PostgreSQL han sido creadas o ya existían.")