from db.connection import Database


class Producto:
    """
    Nueva clase Producto:
    -Maneja todos los productos, agregar, eliminar y listar
    -Adapta para PostgreSql
    """

    def __init__(self, db: Database):
        self.db = db

    # Cargar productos
    def cargar_productos(self, id, nombre, precio, stock):
        with self.db_connect() as con:
            cur = con.cursor()
            cur.execute("SELECT id, nombre, precio, stock FROM productos")
            return [{"id": r[0], "nombre": r[1], "precio": float(r[2]), "stock": r[3]} for r in cur.fetchall()]

def ver_productos(self, id, nombre, precio, stock):
    productos = cargar_productos(self)
    with self.db_connect() as con:
        if not productos:
         print("No hay productos.")
        return
    print("\n=== PRODUCTOS ===")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']} - Stock: {p['stock']}")

    # Listar productos
    def listar(self):
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY nombre")
            return[{"id": i[0], "nombre": i[1], "precio": float(i[2]), "stock": i[3]} for i in cur.fetchall()]
        
    # Agregar o Actualizar producto
    def agregar(self, nombre, precio, stock):
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO productos (nombre, precio, stock)
                VALUES (%s, %s, %s)
                ON CONFLICT (nombre) DO UPDATE SET precio=EXCLUDED.precio, stock=EXCLUDED.stock
            """, (nombre, precio, stock))
            print(f"Producto '{nombre}' agregado/actualizado.")

    # Eliminar Producto
    def eliminar(self, producto_id):
        with self.db.connect() as con:
            cur = con.cursor()
            cur.execute("SELECT FROM productos WHERE id=%s", (producto_id,))
            print(f"Producto con ID {producto_id} eliminado.")
            