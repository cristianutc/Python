vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

palabra = input("Ingresa una palabra: ").lower()

for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1

print(vocales)