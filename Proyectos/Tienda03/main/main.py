from db.connection import Database, InicializadorDB
from models.usuario import Usuario
from models.producto import Producto
from models.venta import Venta
from models.reportes import Reporte

def main():
    # Primero creamos la conexion a la DB
    db = Database()
    # Despues inicializamos las tablas
    inicializador = InicializadorDB(db) # Crea las tablas si no existen
    inicializador.crear_tablas()        # Instancia crear tablas
    # Creamos las clases del sistema
    usuario = Usuario(db)               # Instancia usuario
    producto = Producto(db)              # Instancia producto
    venta = Venta(db)                    # Instancia venta
    reporte = Reporte(db)               # Instancia reporte

    #------------------------
    #--- LOGIN O REGISTRO ---
    #------------------------

    while True:
        op = input("Ya tienes cuenta? (s/n): ").lower()
        if op == "s":
            correo = input("Correo: ")
            pwd = input("Contraseña: ")
            if usuario.login(correo, pwd):
                break

        else:
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo: ")
            pwd = input("Contraseña: ")
            usuario.registrar(nombre, edad, correo, pwd)

    #----------------------
    #--- MENU PRINCIPAL ---
    # ---------------------
    while True:
        print("\n1. Ver productos\n2. Agregar producto\n3. Vender producto\n4. Reportes\n5. Salir")
        op = input("Opción: ")
        if op == "1":
            for p in producto.listar():
                print(p)
        elif op == "2":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto.agregar(nombre, precio, stock)
        elif op == "3":
            prod_id = int(input("ID producto: "))
            cantidad = int(input("Cantidad: "))
            prod = next((p for p in producto.listar() if p["id"] == prod_id), None)
            if prod:
                total = venta.registrar_venta(prod_id, cantidad, prod["precio"])
                print(f"Venta registrada. Total: {total}")
        elif op == "4":
            reporte.ventas_por_producto()
        elif op == "5":
            break

if __name__ == "__main__":
    main()