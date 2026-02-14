from db.connection import Database
import csv
from pathlib import Path

# models/reporte.py
class Reporte:
    def __init__(self, db):
        self.db = db
        """
        Inicializa la clase Reporte con la conexión a la base de datos.
        db: instancia de Database
        """

    def ventas_por_producto(self):
        """Muestra el total vendido de cada producto"""
        with self.db.connect() as con:
            with con.cursor() as cur:
                cur.execute("""
                    SELECT p.nombre, COALESCE(SUM(vp.cantidad), 0) as total_vendido
                    FROM productos p
                    LEFT JOIN ventas_productos vp ON vp.producto_id = p.id
                    GROUP BY p.nombre
                    ORDER BY total_vendido DESC
                """)
                resultados = cur.fetchall()
                print("Ventas por producto:")
                for fila in resultados:
                    print({"producto": fila[0], "total_vendido": fila[1]})

    def ventas_por_usuario(self):
        """Muestra el total de compras realizadas por cada usuario"""
        with self.db.connect() as con:
            with con.cursor() as cur:
                cur.execute("""
                    SELECT u.nombre, COALESCE(SUM(v.total), 0) as total_compras
                    FROM usuarios u
                    LEFT JOIN ventas v ON v.usuario_id = u.id
                    GROUP BY u.nombre
                    ORDER BY total_compras DESC
                """)
                resultados = cur.fetchall()
                print("Ventas por usuario:")
                for fila in resultados:
                    print({"usuario": fila[0], "total_compras": float(fila[1])})

    def inventario_actual(self):
        """Muestra la cantidad actual en stock de cada producto"""
        with self.db.connect() as con:
            with con.cursor() as cur:
                cur.execute("SELECT nombre, stock FROM productos ORDER BY nombre")
                resultados = cur.fetchall()
                print("Inventario actual:")
                for fila in resultados:
                    print({"producto": fila[0], "stock": fila[1]})
