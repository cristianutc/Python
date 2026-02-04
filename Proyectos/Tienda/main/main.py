import csv  # Para crear archivos CSV
import sqlite3  # Para crear la conexión SQLite3
import os #Para crear carpetas (mkdir)
from datetime import datetime  # Para importar hora y fecha

#link para la Documentacion de las librerias usadas
#https://docs.python.org/3/library/csv.html
#https://docs.python.org/3/library/sqlite3.html
#https://docs.python.org/3/library/datetime.html

# Obtener la ruta al directorio donde está el script (main.py)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Definir las rutas correctas para la base de datos y los archivos exportados fuera de main
# Usamos una ruta relativa para evitar que las carpetas se creen en main

# Definir las rutas para la base de datos y los archivos exportados
db_dir = os.path.join(script_dir, "DB")  # Ruta donde está la base de datos
export_dir = os.path.join(script_dir,"Archivos_Excel")  # Ruta para los archivos exportados

# Definir la ruta completa para el archivo de la base de datos
DB_FILE = os.path.join(db_dir, "/home/pepino/Documentos/Python/Proyectos/Tienda/DB/tienda.db")
ventas_csv_path = os.path.join(export_dir, "/home/pepino/Documentos/Python/Proyectos/Tienda/Archivos_Excel/ventas.csv")
Stock_csv_path = os.path.join(export_dir, "/home/pepino/Documentos/Python/Proyectos/Tienda/Archivos_Excel/stock.csv")
Altas_csv_path = os.path.join(export_dir, "/home/pepino/Documentos/Python/Proyectos/Tienda/Archivos_Excel/altas.csv")

# Verificar si la carpeta DB existe, y si no, crearla
if not os.path.exists(DB_FILE):
    os.makedirs(DB_FILE)  # Crea la carpeta DB si no existe
    print(f"Carpeta {DB_FILE} creada.")

# Verificar si la base de datos ya existe
if not os.path.exists(DB_FILE):
    print(f"Base de datos no encontrada en: {DB_FILE}. Creando base de datos.")
    # Si la base de datos no existe, crearla
    con = sqlite3.connect(DB_FILE)
    con.close()  # Cerramos la conexión después de crearla
else:
    print(f"Base de datos ya existe en: {DB_FILE}")

# Conexión a la base de datos
con = None

# Función para abrir la conexión con la base de datos
# ----------------------------
# Conexión a la base de datos
# ----------------------------
def abrir_conexion():
    global con #global con Aquí se indica que con es una variable global. global le dice a Python que 
    #la variable con que vamos a modificar dentro de esta función es la misma variable que está definida
    #en el alcance global del programa (fuera de la función).
    if con is None: #if con is None: Esta línea evalúa si la variable con es None (es decir, si no ha sido inicializada aún).
        #Esto es útil porque la conexión a la base de datos solo debe abrirse una vez (para evitar múltiples conexiones abiertas innecesarias).
        con = sqlite3.connect(DB_FILE) #sqlite3.connect() devuelve un objeto de conexión que se asigna a con. Si la conexión ya estaba abierta, esta línea no se ejecuta.
    return con #return con Finalmente, la función devuelve el objeto con, que es la conexión a la base de datos.
#Esto permite que cualquier función que llame a abrir_conexion pueda usar la misma conexión abierta.

def cerrar_conexion(): #Funcion para cerrar la coneccion de la base de datos
    global con #Aquí, también se indica que con es una variable global. Esto es necesario porque queremos modificar la variable global con (la conexión) dentro de la función. Sin la palabra clave global, Python trataría de crear una nueva variable local dentro de la función.
    if con: #if con:Esta línea verifica si con tiene un valor que no sea None.Si con tiene un valor (es decir, si la conexión está abierta), la condición se cumple y se ejecuta el siguiente bloque de código.Si la conexión ya está cerrada (es decir, con es None), la condición no se cumple y no hace nada.
        con.close() #con.close()Si la conexión está abierta, esta línea cierra la conexión a la base de datos. con.close() es un método del objeto de conexión de SQLite que cierra la conexión a la base de datos.Después de ejecutar esta línea, la conexión ya no estará activa y no se podrán ejecutar más consultas hasta que se abra una nueva conexión.
        con = None #Esta línea asegura que la variable con sea None después de cerrar la conexión.Esto es útil para que el programa sepa que no hay una conexión abierta. Si más tarde intentamos usar con sin haberla reabierto, sabremos que la conexión no está activa.Establecer con a None también ayuda a evitar que accidentalmente se intente usar una conexión cerrada.
# ----------------------------
# Exportar ventas a excel
# ----------------------------

def exportar_ventas_excel():
    con = sqlite3.connect(DB_FILE) # nos conectamos a la base de datos
    cur = con.cursor() #Este método se usa para crear un cursor de base de datos, que es un objeto que 
    #permite interactuar con la base de datos. El cursor se utiliza para ejecutar consultas SQL y manipular los datos en la base de datos.

#El método execute() del cursor se usa para ejecutar consultas SQL dentro de la base de datos.
#Puedes usar execute() para ejecutar cualquier tipo de consulta: SELECT, INSERT, UPDATE, DELETE, etc.
#Este método toma una cadena de texto que contiene la consulta SQL.
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
    
    """SELECT: Selecciona las columnas que quieres obtener de la base de datos.
v.fecha: La fecha de la venta (de la tabla ventas).
p.nombre: El nombre del producto (de la tabla productos).
v.cantidad: La cantidad de productos vendidos (de la tabla ventas).
v.precio_unitario: El precio por unidad del producto (de la tabla ventas).
v.total: El total de la venta (de la tabla ventas)."""

    """FROM ventas v: Indica que los datos provienen de la tabla ventas, y le asigna un alias v para 
    hacer referencia a ella más fácilmente. JOIN productos p ON v.producto_id = p.id: Realiza un 
    JOIN entre la tabla ventas y la tabla productos, de manera que las filas de la tabla ventas se 
    emparejan con las filas correspondientes de la tabla productos basándose en la relación entre el 
    campo producto_id en ventas y el campo id en productos. ORDER BY v.fecha: Ordena los resultados 
    de la consulta por la fecha de la venta (de la tabla ventas), para que las ventas más recientes 
    o antiguas se muestren primero, dependiendo de la dirección del orden."""

# Usar la carpeta Exportados y crear el archivo en esa ubicación
    with open(ventas_csv_path, "w", newline="", encoding="utf-8") as archivo: #Abre un archivo y lo cierra automáticamente cuando se sale del bloque with open()
        #ventas_csv_path:Es la ruta al archivo CSV donde se guardarán los datos exportados
        #"W":Indica que el archivo se abrirá en modo escritura (es decir, se sobrescribirá si ya existe un archivo con el mismo nombre).
        #newline="": Esto se usa para controlar cómo se gestionan los saltos de línea en los archivos CSV. asegura que Python maneje correctamente los saltos de línea en plataformas cruzadas (Windows, Linux, etc.).
        #encoding="utf-8": Especifica que el archivo se guardará con codificación UTF-8, que es una codificación estándar y compatible con caracteres especiales (como acentos, símbolos, etc.).
        writer = csv.writer(archivo)
        #writer = csv.writer(archivo)
        #Aquí estamos creando un escritor de CSV con el módulo csv de Python.csv.writer(archivo): 
        # Crea un objeto que puede escribir datos en el archivo abierto (archivo). Este objeto se usará para escribir las filas y encabezados en el archivo CSV.
        writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario", "Total"])
        #writer.writerow([...]): Escribe una fila en el archivo CSV. En este caso, la fila escrita es 
        # el encabezado de las columnas en el archivo CSV.
        writer.writerows(cur.fetchall())
        #cur.fetchall(): Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

    con.close() #Cierra la conexión a la base de datos. Es una buena práctica cerrar la conexión 
    #cuando ya no la necesites, para liberar los recursos del sistema.
    print(" Archivo ventas.csv generado (abrir con Excel)")

# ----------------------------
# Exportar stock a excel
# ----------------------------

def exportar_stock_excel(): #funcion para exportar archivos csv
    con = sqlite3.connect(DB_FILE) #nos conectamos DB donde se eucuentra ubicado el archivo 
    cur = con.cursor() #para hacer consultas sql
    
    cur.execute("""
        SELECT nombre, precio, stock
        FROM productos
        ORDER BY nombre
    """) #ejecutamos la consulta

    with open(Stock_csv_path, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
        writer = csv.writer(archivo) #creamos el archivo csv
        writer.writerow(["Producto", "Precio", "Stock"]) #Escribe una fila en el archivo CSV. (encabezado)
        writer.writerows(cur.fetchall()) #Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

    con.close() #Cierra la conexion a la base de datos
    print(" Archivo stock.csv generado (abrir con Excel)")

# ----------------------------
# Exportar ingresos/altas a excel
# ----------------------------

def exportar_altas_excel(): #funcion para exportar archivos csv
    con = sqlite3.connect(DB_FILE) #nos conectamos DB donde se eucuentra ubicado el archivo 
    cur = con.cursor() #para hacer consultas sql

    cur.execute("""
        SELECT 
            a.fecha,
            p.nombre,
            a.cantidad,
            a.precio_unitario
        FROM altas a
        JOIN productos p ON a.producto_id = p.id
        ORDER BY a.fecha
    """) #ejecutamos la consulta

    with open(Altas_csv_path, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
        writer = csv.writer(archivo) #creamos el archivo csv
        writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario"]) #Escribe una fila en el archivo CSV. (encabezado)
        writer.writerows(cur.fetchall()) #Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

    con.close() #Cierra la conexion a la base de datos
    print(" Archivo altas.csv generado (abrir con Excel)")

# ----------------------------
# Exportar todo a excel
# ----------------------------

def exportar_todo_excel(): #funcion para exportar todos los archivos csv 
    con = sqlite3.connect(DB_FILE) #nos conectamos DB donde se eucuentra ubicado el archivo 
    #solo llamamos todas las funciones creadas para exportar archivos csv
    exportar_ventas_excel()
    exportar_stock_excel()
    exportar_altas_excel()
    print(" Todos los archivos fueron exportados")


# ----------------------------
# Crear tablas
# ----------------------------
def crear_tablas(): #esta funcion es para crear tablas sql
    con = abrir_conexion() #abrimos coneccion para crear la DB
    cur = con.cursor() #para ejecutar sql y crear la DB
    cur.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE,
        precio REAL,
        stock INTEGER
    )
    """) #ejecutamos la consulta y creamos la tabla productos
    #hacemos otra ejecucion
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
    """) #Creamos la tabla ventas
    #hacemos otra ejecucion
    cur.execute("""
    CREATE TABLE IF NOT EXISTS altas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        producto_id INTEGER,
        cantidad INTEGER,
        precio_unitario REAL,
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )
    """) #ejecutamos la consulta y creamos la tabla altas
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
