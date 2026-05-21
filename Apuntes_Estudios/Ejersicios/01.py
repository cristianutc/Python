#Pide un número al usuario y determina si es par o impar.

numero = int(input("ingrese un numero entero: "))

if (numero%2) == 0 :
    print(f"El numero que ingreso es par: ${numero}")
else:
    print(f"El numero que ingreso es impar: ${numero}")