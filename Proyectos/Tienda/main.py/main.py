import csv  #para crear archivos csv
import sqlite3 # para crear la coneccion sqlite3
from datetime import datetime #para importar hora y fecha
#link para los Documentos
#https://docs.python.org/3/library/csv.html
#https://docs.python.org/3/library/sqlite3.html
#https://docs.python.org/3/library/datetime.html

DB_FILE = "tienda.db"
con = None

# ----------------------------
# Conexión a la base de datos
# ----------------------------
def abrir_conexion():
    global con
    if con is None:
        con = sqlite3.connect(DB_FILE)
    return con

def cerrar_conexion():
    global con
    if con:
        con.close()
        con = None
# ----------------------------
# Exportar ventas a excel
# ----------------------------

def exportar_ventas_excel():
    con = sqlite3.connect("tienda.db")
    cur = con.cursor()

    cur.execute("""
        SELECT 
            v.fecha,
            p.nombre,
            v.cantidad,
            v.precio_unitario,
            v.total
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        ORDER BY v.fecha
    """)

    with open("ventas.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario", "Total"])
        writer.writerows(cur.fetchall())

    con.close()
    print(" Archivo ventas.csv generado (abrir con Excel)")

# ----------------------------
# Exportar stock a excel
# ----------------------------

def exportar_stock_excel():
    con = sqlite3.connect("tienda.db")
    cur = con.cursor()

    cur.execute("""
        SELECT nombre, precio, stock
        FROM productos
        ORDER BY nombre
    """)

    with open("stock.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Producto", "Precio", "Stock"])
        writer.writerows(cur.fetchall())

    con.close()
    print(" Archivo stock.csv generado (abrir con Excel)")

# ----------------------------
# Exportar ingresos/altas a excel
# ----------------------------

def exportar_altas_excel():
    con = sqlite3.connect("tienda.db")
    cur = con.cursor()

    cur.execute("""
        SELECT 
            a.fecha,
            p.nombre,
            a.cantidad,
            a.precio_unitario
        FROM altas a
        JOIN productos p ON a.producto_id = p.id
        ORDER BY a.fecha
    """)

    with open("altas.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario"])
        writer.writerows(cur.fetchall())

    con.close()
    print(" Archivo altas.csv generado (abrir con Excel)")

# ----------------------------
# Exportar todo a excel
# ----------------------------

def exportar_todo_excel():
    exportar_ventas_excel()
    exportar_stock_excel()
    exportar_altas_excel()
    print(" Todos los archivos fueron exportados")


# ----------------------------
# Crear tablas
# ----------------------------
def crear_tablas():
    con = abrir_conexion()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE,
        precio REAL,
        stock INTEGER
    )
    """)
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
    con.commit()

# ----------------------------
# Funciones básicas
# ----------------------------
def cargar_productos():
    con = abrir_conexion()
    cur = con.cursor()
    cur.execute("SELECT id, nombre, precio, stock FROM productos")
    return [{"id": row[0], "nombre": row[1], "precio": row[2], "stock": row[3]} for row in cur.fetchall()]

def guardar_producto(nombre, precio, stock):
    con = abrir_conexion()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO productos (nombre, precio, stock)
        VALUES (?, ?, ?)
        ON CONFLICT(nombre) DO UPDATE SET
            precio=excluded.precio,
            stock=excluded.stock
    """, (nombre, precio, stock))
    con.commit()

# ----------------------------
# Funciones registrar movimientos
# ----------------------------
def registrar_alta(producto_id, cantidad, precio_unitario):
    con = abrir_conexion()
    cur = con.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
        INSERT INTO altas (fecha, producto_id, cantidad, precio_unitario)
        VALUES (?, ?, ?, ?)
    """, (fecha, producto_id, cantidad, precio_unitario))
    con.commit()

def registrar_venta(producto_id, cantidad, precio_unitario):
    con = abrir_conexion()
    cur = con.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = cantidad * precio_unitario
    cur.execute("""
        INSERT INTO ventas (fecha, producto_id, cantidad, precio_unitario, total)
        VALUES (?, ?, ?, ?, ?)
    """, (fecha, producto_id, cantidad, precio_unitario, total))
    con.commit()
    return total

def registrar_merma(producto_id, cantidad, motivo):
    con = abrir_conexion()
    cur = con.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
        INSERT INTO merma (fecha, producto_id, cantidad, motivo)
        VALUES (?, ?, ?, ?)
    """, (fecha, producto_id, cantidad, motivo))
    con.commit()

# ----------------------------
# Funciones del menú
# ----------------------------
def ver_productos():
    productos = cargar_productos()
    if not productos:
        print("No hay productos.")
        return
    print("\n===== PRODUCTOS =====")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']} (Stock {p['stock']})")

def agregar_producto():
    while True:
        try:
            nombre = input("Nombre del producto: ").lower()
            cantidad = int(input("Cantidad a ingresar: "))
            precio = float(input("Precio unitario: "))
            break
        except ValueError:
            print("Porfavor ingrese bien el producto")

    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            nuevo_stock = p["stock"] + cantidad
            guardar_producto(nombre, precio, nuevo_stock)
            registrar_alta(p["id"], cantidad, precio)
            print("Stock actualizado")
            return

    guardar_producto(nombre, precio, cantidad)
    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            registrar_alta(p["id"], cantidad, precio)
            break
    print("Producto agregado")

def eliminar_producto():
    ver_productos()
    nombre = input("Ingrese el nombre exacto del producto a eliminar: ").lower()
    
    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            con = abrir_conexion()
            cur = con.cursor()
            cur.execute("DELETE FROM productos WHERE id = ?", (p["id"],))
            con.commit()
            registrar_merma(p["id"], p["stock"], "Eliminación de producto")
            print(f"Producto '{nombre}' eliminado.")
            return
    print("Producto no encontrado.")

def buscar_producto():
    nombre = input("Ingrese el nombre a buscar: ").lower()
    con = abrir_conexion()
    cur = con.cursor()
    cur.execute("SELECT id, nombre, precio, stock FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cur.fetchall()
    if not resultados:
        print("No se encontraron productos.")
        return
    print("\nResultados encontrados:")
    for row in resultados:
        print(f"{row[0]}. {row[1]} - ${row[2]} (Stock {row[3]})")

def comprar_producto():
    productos = cargar_productos()
    if not productos:
        print("No hay productos.")
        return None

    carrito = []
    total_general = 0

    while True:
        print("\nProductos disponibles:")
        for i, p in enumerate(productos, start=1):
            print(f"{i}. {p['nombre']} - ${p['precio']} (Stock {p['stock']})")
        print("0. Pagar")

        try:
            op = int(input("Seleccione producto: "))
        except ValueError:
            print("Opción inválida")
            continue

        if op == 0:
            break
        if not (1 <= op <= len(productos)):
            print("Opción inválida")
            continue

        producto = productos[op - 1]
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida")
            continue

        if cantidad > producto["stock"]:
            print("No hay suficiente stock")
            continue

        carrito.append({"id": producto["id"], "nombre": producto["nombre"], "cantidad": cantidad, "precio": producto["precio"]})

    if not carrito:
        print("No se seleccionó ningún producto.")
        return None

    print("\n===== RESUMEN DE COMPRA =====")
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total_general += subtotal
        print(f"{item['nombre']} x{item['cantidad']} = ${subtotal}")

    confirmar = input(f"Total a pagar: ${total_general}. Confirmar compra (s/n): ").lower()
    if confirmar != "s":
        print("Compra cancelada")
        return None

    for item in carrito:
        registrar_venta(item["id"], item["cantidad"], item["precio"])
        con = abrir_conexion()
        cur = con.cursor()
        cur.execute("UPDATE productos SET stock = stock - ? WHERE id = ?", (item["cantidad"], item["id"]))
        con.commit()

    print("Compra realizada con éxito.")
    return carrito

def generar_ticket(carrito):
    print("\n===== TICKET =====")
    total = 0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['nombre']} x{item['cantidad']} = ${subtotal}")
    print(f"TOTAL A PAGAR: ${total}")
    print("==================")

# ----------------------------
# Reportes avanzados
# ----------------------------
def reporte_stock():
    productos = cargar_productos()
    print("\n===== REPORTE DE STOCK =====")
    for p in productos:
        print(f"{p['nombre']} - Stock: {p['stock']}")

def reporte_ventas():
    con = abrir_conexion()
    cur = con.cursor()
    cur.execute("""
        SELECT p.nombre, SUM(v.cantidad) as total_vendido, SUM(v.total) as total_recaudado
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        GROUP BY p.nombre
    """)
    rows = cur.fetchall()
    print("\n===== REPORTE DE VENTAS POR PRODUCTO =====")
    for row in rows:
        print(f"{row[0]} - Cantidad vendida: {row[1]} - Total recaudado: ${row[2]}")

def reporte_ventas_fecha():
    desde = input("Fecha desde (YYYY-MM-DD): ")
    hasta = input("Fecha hasta (YYYY-MM-DD): ")
    con = abrir_conexion()
    cur = con.cursor()
    cur.execute("""
        SELECT p.nombre, SUM(v.cantidad) as total_vendido, SUM(v.total) as total_recaudado
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        WHERE date(v.fecha) BETWEEN ? AND ?
        GROUP BY p.nombre
    """, (desde, hasta))
    rows = cur.fetchall()
    print(f"\n===== REPORTE DE VENTAS DESDE {desde} HASTA {hasta} =====")
    for row in rows:
        print(f"{row[0]} - Cantidad vendida: {row[1]} - Total recaudado: ${row[2]}")

def historial_completo():
    con = abrir_conexion()
    cur = con.cursor()
    print("\n===== HISTORIAL DE VENTAS =====")
    cur.execute("""
        SELECT v.fecha, p.nombre, v.cantidad, v.precio_unitario, v.total
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        ORDER BY v.fecha
    """)
    for row in cur.fetchall():
        print(f"{row[0]} | {row[1]} x{row[2]} = ${row[4]} (Precio unitario: {row[3]})")

    print("\n===== HISTORIAL DE ALTAS =====")
    cur.execute("""
        SELECT a.fecha, p.nombre, a.cantidad, a.precio_unitario
        FROM altas a
        JOIN productos p ON a.producto_id = p.id
        ORDER BY a.fecha
    """)
    for row in cur.fetchall():
        print(f"{row[0]} | {row[1]} x{row[2]} (Precio unitario: {row[3]})")

# ----------------------------
# Menú principal
# ----------------------------
def menu():
    crear_tablas()
    while True:
        print("\n===== MENU TIENDA =====")
        print("1. Ver productos")
        print("2. Comprar producto")
        print("3. Agregar producto")
        print("4. Buscar producto")
        print("5. Eliminar producto")
        print("6. Historial completo")
        print("7. Reporte de stock")
        print("8. Reporte de ventas totales")
        print("9. Reporte de ventas por fecha")
        print("10. Exportar a excel")
        print("11. Salir")

        try:
            op = int(input("Ingrese opción: "))
        except ValueError:
            print("Opción inválida")
            continue

        if op == 1:
            ver_productos()
        elif op == 2:
            carrito = comprar_producto()
            if carrito:
                generar_ticket(carrito)
        elif op == 3:
            agregar_producto()
        elif op == 4:
            buscar_producto()
        elif op == 5:
            eliminar_producto()
        elif op == 6:
            historial_completo()
        elif op == 7:
            reporte_stock()
        elif op == 8:
            reporte_ventas()
        elif op == 9:
            reporte_ventas_fecha()
        elif op == 10:
            menu_exportaciones()
        elif op == 11:
            print("Saliendo...")
            cerrar_conexion()
            break
        else:
            print("Opción inválida")

def menu_exportaciones():
    while True:
        print("\n===== EXPORTAR A EXCEL =====")
        print("1. Exportar ventas a Excel")
        print("2. Exportar stock a Excel")
        print("3. Exportar ingresos a Excel")
        print("4. Exportar todo a Excel")
        print("5. Volver al menú principal")

        try:
            op = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido")
            continue

        if op == 1:
            exportar_ventas_excel()
        elif op == 2:
            exportar_stock_excel()
        elif op == 3:
            exportar_altas_excel()
        elif op == 4:
            exportar_todo_excel()
        elif op == 5:
            break
        else:
            print("Opción inválida")


menu()
