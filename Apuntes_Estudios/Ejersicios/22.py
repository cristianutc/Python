"""Cajero Automático PRO
Ya hiciste uno básico, ahora mejóralo.
Requisitos
Menú:
1. Consultar saldo
2. Depositar
3. Retirar
4. Historial
5. Salir
Nuevas reglas
guardar historial en una lista
no permitir retirar saldo negativo
validar números negativos
mostrar movimientos realizados
Practicas
listas
validaciones
loops
acumuladores
menús"""

def Menu():
    print("\t===== Cajero Autmatico PRO =====\n")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Historial")
    print("5. Salir\n")

def ejecucion():

    saldo = 0
    deposito = 0
    retiro = 0
    historial = []

    while True:
        Menu()
        try:
            op = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error: Ingrese una opcion.")
            continue

        match op:
            case 1:
                print(f"Tu saldo es de: {saldo}")

            case 2:
                try:
                    deposito = int(input("Ingrese una cantidad a depositar: "))
                except ValueError:
                    print("Error: porfavor una cantidad.")

                if deposito <= 0:
                    print("Opcion invalida")
                else:
                    saldo += deposito
                    historial.append(f"Deposito: +${deposito}")
                    print(f"Finalizas con {saldo}")


            case 3:
                try:
                    retiro = int(input("Ingrese la cantidad a retirar: "))
                except ValueError:
                    print("Error: Ingrese una cantidad valida. ")
                    continue

                if retiro <= 0:
                    print("Cantidad invalida")

                elif retiro > saldo:
                    print("Saldo insuficiente")

                else:
                    saldo -= retiro
                    historial.append(f"Retiro: -${retiro}")
                    print(f"Finalizas con {saldo}")
                    
            case 4:
                print("\t===== HISTORIAL =====")

                if len(historial) == 0:
                    print("No hay movimientos")

                else:
                    for movimiento in historial:
                        print(movimiento)

            case 5:
                print("Saliendo...")
                break

            case _:
                print("Opcion invalida.")

ejecucion()