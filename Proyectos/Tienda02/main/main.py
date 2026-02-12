import os
import sqlite3
import csv
import bcrypt
from datetime import datetime
from contextlib import contextmanager

def main():
        
    crear_tablas()
    while not login():
            print("Intento Fallido. Vuelve a Intentar")

    menu()

def menu():
    while True:
        print("\t ======= MENU TIENDA CHINA ======")
        print("1. Ver productos")
        print("2. Vender Productos")
        print("3. Buscar Producto")
        print("4. Agregar Producto")
        print("5. Eliminar Producto")
        print("6. Menu de Reportes")
        print("7. Salir Del Programa\n")

        try:
            op = int(input("Ingrese una opcion del Menu y click Enter\n"))
        except ValueError:
            print("Opcion invalida")
            continue

        if op == 1:
            ver_productos()
        elif op == 2:
            comprar_productos()
        elif op == 3:
            buscar_productos()
        elif op == 4:
            agregar_productos()
        elif op == 5:
            eliminar_productos()
        elif op == 6:
            menu_de_reportes()
        elif op == 7:
            break
        else:
            print("Opcion invalida")

def menu_de_reportes():
    while True:

        print("\t =======MENU DE REPORTES======")
        print("1. Reporte de Stock")
        print("2. Reportes de ventas totales")
        print("3. Reportes de Ventas por Fechas")
        print("4. Historial Completo")
        print("5. Exportar a Excel")
        print("6. Regresar hacia Atras\n")

        try:
            op = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Opcion invalida")
            continue

        if op == 1:
            reporte_stock()
        elif op == 2:
            reporte_ventas()
        elif op == 3:
            reporte_ventas_fecha()
        elif op == 4:
            historial_completo()
        elif op == 5:
            menu_excel()
        elif op == 6:
            break
        else:
            print("Opcion invalida")

def menu_excel():
    while True:

        print("\t ======MENU EXCEL======")
        print("1. Exportar Ventas de Excel")
        print("2. Exportar Ingresos a Excel")
        print("3. Exportar Stock a Excel")
        print("4. Exportar todo a Excel")
        print("5. Regresar Hacia Atras\n")

        try:
            op = int(input("Ingrese una Opcion: "))
        except ValueError:
            print("Opcion Invalida")
            continue

        if op == 1:
            exportar_ventas_excel()
        elif op == 2:
            exportar_altas_excel()
        elif op == 3:
            exportar_stock_excel()
        elif op == 4:
            exportar_todo_excel()
        elif op == 5:
            break
        else:
            print("Opcion Invalida")

#------------------
#---Generar hash---
#------------------
def has_password(password):
    salt = bcrypt.gensalt() # Genera un "salt" ubico para cada Contraseña
    return bcrypt.hashpw(password.encode(), salt).decode() #Devuelve el hash codificado a texto

#Verificamos la Contraseña
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode()) # Comparamos el hash con la contraseña ingresada
 
#Obtener ruta al directorio donde esta el script (main)
script_dir = os.path.dirname(os.path.abspath(__file__))

db_dir = os.path.join(script_dir, "DB") # Ruta de la DB
export_dir = os.path.join(script_dir, "Archivos_Excel") # Ruta para los Archivos Exportados

#Definir la ruta completa para la base de datos y los archivos excel
DB_FILE = os.path.join(db_dir, "tienda.db")
Ventas_csv_path = os.path.join(export_dir, "ventas.csv")
Stock_csv_path = os.path.join(export_dir, "stock.csv")
Altas_csv_path = os.path.join(export_dir, "altas.csv")

#Verificar si la carpeta DB existe, si no crearla
if not os.path.exists(db_dir):
    os.makedirs(db_dir)
    print(f"carpeta {db_dir} Creada.")

#Verificar si la carpeta Aerchivos_Excel existe, si no crearla
if not os.path.exists(export_dir):
    os.makedirs(export_dir)
    print(f"Carpeta {export_dir} Creada.")

#Verificar si la Base de Datos exitse
if not os.path.exists(DB_FILE):
    print(f"Base de datos no encontrada en: {DB_FILE}. Creando la Base de Datos.")
    con = sqlite3.connect(DB_FILE)
    con.close() #Cerramos la conexion despues de crearla
else:
    print(f"Base de Datos ya Existe en: {DB_FILE}")

#Creamos la variable Global para la Conexion a la DB
con = None

#----------------------------
# Conexion a la Base de Datos
#----------------------------
# Creando el context manager usando un decorador
@contextmanager
def open_connect():
    con = sqlite3.connect(DB_FILE)
    try:
        yield con # Proporcionamos la conexión para su uso
    finally:
        con.close() # Cerramos la conexión cuando se termina el bloque

#-----------------------------
# --------Crear Tablas--------
#-----------------------------

def crear_tablas():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    edad INTEGER,
                    correo_electronico TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                    )
                    """) # Tabla Usuario
        cur.execute("""
        CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE,
                    precio REAL,
                    stock INTEGER
                    )
                    """) # Creamos Tabla Productos
        cur.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT,
                    producto_id INTIGER,
                    cantidad INTEGER,
                    precio_unitario REAL,
                    total REAL,
                    FOREIGN KEY(producto_id) REFERENCES productos(id)
                    )
                    """) # Creamos la Tabla Ventas
        cur.execute("""
        CREATE TABLE IF NOT EXISTS altas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT,
                    producto_id INTEGER,
                    cantidad INTEGER,
                    precio_unitario REAL,
                    FOREIGN KEY(producto_id) REFERENCES productos(id)
                    )
                    """) # Creamos la Tabla Altas
        cur.execute("""
        CREATE TABLE IF NOT EXISTS merma (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT,
                    producto_id INTEGER,
                    cantidad INTEGER,
                    motivo TEXT,
                    FOREIGN KEY(producto_id) REFERENCES productos(id)
                    )
                    """) #Creamos la Tabla Merma
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_dia (
                    fecha TEXT,
                    producto_id INTEGER,
                    cantidad_total INTEGER,
                    ingreso_total REAL,
                    PRIMARY KEY (fecha, producto_id)
                    )
                    """) #Creamos la Tabla Resumen_dia
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_semana (
                    anio_semana TEXT,
                    producto_id INTEGER,
                    cantidad_total INTEGER,
                    ingreso_total REAL,
                    PRIMARY KEY (anio_semana, producto_id)
                    )
                    """) #Creamos la Tabla resumen_semana
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_mes (
                   anio_mes TEXT,
                    producto_id INTEGER,
                    caantidad_total INTEGER,
                    ingreso_total REAL,
                    PRIMARY KEY (anio_mes, producto_id) 
                    )
                    """) #Creamos la Tabla resumen_mes
        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_anio (
                    anio TEXT,
                    producto_id INTEGER,
                    cantidad_total INTEGER,
                    ingreso_total REAL,
                    PRIMARY KEY (anio, producto_id)
                    )
                    """) #Creamos la Tabla resumen_año
        con.commit() #Guardamos

#----------------------------
# ---Registrar Movimientos---
#----------------------------

def registrar_usuario():
    with open_connect() as con:
        cur = con.cursor()

        nombre = input("Ingrese su Nombre: \n")
        edad = input("Ingrese su Edad: \n")
        correo = input("Ingrese su Correo Electronico: \n")
        password = input("Ingrese su Contraseña:\n")

        # Verificamos si el correo ya Existe
        cur.execute("""
        SELECT * FROM usuarios WHERE correo_electronico = ?
                    """,(correo,))
        if cur.fetchone():
            print("Este Correo ya  esta Registrado.")
            return 
        password_hash = has_password(password) #Generamos el hash de la Contraseña

        try:
            cur.execute("""
            INSERT INTO usuarios (nombre, edad, correo_electronico, password)
                        VALUES(?, ?, ?, ?)
                    """, (nombre, edad, correo, password_hash))
            con.commit()
            print("Usuario Registrado Exitosamente")
        except Exception as e:
            print(f"Error al Registrar el Usuario: {e}")

            
def registrar_venta(producto_id, cantidad, precio_unitario):
    with open_connect() as con:
        cur = con.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d  %H: %M: %S:")
        total = cantidad * precio_unitario
        cur.execute("""
        INSERT INTO ventas (fecha, producto_id, cantidad, precio_unitario, total)
                    VALUES (?, ?, ?, ?, ?)
                    """, (fecha, producto_id, cantidad, precio_unitario, total))
        con.commit()
        return total
    
def registrar_alta(producto_id, cantidad, precio_unitario):
    with open_connect() as con:
        cur = con.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d  %H: %M: %S:")
        cur.execute("""
        INSERT INTO altas (fecha, producto_id, cantidad, precio_unitario)
                    VALUES (?, ?, ?, ?)
                    """, (fecha, producto_id, cantidad, precio_unitario))
        con.commit()

def registrar_merma(producto_id, cantidad, motivo):
    with open_connect() as con:
        cur = con.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d  %H: %M: %S:")
        cur.execute("""
        INSERT INTO merma (fecha, producto_id, cantidad, motivo)
                    VALUES (?, ?, ?, ?)
                    """, (fecha, producto_id, cantidad, motivo))
        con.commit()
        
            
def cargar_productos():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("SELECT id, nombre, precio, stock FROM productos")
        return [{"id": i[0], "nombre": i[1], "precio": i[2], "stock": i[3]} for i in cur.fetchall()] 
    
def guardar_producto(nombre, precio, stock):
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO productos (nombre, precio, stock)
                    VALUES (?,?,?)
                    ON CONFLICT(nombre) DO UPDATE SET
                    precio=excluded.precio,
                    stock=excluded.stock
                    """, (nombre,precio,stock))
        con.commit()

#------------------------
#---Funciones del Menu---
#------------------------
def login():
    with open_connect() as con:
        cur = con.cursor()
    
        op = input("Ya tienes una cuenta? (s/n): \n")

        if op == "s":
            correo = input("Correo Electronico: \n")
            password = input("Contraseña: \n")

            cur.execute("""
            SELECT * FROM usuarios WHERE correo_electronico = ?
            """, (correo,))

            usuario = cur.fetchone()

            if usuario:
                if check_password(password, usuario[4]):
                    print("Login Exitoso")
                    return True
                else:
                    print("Contraseña Incorrecta")
                    return False
            else:
                print("Usuario no Econtrado")
                return False
        else:
            registrar_usuario()
            return False

def ver_productos():
    productos = cargar_productos()
    if not productos:
        print("No Hay Productos.\n")
        return
    print("\n====== PRODUCTOS =======")
    for p in productos:
        print(f"{p['id']}. {p['nombre']}. {p['precio']}. (Stock {p['stock']})")

def comprar_productos():
    productos = cargar_productos()
    if not productos:
        print("No hay Productos.\n")
        return None

    carrito = []
    total_general = 0

    while True:
        print("\nProductos Disponibles: ")
        for i, p in enumerate(productos, start=1):
            print(f"{i}. {p['nombre']} - ${p['precio']} - (Stock {p['stock']})")
        print("0. Pagar")

        try:
            op = int(input("Selecione Producto: "))
        except ValueError:
            print("Opcion Invalida")
            continue

        if op == 0:
            break
        if not (1 <= op <= len(productos)):
            print("Opcion invalida")
            continue

        productos = productos[op - 1]
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad Invalida")
            continue

        if cantidad > productos["stock"]:
            print("No hay suficiente stock")
            continue

        carrito.append({"id": productos["id"], "nombre": productos["nombre"], "cantidad": cantidad, "precio": productos["precio"]})

    if not carrito:
        print("No Selecciono Ningun Producto.")
        return None
    
    print("===== RESUMEN DE COMPRA =====")
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total_general += subtotal
        print(f"{item['nombre']} x {item['cantidad']} = ${subtotal}")

    confimar = input(f"Total a Pagar: ${total_general}. \n Confirmar Compra (s/n): ").lower

    if confimar != "s":
        print("Compra Cancelada")
        return None
    
    for item in carrito:
        registrar_venta(item["id"], item["cantidad"], item["precio"])
        with open_connect() as con:
            cur = con.cursor()
            cur.execute("UPDATE productos SET stock = stock - ? WHERE id = ?",  (item["cantidad"], item["id"]))
            con.commit()

    actualizar_resumen()
    print("Venta realizada correctamente.")

            
def agregar_productos():
    while True:
        try:
            nombre = input("Nombre del Producto: ").lower()
            cantidad = int(input("Cantidad a Ingresar: "))
            precio = float(input("Precio Unitario: "))
            break
        except ValueError:
            print("Porfavor Ingrese bien el Producto")

    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            nuevo_stock = p["stock"] + cantidad
            guardar_producto(nombre, cantidad, precio)
            registrar_alta(p["id"], cantidad, precio)
            print("Stock Actualizado.")
            return
        
    guardar_producto(nombre, precio, cantidad)
    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            registrar_alta(p["id"], cantidad, precio)
            break
    print("Producto Agregado Exitosamente")
        
def generar_ticket(carrito):
    print("\t ===== TICKET =====")
    total = 0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['precio']} x {item['cantidad']} = ${subtotal}")
    print(f"TOTAL A PAGAR: ${total}")
    print("=========================")

def buscar_productos():
    nombre = input("Ingresar el Nombre a Buscar: ").lower()
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("SELECT id, nombre, precio, stock FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        resultados = cur.fetchall()
        if not resultados:
            print("No se Econtraron Productos.")
            return
        print("\n Resultados Econtrados.")
        for i in resultados:
            print(f"{i[0]}. {i[1]} - ${i[2]} (Stock {i[3]})")

def eliminar_productos():
    ver_productos()
    nombre = input("Ingrese el Nombre Exacto del Producto a Eliminar: ").lower()

    productos = cargar_productos()
    for p in productos:
        if p["nombre"]  == nombre:
            with open_connect() as con:
                cur = con.cursor()
                cur.execute("DDELTE FROM productos WHERE id = ?", (p["id"]))
                con.commit()
                registrar_merma(p["id"], p["stock"], "Eliminacion de producto.")
                print(f"Producto '{nombre}' Eliminado.")
                return
    print("Producto no econtrado.")

#------------------------
#---REPORTES AVANZADOS---
#------------------------

def reporte_stock():
    productos = cargar_productos
    print(("\t==== REPORTE DE STOCK ===="))
    for p in productos:
        print(f"{p['nombre']} - Stock: {p['stock']}")

def reporte_ventas():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT p.nombre, SUM(v.cantidad) as total_vendido, SUM(v.total) as total_recaudado
                   FROM ventas v
                    JOIN productos p ON v.producto_id = p.id
                    GROUP BY p.nombre
                     """)
        rows = cur.fetchall()
        print("\t==== REPORTE DE VENTAS POR PRODUCTO ====")
        for i in rows:
            print(f"{i[0]} - Cantidad Vendida: {i[1]} - Total Recaudado_ ${i[2]}")

def reporte_ventas_fecha():
    desde = input("FEcha Desde (YYYY-MM-DD): ")
    hasta = input("Fecha Hasta (YYYY-MM-DD): ")
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT p.nombre, SUM(v.cantidad) as total_vendido, SUM(v.total) as total_recaudado
                   FROM ventas v
                    JOIN productos p ON v.producto_id = p.id
                    WHERE date(v.fecha) BETWEEN ? AND ?
                    GROUP BY p.nombre
                     """, (desde, hasta))
        rows = cur.fetchall()
        print(f"==== REPORTE DE VENTAS DESDE: {desde} - HASTA: {hasta} ====")
        for i in rows:
            print(f"{i[0]} - Cantidad Vendida: {i[1]} - Total Recaudado: ${i[2]}")

#--------------------------
#--- HISTORIAL COMPLETO ---
#--------------------------

def historial_completo():
    with open_connect() as con:
        cur = con.cursor()
        print("\t==== HISTORIAL DE VENTAS ====")
        cur.execute("""
        SELECT v.fecha, p.nombre, v.cantidad, v.precio_unitario, v.total
                   FROM ventas v
                    JOIN productos p ON v.productos_id = p.id 
                    ORDER BY v.fecha
                    """)
        for i in cur.fetchall():
            print(f"{i[0]} | {i[1]} x {i[2]} = ${i[4]} (Precio unitario: {i[3]})")

        print("\t====HISTORIAL DE ALTAS ====")
        cur.execute("""
        SELECT a.fecha, p.nombre, a.cantidad, a.precio_unitario
                   FROM altas a
                    JOIN productos p ON a.producto_id = p.id
                    ORDER BY a.fecha
                     """)
        for i in cur.fetchall():
            print(f"{i[0]} | {i[1]} x {i[2]} (Precio Unitario: {i[3]})")

#--------------------
#---EXPORTES EXCEL---
#--------------------

def exportar_ventas_excel():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT
                    v.fecha,
                    p.nombre,
                    v.cantidad,
                    v.precio_unitario,
                    v,total
                    FROM ventas v
                    JOIN productos p ON v.producto_id = p.id
                    ORDER BY v.fecha
                    """)
        with open(Ventas_csv_path, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
            writer = csv.writer(archivo) #creamos el archivo csv
            writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario", "Total"]) #Escribe una fila en el archivo CSV. (encabezado)
            writer.writerows(cur.fetchall()) #Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

        print(" Archivo ventas.csv generado (abrir con Excel)")

def exportar_stock_excel():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT nombre, PRECIO, stock
                    FROM productos
                    ORDER BY nombre
                    """)
        with open(Stock_csv_path, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
            writer = csv.writer(archivo) #creamos el archivo csv
            writer.writerow(["Producto", "Precio", "Stock"]) #Escribe una fila en el archivo CSV. (encabezado)
            writer.writerows(cur.fetchall()) #Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

        print("Archivo stock.csv generado (abrir con Excel)")


def exportar_altas_excel(): 
    with open_connect() as con:
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

    with open(Altas_csv_path, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
        writer = csv.writer(archivo) #creamos el archivo csv
        writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario"]) #Escribe una fila en el archivo CSV. (encabezado)
        writer.writerows(cur.fetchall()) #Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

    print(" Archivo altas.csv generado (abrir con Excel)")

def exportar_resumen_dia():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM resumen_dia")
        datos = cur.fetchall()

# ----------------------------
#--- EXPORTAR TODO EXCEL  ----
# ----------------------------

def exportar_todo_excel(): #funcion para exportar todos los archivos csv 
    with open_connect() as con: #nos conectamos DB donde se eucuentra ubicado el archivo 
    #solo llamamos todas las funciones creadas para exportar archivos csv
        exportar_ventas_excel()
        exportar_stock_excel()
        exportar_altas_excel()
        actualizar_resumen()
        exportar_todo_resumen()
        print(" Todos los archivos fueron exportados")

#----------------------------
#--- EXPORTACION LOOP -------
#----------------------------
def exportar_todo_resumen():
    # Cada elemento es una tupla de 2 valores
    tablas = [
        ("resumen_dia", "resumen_dia.csv"),
        ("resumen_semana", "resumen_semana.csv"),
        ("resumen_mes", "resumen_mes.csv"),
        ("resumen_anio", "resumen_anio.csv")
    ]
    #conectas a la DB
    with open_connect() as con:
        cur = con.cursor() #variable para ejecutar comandos sql
        #for desempaqueta autamaticamente cada tupla
        for nombre_tabla, nombre_archivo in tablas:

            cur.execute(f"SELECT * FROM {nombre_tabla}") #ejecutamos sql y usamos plantilla para pasar el nombre de la tabla
            datos = cur.fetchall() #guardamos la consulta en una variable llamada datos con fetchall
            #abrimos archivo con with
            with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)

                #Encabezados automaticos
                columnas = [descripcion[0] for descripcion in cur.description]
                writer.writerow(columnas)

                writer.writerows(datos)

                print(f"{nombre_archivo} Exportado Correctamente.")


#-------------------------
#--- RESUMEN DE VENTAS ---
#-------------------------

def actualizar_resumen():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("DELETE FROM resumen_dia")
        cur.execute("""
            INSERT INTO resumen_dia (fecha, producto_id, cantidad_total, ingreso_total)
            SELECT DATE(fecha), producto_id, SUM(cantidad), SUM(total)
            FROM ventas
             GROUP BY DATE(fecha), producto_id
                    """)
        cur.execute("DELETE FROM resumen_semana")    
        cur.execute("""
        INSERT INTO resumen_semana (anio_semana, producto_id, cantidad_total, ingreso_total)
                    SELECT strftime('%Y-%W', fecha), producto_id, SUM(cantidad), SUM(total)
                    FROM ventas
                    GROUP BY strftime('%Y-%W', fecha), producto_id
                    """)
        cur.execute("DELETE FROM resumen_mes")
        cur.execute("""
        INSERT INTO resumen_mes (anio_mes, producto_id, cantidad_total, ingreso_total)
                    SELECT strftime('%Y-%m', fecha), producto_id, SUM(cantidad), SUM(total)
                    FROM ventas
                    GROUP BY strftime('%Y-%m', fecha), producto_id
                    """)
        cur.execute("DELETE FROM resumen_anio")
        cur.execute("""
        INSERT INTO resumen_anio (anio, producto_id, cantidad_total, ingreso_total)
                    SELECT strftime('%Y', fecha), producto_id, SUM(cantidad), SUM(total)
                    FROM ventas
                    GROUP BY strftime('%Y', frcha), producto_id
                    """)
        con.commit()
        print("Rsumen Actualizado Correctamente")


main()