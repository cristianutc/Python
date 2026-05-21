"""Crear un menú:

1. Agregar contacto
2. Mostrar contactos
3. Buscar contacto
4. Salir
Usa:
diccionarios
funciones
loops"""

def menu():
    print("\t===== AGENDA =====\n")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir\n")

def logica():

    contactos = {
        "juan": 5555555,
        "pedro": 666666,
        "luis": 7777777,
        "toño": 8888888,
        "marta": 999999
        }
    
    while True:
        menu()

        try:
            opcion = int(input("Ingresa una opcion del menu: "))
        except ValueError:
            print("Error: Por favor ingresa un número válido.\n")
            continue

        match opcion:
            case 1:
                try:
                    nombre = str(input("Nombre del contacto: ")).lower()
                    telefono = int(input("Telefono: "))
                    contactos[nombre] = telefono
                    print("Contacto agregado")
                except ValueError:
                    print("Error: Porfavor ingrese bien los datos ")

            case 2:
                print("\t===== CONTACTOS =====\n")

                for nombre, telefono in contactos.items():
                    print(f"{nombre} -> {telefono}")

            case 3:
                try:
                    buscar = str(input("Ingrese un nombre: ")).lower()
                except ValueError:
                    print("Error: porfavor ingrese un numbre")

                if buscar in contactos:
                    print(f"Telefono: {contactos[buscar]}")

                else:
                    print("Contacto no econtrado")

            case 4:
                print("Saliendo del programa...")
                break

            case _:
                print("Opcion invalida.")
logica()