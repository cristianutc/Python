#numero magico pro

import random

num = random.randint(1, 20)
intentos = 0

while True:
    resul = int(input("Adivina el numero magico del 1 al 20: "))
    intentos += 1

    if resul == num:
        print("Felicidades, adivinaste el numero en", intentos, "intentos")
        break
    elif resul < num:
        print("Muy bajo")
    else:
        print("Muy alto")
              