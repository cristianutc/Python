from datetime import datetime
import sqlite3
from assets.db import open_connect
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
import tkinter as tk
from pathlib import Path
import csv
import os
from tkinter import ttk
from db import export_dir

APP_NAME = "MiTienda"

base_dir = os.path.join(os.environ["LOCALAPPDATA"], APP_NAME)
db_dir = os.path.join(base_dir, "DB")
export_dir = os.path.join(base_dir, "Archivos_Excel")

os.makedirs(db_dir, exist_ok=True)
os.makedirs(export_dir, exist_ok=True)

ventas_csv = Path(export_dir) / "ventas.csv"
stock_csv = Path(export_dir) / "stock.csv"
altas_csv = Path(export_dir) / "altas.csv"
merma_csv = Path(export_dir) / "merma.csv"

#Verificar si la carpeta Aerchivos_Excel existe, si no crearla
if not os.path.exists(export_dir):
    os.makedirs(export_dir)
    print(f"Carpeta {export_dir} Creada.")

def cargar_productos():
    """Carga los productos de la base de datos."""
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

def agregar_al_carrito(carrito, producto, cantidad):
    """Agrega un producto al carrito"""
    subtotal = producto['precio'] * cantidad  # Precio * Cantidad
    carrito.append({"id": producto[0], "nombre": producto[1], "cantidad": cantidad, "precio": producto[2], "subtotal": subtotal})
    return carrito

def registrar_venta(carrito):
    """Registra la venta en la base de datos y actualiza el stock"""
    with open_connect() as con:
        cur = con.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for item in carrito:
            cur.execute("""
            INSERT INTO ventas (fecha, producto_id, cantidad, precio_unitario, total)
            VALUES (?, ?, ?, ?, ?)
            """, (fecha, item['id'], item['cantidad'], item['precio'], item['subtotal']))
            
            # Actualizar stock del producto
            cur.execute("""
            UPDATE productos
            SET stock = stock - ?
            WHERE id = ?
            """, (item['cantidad'], item['id']))

        con.commit()

def registrar_alta(producto_id, cantidad, precio_unitario):
    with open_connect() as con:
        cur = con.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d  %H:%M:%S:")
        cur.execute("""
        INSERT INTO altas (fecha, producto_id, cantidad, precio_unitario)
                    VALUES (?, ?, ?, ?)
                    """, (fecha, producto_id, cantidad, precio_unitario))
        con.commit()
def registrar_merma(producto_id, cantidad, motivo):
    with open_connect() as con:
        cur = con.cursor()
        fecha = datetime.now().strftime("%Y-%m-%d  %H:%M:%S:")
        cur.execute("""
        INSERT INTO merma (fecha, producto_id, cantidad, motivo)
                    VALUES (?, ?, ?, ?)
                    """, (fecha, producto_id, cantidad, motivo))
        con.commit()

#------------------------
#---Funciones del Menu---
#------------------------
def ver_productos():
    """Función que devuelve los productos o un mensaje si no hay productos."""
    productos = cargar_productos()
    if not productos:
        return None  # Si no hay productos, retornamos None
    return productos

def agregar_productos_dialog(root):
    """Función para agregar productos usando cuadros de diálogo en lugar de consola"""

    # Pedir nombre
    nombre = simpledialog.askstring("Agregar Producto", "Nombre del Producto:", parent=root)
    if not nombre:
        return  # Si cancela o no ingresa nada, salir
    nombre = nombre.lower()

    # Pedir cantidad
    try:
        cantidad = simpledialog.askinteger("Agregar Producto", "Cantidad a Ingresar:", parent=root, minvalue=1)
        if cantidad is None:
            return
    except Exception:
        messagebox.showerror("Error", "Cantidad inválida")
        return

    # Pedir precio
    try:
        precio = simpledialog.askfloat("Agregar Producto", "Precio Unitario:", parent=root, minvalue=0.0)
        if precio is None:
            return
    except Exception:
        messagebox.showerror("Error", "Precio inválido")
        return

    # Revisar si el producto ya existe
    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            guardar_producto(nombre, precio, p["stock"] + cantidad)  # Actualiza stock y precio
            registrar_alta(p["id"], cantidad, precio)
            messagebox.showinfo("Agregar Producto", "Stock Actualizado.")
            return

    # Si es un producto nuevo
    guardar_producto(nombre, precio, cantidad)
    productos = cargar_productos()
    for p in productos:
        if p["nombre"] == nombre:
            registrar_alta(p["id"], cantidad, precio)
            break
    messagebox.showinfo("Agregar Producto", "Producto Agregado Exitosamente")


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

        producto = productos[op - 1]
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad Invalida")
            continue

        if cantidad > producto["stock"]:
            print("No hay suficiente stock")
            continue

        carrito.append({"id": producto["id"], "nombre": producto["nombre"], "cantidad": cantidad, "precio": producto["precio"]})

    if not carrito:
        print("No Selecciono Ningun Producto.")
        return None
    
    print("===== RESUMEN DE COMPRA =====")
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total_general += subtotal
        print(f"{item['nombre']} x {item['cantidad']} = ${subtotal}")

    confimar = input(f"Total a Pagar: ${total_general}. \n Confirmar Compra (s/n): ").lower()

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

def generar_ticket(carrito):
    print("\t ===== TICKET =====")
    total = 0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['precio']} x {item['cantidad']} = ${subtotal}")
    print(f"TOTAL A PAGAR: ${total}")
    print("=========================")


def buscar_productos_dialog(root):
    nombre = simpledialog.askstring("Buscar Producto", "Ingrese el nombre a buscar:", parent=root)
    if not nombre:
        return

    nombre = nombre.lower()
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("SELECT id, nombre, precio, stock FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
        resultados = cur.fetchall()
        if not resultados:
            messagebox.showinfo("Resultados", "No se encontraron productos.")
            return

    # Mostrar resultados en un mensaje
    mensaje = "Resultados encontrados:\n\n"
    for i in resultados:
        mensaje += f"{i[0]}. {i[1]} - ${i[2]:.2f} (Stock {i[3]})\n"
    
    messagebox.showinfo("Resultados", mensaje)

def eliminar_producto_dialog(root):
    """
    Función completa para eliminar un producto parcial o totalmente,
    registrando correctamente la merma en cada operación.
    """
    # 1 Pedir nombre del producto
    nombre = simpledialog.askstring(
        "Eliminar Producto",
        "Ingrese el nombre del producto a eliminar:",
        parent=root
    )

    if not nombre:
        return  # Canceló

    nombre = nombre.lower()
    productos = cargar_productos()  # Cargar productos con stock actual

    # 2 Buscar el producto
    for p in productos:
        if p["nombre"] == nombre:

            stock_actual = p["stock"]
            if stock_actual == 0:
                messagebox.showerror("Error", "El producto no tiene stock disponible.")
                return

            # 3 Pedir cantidad a eliminar
            cantidad_eliminar = simpledialog.askinteger(
                "Cantidad a eliminar",
                f"Stock disponible: {stock_actual}\n"
                f"Ingrese la cantidad a eliminar (1-{stock_actual}):",
                parent=root,
                minvalue=1,
                maxvalue=stock_actual
            )

            if not cantidad_eliminar:
                return  # Canceló

            # 4 Pedir motivo
            motivo = simpledialog.askstring(
                "Motivo de eliminación",
                "Ingrese el motivo de la eliminación (ej: caducado, defectuoso, etc.):",
                parent=root
            )

            if not motivo:
                return  # Canceló

            # 5 Actualizar stock o eliminar producto si se agota
            with open_connect() as con:
                cur = con.cursor()
                if cantidad_eliminar >= stock_actual:
                    # Se elimina todo el producto
                    cur.execute("DELETE FROM productos WHERE id = ?", (p["id"],))
                else:
                    # Reducir stock parcial
                    cur.execute(
                        "UPDATE productos SET stock = stock - ? WHERE id = ?",
                        (cantidad_eliminar, p["id"])
                    )
                con.commit()

            # 6 Registrar merma con la cantidad exacta eliminada
            registrar_merma(
                producto_id=p["id"],
                cantidad=cantidad_eliminar,
                motivo=motivo
            )

            # 7 Mensaje de éxito
            messagebox.showinfo(
                "Eliminación Exitosa",
                f"Producto '{nombre}' procesado correctamente.\n"
                f"Cantidad eliminada: {cantidad_eliminar}\n"
                f"Motivo: {motivo}\n"
                f"Stock restante: {max(0, stock_actual - cantidad_eliminar)}"
            )
            return

    # Si no se encuentra el producto
    messagebox.showerror("Error", "Producto no encontrado.")


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
                    GROUP BY strftime('%Y', fecha), producto_id
                    """)
        con.commit()
        print("Rsumen Actualizado Correctamente")

def reporte_stock(root):
    productos = cargar_productos()  # Correcto: Llamada de la función
    if not productos:
        messagebox.showinfo("Stock", "No hay productos registrados.")
        return

    reporte = "===== REPORTE DE STOCK =====\n\n"
    for p in productos:
        reporte += f"{p['nombre']} - Stock: {p['stock']}\n"

    # Mostrar el reporte en un cuadro de mensaje
    messagebox.showinfo("Reporte de Stock", reporte)


def reporte_ventas(root):
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT p.nombre, SUM(v.cantidad) as total_vendido, SUM(v.total) as total_recaudado
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        GROUP BY p.nombre
        """)
        rows = cur.fetchall()

        if not rows:
            messagebox.showinfo("Ventas", "No hay ventas registradas.")
            return

        reporte = "===== REPORTE DE VENTAS POR PRODUCTO =====\n\n"
        for i in rows:
            reporte += f"{i[0]} - Cantidad Vendida: {i[1]} - Total Recaudado: ${i[2]:.2f}\n"

        # Mostrar el reporte en un cuadro de mensaje
        messagebox.showinfo("Reporte de Ventas", reporte)


def reporte_ventas_fecha(root):
    # Pedir fechas al usuario
    desde = simpledialog.askstring("Fecha Desde", "Ingrese la fecha de inicio (YYYY-MM-DD):", parent=root)
    hasta = simpledialog.askstring("Fecha Hasta", "Ingrese la fecha final (YYYY-MM-DD):", parent=root)

    if not desde or not hasta:
        messagebox.showerror("Error", "Las fechas son necesarias para el reporte.")
        return

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

        if not rows:
            messagebox.showinfo("Ventas", f"No hay ventas entre las fechas {desde} y {hasta}.")
            return

        reporte = f"===== REPORTE DE VENTAS DESDE {desde} HASTA {hasta} =====\n\n"
        for i in rows:
            reporte += f"{i[0]} - Cantidad Vendida: {i[1]} - Total Recaudado: ${i[2]:.2f}\n"

        # Mostrar el reporte en un cuadro de mensaje
        messagebox.showinfo("Reporte de Ventas por Fecha", reporte)


def historial_completo(root):
    historial = "===== HISTORIAL COMPLETO =====\n\n"

    with open_connect() as con:
        cur = con.cursor()

        # Historial de ventas
        historial += "===== HISTORIAL DE VENTAS =====\n\n"
        cur.execute("""
        SELECT v.fecha, p.nombre, v.cantidad, v.precio_unitario, v.total
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        ORDER BY v.fecha
        """)
        ventas = cur.fetchall()
        for v in ventas:
            historial += f"{v[0]} | {v[1]} x {v[2]} = ${v[4]} (Precio unitario: {v[3]})\n"

        # Historial de altas
        historial += "\n===== HISTORIAL DE ALTAS =====\n\n"
        cur.execute("""
        SELECT a.fecha, p.nombre, a.cantidad, a.precio_unitario
        FROM altas a
        JOIN productos p ON a.producto_id = p.id
        ORDER BY a.fecha
        """)
        altas = cur.fetchall()
        for a in altas:
            historial += f"{a[0]} | {a[1]} x {a[2]} (Precio Unitario: {a[3]})\n"

    # Mostrar el historial completo en un cuadro de mensaje
    messagebox.showinfo("Historial Completo", historial)

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
                    v.total
                    FROM ventas v
                    JOIN productos p ON v.producto_id = p.id
                    ORDER BY v.fecha
                    """)
        with open(ventas_csv, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
            writer = csv.writer(archivo) #creamos el archivo csv
            writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario", "Total"]) #Escribe una fila en el archivo CSV. (encabezado)
            writer.writerows(cur.fetchall()) #Recupera todos los resultados de la consulta SQL ejecutada previamente (la consulta SELECT).

        print(" Archivo ventas.csv generado (abrir con Excel)")

def exportar_stock_excel():
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT nombre AS producto, precio, stock
                    FROM productos
                    ORDER BY nombre
                    """)
        with open(stock_csv, "w", newline="", encoding="utf-8") as archivo: #se abre archivo de manera controlada
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
                p.nombre AS producto,
                a.cantidad,
                a.precio_unitario
            FROM altas a
            JOIN productos p ON a.producto_id = p.id
            ORDER BY a.fecha
        """)

        with open(altas_csv, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Fecha", "Producto", "Cantidad", "Precio Unitario"])
            writer.writerows(cur.fetchall())

    print("Archivo altas.csv generado (abrir con Excel)")

def exportar_merma_excel():
    """Exporta la tabla de merma a CSV (para abrir en Excel)"""
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT 
                m.fecha,
                p.nombre AS producto,
                m.cantidad,
                m.motivo
            FROM merma m
            JOIN productos p ON m.producto_id = p.id
            ORDER BY m.fecha
        """)

        # Usamos tu path ya definido, por ejemplo:
        with open(merma_csv, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Fecha", "Producto", "Cantidad", "Motivo"])
            writer.writerows(cur.fetchall())

    print("Archivo merma.csv generado (abrir con Excel)")

# Rutas de exportación

Resumen_dia_csv_path = Path(export_dir) / "resumen_dia.csv"
Resumen_semana_csv_path = Path(export_dir) / "resumen_semana.csv"
Resumen_mes_csv_path = Path(export_dir) / "resumen_mes.csv"
Resumen_anio_csv_path = Path(export_dir) / "resumen_anio.csv"


def mostrar_resumen_ventas(root):
    """Ventana de Resumen de Ventas interactiva con menú desplegable para productos"""
    resumen_win = tk.Toplevel(root)
    resumen_win.title("Resumen de Ventas")
    resumen_win.geometry("1000x650")

    # --- Frame superior: botones de periodo ---
    frame_botones = tk.Frame(resumen_win)
    frame_botones.pack(pady=10)

    periodo = tk.StringVar(value="resumen_dia")

    def mostrar_periodo(tabla):
        periodo.set(tabla)
        cargar_tabla(tabla)

    for texto, tabla in [("Día", "resumen_dia"),
                         ("Semana", "resumen_semana"),
                         ("Mes", "resumen_mes"),
                         ("Año", "resumen_anio")]:
        tk.Button(frame_botones, text=texto, width=12,
                  command=lambda t=tabla: mostrar_periodo(t)).pack(side="left", padx=5)

    # --- Treeview ---
    columnas = ("Producto", "Cantidad", "Ingreso")
    tree = ttk.Treeview(resumen_win, columns=columnas, show="headings")
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=250)
    tree.pack(expand=True, fill="both", pady=10)

    # --- Frame inferior ---
    frame_destacados = tk.Frame(resumen_win)
    frame_destacados.pack(pady=10, fill="x")

    lbl_destacados = tk.Label(frame_destacados, text="Productos Destacados", font=("Arial", 12, "bold"))
    lbl_destacados.pack()

    txt_destacados = tk.Text(frame_destacados, height=10)
    txt_destacados.pack(expand=False, fill="x")

    # --- Función para cargar tabla ---
    def cargar_tabla(tabla):
        # Limpiar
        for i in tree.get_children():
            tree.delete(i)
        txt_destacados.delete("1.0", tk.END)

        with open_connect() as con:
            cur = con.cursor()
            cur.execute(f"""
                SELECT r.*, p.nombre, p.precio
                FROM {tabla} r
                JOIN productos p ON r.producto_id = p.id
            """)
            filas = cur.fetchall()

        for f in filas:
            tree.insert("", "end", values=(f[-2], f[2], f[3]))  # nombre, cantidad_total, ingreso_total

        if not filas:
            return

        # --- Productos por cantidad ---
        filas_cantidad = sorted(filas, key=lambda x: x[2], reverse=True)
        max_vendido = filas_cantidad[0][2]
        min_vendido = filas_cantidad[-1][2]

        productos_mas_vendido = [f[-2] for f in filas_cantidad if f[2] == max_vendido]
        productos_menos_vendido = [f[-2] for f in filas_cantidad if f[2] == min_vendido]
        productos_intermedio_vendido = [f[-2] for f in filas_cantidad[len(filas_cantidad)//2:len(filas_cantidad)//2+1]]

        # --- Productos por precio ---
        filas_precio = sorted(filas, key=lambda x: x[-1], reverse=True)
        max_precio = filas_precio[0][-1]
        min_precio = filas_precio[-1][-1]

        productos_mas_caro = [f[-2] for f in filas_precio if f[-1] == max_precio]
        productos_menos_caro = [f[-2] for f in filas_precio if f[-1] == min_precio]
        productos_intermedio_caro = [f[-2] for f in filas_precio[len(filas_precio)//2:len(filas_precio)//2+1]]

        # --- Mostrar en caja de texto ---
        txt_destacados.insert("end", "Filtrar por cantidad:\n")
        txt_destacados.insert("end", f"  Más vendido: {', '.join(productos_mas_vendido)}\n")
        txt_destacados.insert("end", f"  Menos vendido: {', '.join(productos_menos_vendido)}\n")
        txt_destacados.insert("end", f"  Intermedio: {', '.join(productos_intermedio_vendido)}\n\n")

        txt_destacados.insert("end", "Filtrar por precio:\n")
        txt_destacados.insert("end", f"  Más caro: {', '.join(productos_mas_caro)}\n")
        txt_destacados.insert("end", f"  Menos caro: {', '.join(productos_menos_caro)}\n")
        txt_destacados.insert("end", f"  Intermedio: {', '.join(productos_intermedio_caro)}\n")

        # --- Menú desplegable por categoría ---
        for widget in frame_destacados.pack_slaves():
            if isinstance(widget, tk.Menubutton):
                widget.destroy()

        categorias = {
            "Más vendido": productos_mas_vendido,
            "Menos vendido": productos_menos_vendido,
            "Intermedio vendido": productos_intermedio_vendido,
            "Más caro": productos_mas_caro,
            "Menos caro": productos_menos_caro,
            "Intermedio caro": productos_intermedio_caro
        }

        for nombre_categoria, lista_productos in categorias.items():
            if not lista_productos:
                continue
            menubtn = tk.Menubutton(frame_destacados, text=nombre_categoria, width=15, relief="raised")
            menubtn.menu = tk.Menu(menubtn, tearoff=0)
            menubtn["menu"] = menubtn.menu
            for producto in lista_productos:
                menubtn.menu.add_command(label=producto, command=lambda p=producto: filtrar_producto(p))
            menubtn.pack(side="left", padx=5, pady=5)

    # --- Función para filtrar Treeview ---
    def filtrar_producto(nombre_producto):
        for i in tree.get_children():
            tree.delete(i)
        tabla_actual = periodo.get()
        with open_connect() as con:
            cur = con.cursor()
            cur.execute(f"""
                SELECT r.*, p.nombre
                FROM {tabla_actual} r
                JOIN productos p ON r.producto_id = p.id
                WHERE p.nombre = ?
            """, (nombre_producto,))
            filas = cur.fetchall()
        for f in filas:
            tree.insert("", "end", values=(f[-1], f[2], f[3]))

    # --- Botón exportar ---
    def exportar_resumen():
        tablas = [
            ("resumen_dia", Resumen_dia_csv_path),
            ("resumen_semana", Resumen_semana_csv_path),
            ("resumen_mes", Resumen_mes_csv_path),
            ("resumen_anio", Resumen_anio_csv_path)
        ]
        with open_connect() as con:
            cur = con.cursor()
            for nombre_tabla, ruta_archivo in tablas:
                cur.execute(f"""
                    SELECT r.*, p.nombre
                    FROM {nombre_tabla} r
                    JOIN productos p ON r.producto_id = p.id
                """)
                datos = cur.fetchall()
                with open(ruta_archivo, "w", newline="", encoding="utf-8") as archivo:
                    writer = csv.writer(archivo)
                    columnas = [descripcion[0] for descripcion in cur.description]
                    writer.writerow(columnas)
                    writer.writerows(datos)
        messagebox.showinfo("Exportar Resumen", "Todos los resúmenes exportados correctamente en 'Archivos Excel'")

    tk.Button(resumen_win, text="Exportar Resumen a Excel", command=exportar_resumen, width=30).pack(pady=5)

    # --- Cargar datos inicial ---
    cargar_tabla("resumen_dia")
