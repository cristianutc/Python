#Pide una frase y cuenta cuántas palabras tiene.

"""def contador_de_palabras():

    frase = input("Ingresa una frase: ").lower()

    palabras = frase.split()

    contador = 0

    for i in palabras:
        contador += 1

    print(f"La frase tiene {contador} palabras")
    print(palabras)


contador_de_palabras()"""

frase = input("Ingresa una frase: ").lower()

print(len(frase.split()))