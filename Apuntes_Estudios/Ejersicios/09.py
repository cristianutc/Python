#Pide un número y muestra su tabla del 1 al 10.

numero = int(input("Ingrese un numero para la tabla de multiplicar: "))

def tabla(numero):
    ressultado = 0

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabla(numero)