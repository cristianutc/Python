"""Calculadora de estadísticas
 Dada una lista:

numeros = [10, 20, 30, 40, 50]

Mostrar:
suma
promedio
número mayor
número menor"""

def estadistica():

    numeros = [10, 20, 30, 40, 50]
    suma = 0
    promedio = 0
    mayor = numeros[0]
    menor = numeros[0]

    for i in numeros:
        suma += i
        promedio = (suma /5) 
        if i > mayor:
            mayor = i

        elif i < menor:
            menor = i


    print(suma)
    print(promedio)
    print(mayor)
    print(menor)

estadistica()