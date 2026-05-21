#Genera un número aleatorio entre 1 y 10 y haz que el usuario adivine.
# Dale pistas:

#"Muy alto"
#"Muy bajo"
#"Correcto"

# Usa: import random

import random

num = random.randint(1, 10)

while True:
    resul = int(input("Adivina el numero magico del 1 al 10: "))

    if resul == num:
        print("Felicidades, adivinaste el numero magico")
        break
    
    elif resul < num:
        print("Muy bajo")

    else:
        print("Muy alto")