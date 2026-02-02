#inpuy y output (Entradas y salidas)

#Entrada: input()
#La función input() se utiliza para obtener datos del usuario. 
#Esta función pausa la ejecución del programa y espera que el usuario ingrese algo a través del teclado.
#Lo que el usuario ingresa es devuelto como una cadena de texto (str).

nombre = input("¿Como te llamas?\n ")
print(f"Hola, {nombre}!")

#Conversión de tipos de entrada
#Lo que el usuario ingresa con input() siempre es una cadena (str).
# Si necesitas que el dato sea de otro tipo (por ejemplo, un número), debes convertirlo a ese tipo explícitamente.

edad = input(f"¿Cuantos años tienes? \n {nombre}\n")
edad = int(edad) # Convertir de string a entero
print(f"Tienes {edad} años.")

precio = input(f"¿Cuál es el precio del artículo?\n {nombre}\n ")
precio = float(precio)  # Convertir a número decimal
print(f"El precio del artículo es: {precio}€")


# Pedir al usuario que ingrese dos números
numero1 = input("Ingresa el primer número: ")
numero2 = input("Ingresa el segundo número: ")

# Convertir las entradas a enteros
numero1 = int(numero1)
numero2 = int(numero2)

# Sumar los números y mostrar el resultado
suma = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es {suma}.")

#Manejo de excepciones en la entrada
#Es importante manejar errores al recibir entradas del usuario, porque 
#si el usuario ingresa un valor que no puede ser convertido a tipo esperado (como un número), el programa generará un error.

try:
    juegos = int(input("¿Cuantos juegos tienes?\n"))
    print(f"Tienes {juegos} juegos.")
except ValueError:
    print(f"¡Eso no es un numero valido! {nombre}")

#Entrada de múltiples valores
#Si necesitas que el usuario ingrese múltiples valores en una sola línea, puedes usar split() para dividir una cadena en una lista. 
entrada = input("Ingresa dos números separados por espacio: ")
numeros = entrada.split()  # Divide la entrada por espacios, creando una lista
numero1 = int(numeros[0])
numero2 = int(numeros[1])

print(f"La suma es: {numero1 + numero2}")


#Entrada con validación de datos
#A veces es necesario validar la entrada del usuario antes de usarla. Aquí tienes un ejemplo de cómo hacerlo con un ciclo while 
# para asegurarte de que el usuario ingrese un número entero:

while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        break  # Salir del ciclo si la entrada es válida
    except ValueError:
        print("Eso no es un número entero, intenta de nuevo.")

print(f"Has ingresado el número {numero}.")
