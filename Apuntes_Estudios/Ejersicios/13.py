#Ahorcado mini
#Haz un mini juego:

#palabra secreta
#usuario adivina letras
#vidas limitadas

import random

def ahorcado():

    print("\t====== AHORCADO ======\n")

    palabra = ["algodon", "python", "computadora", "gato", "programacion"]
    palabraSecreta = random.choice(palabra)
    letras_correctas = []
    vidas = 5

    while vidas > 0:

        letra = input("Ingresa una letra: ").lower()

        # verificar si la letra existe
        if letra in palabraSecreta:
            print("Correcto")

            letras_correctas.append(letra)

        else:
            vidas -= 1
            print(f"Incorrecto, vidas restantes: {vidas}")

        # mostrar progreso
        progreso = ""

        for i in palabraSecreta:

            if i in letras_correctas:
                progreso += i
            else:
                progreso += "_"

        print(progreso)

        # ganar
        if "_" not in progreso:
            print("Ganaste")
            break

    if vidas == 0:
        print("Perdiste")


ahorcado()