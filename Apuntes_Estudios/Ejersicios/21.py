import random


def menu():
    print("\tElije un juego\n")
    print("1.Numero magico")
    print("2.Ahorcado")
    print("3.Piedra, Papel y Tijeras")
    print("4.Salir")


def juegos():

    while True:
        menu()
        try:
            opcion = int(input("\nIngrese una opcion: "))
        except ValueError:
            print("Error, porfavor ingrese un numero: ")
            continue

        match opcion:
            case 1:
                print("\t===== Ecuentra el numero magico ======\n")
                magico = random.randint(1, 100)
                print("Tienes 20 intentos para econtar el numero magico\n")
                intentos = 20

                while intentos > 0:
                    try:
                        numero = int(input("Ingrese un numero del 1 a 100: "))
                    except ValueError:
                        print("Error: ingrese un numero porfavor")
                        continue

                    if numero == magico:
                        print(f"Adivinaste el numero magico -> {magico}")
                        break

                    elif numero < magico:
                        print("muy bajo")

                    else:
                        print("muy alto")

                    intentos -= 1
                    print(f"Te quedan {intentos} intentos")

                    if intentos == 0:
                        print("Perdiste ya no te quedan intentos\n")
                        break

            case 2:
                print("\t ====== Ahorcado ======\n")
                palabra = random.choice(
                    ["consola", "laptop", "celular", "casco", "television"])
                letra_econtrada = []
                vidas = 5

                while vidas > 0:
                    letra = str(input("Ingrese una letra: ")).lower()

                    if letra in palabra:
                        print("Correcto letra econtrada")

                        letra_econtrada.append(letra)

                    else:
                        vidas -= 1
                        print(f"Intcorrecto, vidas restantes {vidas}")

                    progreso = ""

                    for i in palabra:
                        if i in letra_econtrada:
                            progreso += i

                        else:
                            progreso += "_"

                    print(progreso)

                    if "_" not in progreso:
                        print("Ganaste")
                        break

                if vidas == 0:
                    print("Perdiste")

            case 3:
                print("\t ====== Piedra, papel o tijeras ====== \n")

                while True:
                    cpu = random.choice(["piedra", "papel", "tijera"])
                    player = str(input("Ingrese piedra, papel o tijera: ")).lower()
                    print(f"La CPU eligio: {cpu}")
                    resultado = ""

                    if player == cpu:
                        resultado = "Empate"
                        print(resultado)
                        print(f"{player} = {cpu}")

                    elif (
                        (player == "piedra" and cpu == "tijera") or
                        (player == "papel" and cpu == "piedra") or
                        (player == "tijera" and cpu == "papel")
                    ):
                        resultado = "Ganaste"
                        print(resultado)
                        print(f"{player} vence a {cpu}")

                    else:
                        resultado = "Perdiste"
                        print(resultado)
                        print(f"{cpu} vence a {player}")

                    respetir = str(input("Jugar otra vez: si/no: ")).lower()

                    if respetir != "si":
                        break
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion invalida.")


juegos()
