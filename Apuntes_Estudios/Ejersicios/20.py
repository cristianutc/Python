"""Piedra, papel o tijera

Jugar contra la computadora usando:
random.choice
lógica de ganador
marcador"""

import random

"""guardar datos
validar
repetir
buscar
actualizar"""

print("\t ====== JUEGO ======\n")


import random

while True:

    cpu = random.choice(["piedra", "papel", "tijera"])

    pl1 = input("Ingrese piedra, papel o tijera: ").lower()

    # empate
    if pl1 == cpu:

        resultado = "Empate"

    # jugador gana
    elif (
        (pl1 == "piedra" and cpu == "tijera") or
        (pl1 == "papel" and cpu == "piedra") or
        (pl1 == "tijera" and cpu == "papel")
    ):

        resultado = "Ganaste"

    # cpu gana
    else:

        resultado = "Perdiste"

    print(f"La CPU eligio: {cpu}")

    print(resultado)

    repetir = input("¿Jugar otra vez? si/no: ").lower()

    if repetir != "si":
        break