import tkinter as tk
from db import export_dir
from tkinter import messagebox
from assets.db import open_connect
import bcrypt
from assets.ventas import ver_productos
from assets.ventas import agregar_productos_dialog
from assets.ventas import cargar_productos, registrar_venta
import tkinter.simpledialog as simpledialog
from assets.ventas import buscar_productos_dialog
from assets.ventas import eliminar_producto_dialog
from assets.ventas import reporte_stock, reporte_ventas, reporte_ventas_fecha, historial_completo
from assets.ventas import (
    exportar_ventas_excel,
    exportar_stock_excel,
    exportar_altas_excel,
    exportar_merma_excel
)
from assets.ventas import (
    mostrar_resumen_ventas,
    actualizar_resumen
)



# ------------------ FUNCIONES DE AUTENTICACIÓN ------------------

# ---Generar hash---
def has_password(password):
    salt = bcrypt.gensalt()  # Genera un "salt" único para cada Contraseña
    return bcrypt.hashpw(password.encode(), salt).decode()  # Devuelve el hash codificado a texto

# Verificamos la Contraseña
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())  # Comparamos el hash con la contraseña ingresada

# Función de Registro
def registrar_usuario(nombre, edad, correo, password):
    with open_connect() as con:
        cur = con.cursor()

        # Verificamos si el correo ya Existe
        cur.execute("""
        SELECT * FROM usuarios WHERE correo_electronico = ?
                    """, (correo,))
        if cur.fetchone():
            return "Este Correo ya esta Registrado."
        
        password_hash = has_password(password)  # Generamos el hash de la Contraseña

        try:
            cur.execute("""
            INSERT INTO usuarios (nombre, edad, correo_electronico, password)
                        VALUES(?, ?, ?, ?)
                    """, (nombre, edad, correo, password_hash))
            con.commit()
            return "Usuario Registrado Exitosamente"
        except Exception as e:
            return f"Error al Registrar el Usuario: {e}"

# Función de Login
def login(correo, password):
    with open_connect() as con:
        cur = con.cursor()

        cur.execute("""
        SELECT * FROM usuarios WHERE correo_electronico = ?
        """, (correo,))

        usuario = cur.fetchone()

        if usuario:
            if check_password(password, usuario[4]):
                return "Login Exitoso"
            else:
                return "Contraseña Incorrecta"
        else:
            return "Usuario no Encontrado"


# ------------------ VENTANA DE LOGIN ------------------
def mostrar_ventana_login(root):
    """Muestra la ventana de login donde el usuario puede acceder o registrarse."""
    login_win = tk.Toplevel(root)
    login_win.title("Login")
    login_win.geometry("400x400")

    def intentar_login():
        correo = entry_correo.get()
        password = entry_password.get()
        
        resultado = login(correo, password)
        if resultado == "Login Exitoso":
            messagebox.showinfo("Login Exitoso", "Bienvenido al sistema")
            login_win.destroy()  # Cierra la ventana de login
            mostrar_menu_principal(root)  # Muestra el menú principal
        else:
            messagebox.showerror("Error", resultado)

    def registrar_usuario_ventana():
        """Abre la ventana de registro"""
        login_win.withdraw()  # Oculta la ventana de login

        def registrar():
            nombre = entry_nombre.get()
            edad = entry_edad.get()
            correo = entry_correo_reg.get()
            password = entry_password_reg.get()

            resultado = registrar_usuario(nombre, edad, correo, password)
            messagebox.showinfo("Registro", resultado)
            if "Exitosamente" in resultado:
                login_win.deiconify()  # Muestra la ventana de login nuevamente
                register_win.destroy()

        # Ventana de Registro
        register_win = tk.Toplevel(login_win)
        register_win.title("Registrar Usuario")
        register_win.geometry("400x400")

        tk.Label(register_win, text="Nombre:").pack()
        entry_nombre = tk.Entry(register_win)
        entry_nombre.pack()

        tk.Label(register_win, text="Edad:").pack()
        entry_edad = tk.Entry(register_win)
        entry_edad.pack()

        tk.Label(register_win, text="Correo Electrónico:").pack()
        entry_correo_reg = tk.Entry(register_win)
        entry_correo_reg.pack()

        tk.Label(register_win, text="Contraseña:").pack()
        entry_password_reg = tk.Entry(register_win, show="*")
        entry_password_reg.pack()

        tk.Button(register_win, text="Registrar", command=registrar).pack()

    # Ventana de Login
    tk.Label(login_win, text="Correo Electrónico:").pack()
    entry_correo = tk.Entry(login_win)
    entry_correo.pack()

    tk.Label(login_win, text="Contraseña:").pack()
    entry_password = tk.Entry(login_win, show="*")
    entry_password.pack()

    tk.Button(login_win, text="Iniciar Sesión", command=intentar_login).pack()
    tk.Button(login_win, text="¿No tienes cuenta? Regístrate", command=registrar_usuario_ventana).pack()


# ------------------ VENTANA PRINCIPAL ------------------
def mostrar_menu_principal(root):
    """Muestra la ventana principal con todas las opciones del sistema"""
    menu_win = tk.Toplevel(root)
    menu_win.title("Menú Principal")
    menu_win.geometry("400x400")

    def ver_productos_func():
        """Función para abrir la ventana que muestra los productos"""
        productos = ver_productos()  # Llamamos a la función que obtiene los productos de la DB

        if productos is None:
            messagebox.showinfo("Productos", "No hay productos disponibles.")
        else:
            # Crear la ventana de productos
            ver_win = tk.Toplevel(menu_win)
            ver_win.title("Productos Disponibles")
            ver_win.geometry("400x300")
            
            # Usamos un widget Text para mostrar los productos
            text_area = tk.Text(ver_win, width=50, height=15)
            text_area.pack(pady=10)

            # Insertamos los productos en el widget Text
            text_area.insert(tk.END, "====== PRODUCTOS =======\n\n")
            for p in productos:
                text_area.insert(tk.END, f"{p['id']}. {p['nombre']} - ${p['precio']:.2f} (Stock: {p['stock']})\n")
            
            text_area.config(state=tk.DISABLED)  # Hacer solo lectura

            # Botón de Cerrar
            button_close = tk.Button(ver_win, text="Cerrar", command=ver_win.destroy)
            button_close.pack(pady=10)

    def vender_productos():
        mostrar_ventana_ventas(menu_win)  # Llama la ventana de ventas


    def buscar_producto():
        buscar_productos_dialog(menu_win)  # Llamamos a la función de búsqueda de productos

    def agregar_producto():
        """Llama la función para agregar productos mediante cuadros de diálogo"""
        agregar_productos_dialog(root)  # Llama la función que muestra los cuadros de diálogo

    def eliminar_producto():
        """Llama la función para eliminar productos mediante cuadros de diálogo"""
        eliminar_producto_dialog(menu_win)  # Llama a la función que muestra el cuadro de diálogo



    def menu_reportes():
        menu_win.withdraw()  # OCULTAMOS, no destruimos
        mostrar_menu_reportes(menu_win) # Pasamos la ventana actual

    # Botones del menú principal
    botones = [
    ("Ver productos", ver_productos_func),
    ("Vender Productos", vender_productos),
    ("Buscar Producto", buscar_producto),
    ("Agregar Producto", lambda: agregar_producto()),
    ("Eliminar Producto", eliminar_producto),
    ("Resumen de Ventas", lambda: [actualizar_resumen(), mostrar_resumen_ventas(menu_win)]),  # <-- NUEVO BOTÓN
    ("Menu de Reportes", menu_reportes),
    ("Salir del Programa", menu_win.destroy)
]

    for texto, funcion in botones:
        tk.Button(menu_win, text=texto, width=30, command=funcion).pack(pady=5)

# ------------------ VENTANA DE VENTAS ------------------
def mostrar_ventana_ventas(root):
    """Ventana para gestionar las ventas de productos"""
    ventas_win = tk.Toplevel(root)
    ventas_win.title("Vender Producto")
    ventas_win.geometry("600x400")

    productos = cargar_productos()  # Aquí cargas los productos de la base de datos
    if not productos:
        messagebox.showinfo("Error", "No hay productos disponibles.")
        ventas_win.destroy()
        return

    carrito = []
    total_general = 0

    frame = tk.Frame(ventas_win)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Subframe para seleccionar producto
    product_frame = tk.Frame(frame)
    product_frame.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    tk.Label(product_frame, text="Selecciona producto:").pack(side="top", anchor="e", padx=5, pady=5)
    product_var = tk.StringVar(ventas_win)
    product_choices = [f"{p['id']}. {p['nombre']} - ${p['precio']} - Stock: {p['stock']}" for p in productos]
    product_var.set(product_choices[0])
    product_menu = tk.OptionMenu(product_frame, product_var, *product_choices)
    product_menu.pack(side="top", anchor="e", pady=5)

    # Subframe para la cantidad y agregar al carrito
    cantidad_frame = tk.Frame(frame)
    cantidad_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    tk.Label(cantidad_frame, text="Cantidad:").pack(side="left", padx=5)
    cantidad_entry = tk.Entry(cantidad_frame, width=5)
    cantidad_entry.pack(side="left", padx=5)

    def agregar_al_carrito_handler():
        nonlocal total_general
        producto_seleccionado = product_var.get()
        producto_id = int(producto_seleccionado.split(".")[0])
        producto = next((p for p in productos if p['id'] == producto_id), None)

        if producto:
            try:
                cantidad = int(cantidad_entry.get())
                if cantidad > producto["stock"]:
                    messagebox.showerror("Error", "No hay suficiente stock.")
                    return
                subtotal = producto["precio"] * cantidad
                carrito.append({"id": producto["id"], "nombre": producto["nombre"], "cantidad": cantidad, "precio": producto["precio"], "subtotal": subtotal})
                total_general += subtotal
                total_label.config(text=f"Total: ${total_general}")
                carrito_listbox.insert(tk.END, f"{producto['nombre']} x {cantidad} = ${subtotal:.2f}")
                
                # Limpiar la caja de texto de cantidad después de agregar al carrito
                cantidad_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Cantidad no válida.")

    agregar_button = tk.Button(cantidad_frame, text="Agregar", command=agregar_al_carrito_handler)
    agregar_button.pack(side="left", padx=5)

    # Subframe para carrito y total
    carrito_frame = tk.Frame(frame)
    carrito_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    carrito_listbox = tk.Listbox(carrito_frame, height=6, width=40)
    carrito_listbox.pack(side="left", fill="y")
    total_label = tk.Label(carrito_frame, text=f"Total: ${total_general:.2f}")
    total_label.pack(side="left", pady=5)

    # **Botón para eliminar producto del carrito**
    def eliminar_del_carrito():
        nonlocal total_general
        try:
            selected_index = carrito_listbox.curselection()[0]
            item_text = carrito_listbox.get(selected_index)
            producto_nombre = item_text.split(" x ")[0]
            item = next(i for i in carrito if i['nombre'] == producto_nombre)
            carrito.remove(item)
            total_general -= item['subtotal']  # Usamos subtotal para restar el total
            total_label.config(text=f"Total: ${total_general:.2f}")
            carrito_listbox.delete(selected_index)  # Eliminar la línea del Listbox
        except IndexError:
            messagebox.showerror("Error", "Selecciona un producto para eliminar.")

    # **Botones de pagar, eliminar y cancelar en el mismo frame**
    buttons_frame = tk.Frame(frame)
    buttons_frame.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    # Botón Pagar
    def realizar_pago():
        nonlocal total_general
        if not carrito:
            messagebox.showerror("Error", "No has agregado productos al carrito.")
            return
        pago = simpledialog.askfloat("Pago", f"Total a pagar: ${total_general}. ¿Cuánto pagas?", parent=ventas_win)
        if pago is None: return
        if pago < total_general:
            messagebox.showerror("Error", "El pago es insuficiente.")
            return
        cambio = pago - total_general
        messagebox.showinfo("Cambio", f"Pago recibido: ${pago}. Cambio: ${cambio}. Venta completada.")
        registrar_venta(carrito)  # Registrar la venta en la base de datos
        

    pagar_button = tk.Button(buttons_frame, text="Pagar", command=realizar_pago)
    pagar_button.pack(side="left", padx=5)

    # Botón Eliminar
    eliminar_button = tk.Button(buttons_frame, text="Eliminar", command=eliminar_del_carrito)
    eliminar_button.pack(side="left", padx=5)

    # Botón Cancelar
    cancelar_button = tk.Button(buttons_frame, text="Cancelar", command=ventas_win.destroy)
    cancelar_button.pack(side="left", padx=5)



def cargar_productos():
    """Carga los productos de la base de datos"""
    with open_connect() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM productos")
        productos = cur.fetchall()

    return [{"id": p[0], "nombre": p[1], "precio": p[2], "stock": p[3]} for p in productos]


# ------------------ VENTANA DE REPORTES ------------------
def mostrar_menu_reportes(root):
    """Ventana con las opciones de reportes"""
    reportes_win = tk.Toplevel(root)
    reportes_win.title("Reportes")
    reportes_win.geometry("400x400")

    # Botón para mostrar el reporte de stock
    def abrir_reporte_stock():
        reporte_stock(root)  # Llama a la función reporte_stock
    
    # Botón para mostrar el reporte de ventas
    def abrir_reporte_ventas():
        reporte_ventas(root)  # Llama a la función reporte_ventas
    
    # Botón para mostrar el reporte de ventas por fecha
    def abrir_reporte_ventas_fecha():
        reporte_ventas_fecha(root)  # Llama a la función reporte_ventas_fecha
    
    # Botón para mostrar el historial completo
    def abrir_historial_completo():
        historial_completo(root)  # Llama a la función historial_completo

    def menu_excel():
        reportes_win.destroy()  # Cerramos la ventana de reportes
        mostrar_menu_excel(root)

    def regresar():
        reportes_win.destroy()  # Cerramos la ventana de reportes
        root.deiconify()  # Mostramos la ventana principal nuevamente

    # Botones del menú de reportes
    botones = [
        ("Reporte de Stock", abrir_reporte_stock),
        ("Reporte de ventas totales", abrir_reporte_ventas),
        ("Reporte de ventas por fechas", abrir_reporte_ventas_fecha),
        ("Historial Completo", abrir_historial_completo),
        ("Menu Exportar a Excel", menu_excel),
        ("Regresar", regresar)
    ]

    for texto, funcion in botones:
        tk.Button(reportes_win, text=texto, width=30, command=funcion).pack(pady=5)


# ------------------ VENTANA DE EXPORTAR A EXCEL ------------------
def mostrar_menu_excel(root):
    """Ventana con opciones para exportar datos a Excel"""
    excel_win = tk.Toplevel(root)
    excel_win.title("Exportar a Excel")
    excel_win.geometry("400x400")

        # ---- MENSAJE DINÁMICO ----
    mensaje = tk.StringVar()
    mensaje.set("Seleccione una opción para exportar")

    label_mensaje = tk.Label(excel_win, textvariable=mensaje, fg="green", wraplength=350)
    label_mensaje.pack(pady=10)

    # ---- FUNCIONES ----
    def exportar_ventas():
        exportar_ventas_excel()
        mensaje.set("Exportación exitosa.\nArchivo ubicado en la carpeta 'Archivos Excel'")

    def exportar_altas():
        exportar_altas_excel()
        mensaje.set("Exportación exitosa.\nArchivo ubicado en la carpeta 'Archivos Excel'")

    def exportar_stock():
        exportar_stock_excel()
        mensaje.set("Exportación exitosa.\nArchivo ubicado en la carpeta 'Archivos Excel'")

    def exportar_merma():
        exportar_merma_excel()
        mensaje.set("Exportación exitosa.\nArchivo ubicado en la carpeta 'Archivos Excel'")


    def exportar_todo():
        exportar_ventas_excel()
        exportar_altas_excel()
        exportar_stock_excel()
        exportar_merma_excel()
        mensaje.set("Todos los archivos fueron exportados correctamente.\nUbicados en la carpeta 'Archivos Excel'")

    def regresar():
        excel_win.destroy()  # Cerramos la ventana de Excel
        root.deiconify()  # Mostramos la ventana de reportes nuevamente

        # ---- BOTONES ----
    botones = [
        ("Exportar Ventas a Excel", exportar_ventas),
        ("Exportar Ingresos a Excel", exportar_altas),
        ("Exportar Stock a Excel", exportar_stock),
        ("Exportar Merma a Excel", exportar_merma),
        ("Exportar Todo a Excel", exportar_todo),
        ("Regresar", regresar)
    ]

    for texto, funcion in botones:
        tk.Button(excel_win, text=texto, width=30, command=funcion).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()  # Ventana principal que debe existir
    mostrar_ventana_login(root)  # Llamamos la ventana de login
    root.mainloop()
