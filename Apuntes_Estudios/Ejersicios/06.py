#Pide una palabra y cuenta cuántas vocales tiene.
#Ejemplo:
#Considera:

#a, e, i, o, u
#opcional: mayúsculas

vocales = ["a", "e", "i", "o", "u"]

palabra = str(input("ingrese una palabra para contar las vocales: \n"))

conteo = 0

for letra in palabra:
    if letra.lower() in vocales:
        conteo += 1

print("Numero de vocales: ", conteo)