from db.connection import Database
from datetime import datetime

class Venta:
    """
    Nueva clase Venta:
    -Registra ventas, altas y mermas
    -Actualiza stock automaticamente al vender
    """

    def __init__(self, db: Database):
        self.db = db

    # Registrar una venta
    def registrar_venta(self, producto_id, cantidad, precio_unitario):
        total = cantidad * precio_unitario
        fecha = datetime.now()
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("""
            INSERT INTO ventas (fecha, producto_id, cantidad, precio_unitario, total)
            VALUES (%s, %s, %s, %s, %s)
        """, (fecha, producto_id, cantidad, precio_unitario, total))
            cur.execute("UPDATE productos SET stock = stock - %s WHERE id=%s", (cantidad, producto_id))
            return total
        
    # Registrar entrada de stock
    def registrar_alta(self, producto_id, cantidad, precio_unitario):
        fecha = datetime.now()
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO altas ( fecha, producto_id, cantidad, precio_unitario)
                VALUES (%s, %s, %s,%s)
            """, (fecha, producto_id, cantidad, precio_unitario))

    # Registrar merma (productos eliminados o dañados)
    def registrar_merma (self, producto_id, cantidad, motivo):
        fecha = datetime.now()
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO merma (fecha, producto_id, cantodad, motivo)
                VALUES (%s, %s, %s, %s)
            """, (fecha, producto_id, cantidad, motivo))
            