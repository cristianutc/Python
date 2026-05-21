#Pide una palabra y verifica si se lee igual al revés.

def palidromo():
    palabra = str(input("Ingrese una palabra: "))

    invertida = palabra[::-1]

    if palabra == invertida:
        print(f"{palabra} = {invertida} \n es una palabra palidromo.")

    else:
        print(f"{palabra} = {invertida} \n no es una palabra palidromo.")

palidromo()