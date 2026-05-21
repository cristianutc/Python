#Encuentra el número más grande de esta lista:


def numeroMax():
    numeros = [4, 7, 1, 99, 34, 12]
    mayor = numeros[0]

    for i in numeros:
        if i > mayor :
            mayor = i
    print(f"El numero mayor es : {mayor}")

numeroMax()