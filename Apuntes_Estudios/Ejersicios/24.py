"""Sistema de Inventario
Crear menú
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
Usa
diccionarios
 Ejemplo
productos = {
   "teclado": 5,
   "mouse": 10
}"""

def menu():
    print("\t===== SISTEMA DE INVENTARIO =====\n")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Salir\n")


def crud():
    productos = {
        "teclado": 10,
        "mouse": 10,
        "monitor": 5,
        "laptop": 15
    }

    while True:
        menu()
        try:
            op = int(input("Ingrese una opcion del menu: "))
        except ValueError:
            print("Error: ingrese una opcion valida")
            continue
        
        match op:
            case 1:
                try:
                    nombre = str(input("Introduce el nombre: "))
                    cantidad = int(input("Introduce la cantidad: "))
                except ValueError:
                    print("Error: porfavor introduce bien los valores")
                    continue

                productos[nombre] = cantidad

                print("Producto agregado.")

            case 2:
                print("\t ===== Productos en almacen =====\n")
                for clave, valor in productos.items():
                    print(f"{clave}: {valor}")

            case 3:
                print("\t ===== Buscar productos =====\n")

                buscar = str(input("Ingresa el nombre del producto: "))

                if buscar in productos:
                 print(f"Producto encontrado -> {buscar}: {productos[buscar]}")
                else:
                 print("Producto no encontrado")

            case 4:
                print("\t ===== Eliminar producto =====\n")

                try:
                    eliminar = input("Ingrese el nombre para eliminar: ")
                except ValueError:
                    print("Error: Ingrese el nombre para eliminar el producto")
                    continue

                if eliminar in productos:
                    del productos[eliminar]
                    print(f"Producto eliminado -> {eliminar}")

                else:
                    print("Producto no encontrado")

            case 5:
                print("\t ===== Actualizar Producto =====\n")

                buscar = input("Producto a actualizar: ")

                if buscar in productos:

                    nuevo_nombre = input("Nuevo nombre: ")
                    nueva_cantidad = int(input("Nueva cantidad: "))

                    del productos[buscar]

                    productos[nuevo_nombre] = nueva_cantidad

                    print("Producto actualizado")
            
                else:
                     print("Producto no encontrado")

            case 6:
                print("Saliendo...")
                break
            
            case _:
                print("Opcion invalida")

crud()