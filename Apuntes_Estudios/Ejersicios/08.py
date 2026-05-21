#cajero automatico

def pantalla():
    print("\tBanco de Mexico nacional de perrones\n")
    print("1.saldo")
    print("2.retiro")
    print("3.ingreso")
    print("4.salir")

pantalla()

def logica():
    saldo = 5000
    while True:
        numero = int(input("Ingrese una opcion: "))

        match numero:
            case 1:
                print(f"Tu saldo es de ${saldo}")

            case 2:
                retiro = int(input(f"Retira el monto no mas de ${saldo} \n"))
                if retiro > saldo:
                    print("Saldo insuficiente")
                else:
                    saldo -= retiro
                    print(f"tu retiro fue de {retiro}")

            case 3:
                ingreso = int(input("Ingresa el saldo"))
                saldo += ingreso
                print(f"Tu saldo es de ${saldo}")

            case 4:
                print("Saliendo del programa...")
                break

logica()