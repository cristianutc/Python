import tkinter as tk
from tkinter import messagebox

# ----------------- Funciones simuladas -----------------
def ver_productos():
    messagebox.showinfo("Ver Productos", "Aquí se mostrarían los productos.")

def vender_productos():
    messagebox.showinfo("Vender Productos", "Aquí se gestionaría la venta.")

def buscar_producto():
    messagebox.showinfo("Buscar Producto", "Aquí se buscaría un producto.")

def agregar_producto():
    messagebox.showinfo("Agregar Producto", "Aquí se agregaría un producto.")

def eliminar_producto():
    messagebox.showinfo("Eliminar Producto", "Aquí se eliminaría un producto.")

def exportar_excel(opcion):
    messagebox.showinfo("Exportar a Excel", f"Exportando: {opcion}")

def mostrar_reporte(opcion):
    messagebox.showinfo("Reporte", f"Mostrando: {opcion}")

# ----------------- Ventanas de Menú -----------------
def menu_excel():
    ventana_excel = tk.Toplevel(root)
    ventana_excel.title("Menu Excel")
    ventana_excel.geometry("300x300")

    tk.Label(ventana_excel, text="MENU EXCEL", font=("Arial", 14)).pack(pady=10)

    botones = ["Ventas", "Stock", "Altas", "Todo", "Volver"]
    for b in botones:
        if b == "Volver":
            tk.Button(ventana_excel, text=b, width=25, command=ventana_excel.destroy).pack(pady=5)
        else:
            tk.Button(ventana_excel, text=b, width=25, command=lambda x=b: exportar_excel(x)).pack(pady=5)

def menu_reportes():
    ventana_reportes = tk.Toplevel(root)
    ventana_reportes.title("Menu de Reportes")
    ventana_reportes.geometry("300x300")

    tk.Label(ventana_reportes, text="MENU REPORTES", font=("Arial", 14)).pack(pady=10)

    botones = [
        ("Reporte de Stock", "Stock"),
        ("Reporte de Ventas Totales", "Ventas Totales"),
        ("Reporte de Ventas por Fecha", "Ventas por Fecha"),
        ("Historial Completo", "Historial"),
        ("Exportar a Excel", "Excel"),
        ("Volver", None)
    ]

    for texto, accion in botones:
        if texto == "Volver":
            tk.Button(ventana_reportes, text=texto, width=25, command=ventana_reportes.destroy).pack(pady=5)
        elif texto == "Exportar a Excel":
            tk.Button(ventana_reportes, text=texto, width=25, command=menu_excel).pack(pady=5)
        else:
            tk.Button(ventana_reportes, text=texto, width=25, command=lambda x=accion: mostrar_reporte(x)).pack(pady=5)

def salir():
    root.destroy()

# ----------------- Ventana Principal -----------------
root = tk.Tk()
root.title("Tienda China")
root.geometry("400x400")

tk.Label(root, text="Bienvenido a la Tienda", font=("Arial", 16)).pack(pady=20)

# Botones del menú principal
menu_principal = [
    ("Ver Productos", ver_productos),
    ("Vender Productos", vender_productos),
    ("Buscar Producto", buscar_producto),
    ("Agregar Producto", agregar_producto),
    ("Eliminar Producto", eliminar_producto),
    ("Menu de Reportes", menu_reportes),
    ("Salir", salir)
]

for texto, accion in menu_principal:
    tk.Button(root, text=texto, width=30, command=accion).pack(pady=5)

root.mainloop()
