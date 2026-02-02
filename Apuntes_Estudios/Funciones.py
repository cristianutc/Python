#Funciones
#Las funciones en Python son una parte esencial de la programación y te permiten organizar tu código, 
# hacerlo más modular y reutilizable. Las funciones te permiten definir bloques de código que puedes ejecutar con solo llamarlas, 
# lo que facilita mucho la lectura y mantenimiento de tu código.

def suma(parametro1, parametro2):
    #bloque de codigo
    resultado = parametro1 + parametro2
    return resultado

print(suma(14,16))

#otra manera mas simple

def resta(a,b):
    return a - b
#llamar a la funcion:
resultado = resta(3,5)
print(resultado)

#Parámetros por defecto
#Puedes darle un valor por defecto a los parámetros de la función.
# Si el usuario no pasa un valor para ese parámetro, se usará el valor por defecto.

def  saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar()
saludar("Ana")

#Funciones con múltiples valores de retorno
#En Python, una función puede devolver más de un valor. 
# Para hacer esto, puedes usar tuplas. Aunque es posible devolver múltiples valores, realmente estás devolviendo una tupla con esos valores.

def operaciones(a,b):
    mutiplicacion = a * b
    divicion = a / b
    return mutiplicacion, divicion # Devuelve una tupla

resultado_multiplicacion, resultado_divicion = operaciones(10,5)
print("Multiplicacion:", resultado_multiplicacion)
print("Divicion:", resultado_divicion)

#Funciones sin retorno (None)
#Si no usas la palabra clave return, la función devuelve por defecto 
# el valor especial None. Esto significa que la función realiza una acción, pero no devuelve un valor explícito.

def imprimir_mensaje():
    print("Este es un mensaje.")

resultado2 = imprimir_mensaje() # Imprime "Este es un mensaje."
print(resultado2) #Imprime "None"

#Funciones con número variable de argumentos
#A veces no sabes cuántos argumentos va a recibir la función. 
# En esos casos, puedes usar *args (para una lista de parámetros posicionales) o **kwargs (para una lista de parámetros con nombre).

def suma_total(*args):
    return sum(args)

resultado = suma_total(1, 2, 3, 4, 5)
print(resultado)  # Imprime 15

#**kwargs (argumentos variables con nombre):
#Permite pasar un número variable de argumentos con nombre (palabra clave).

def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Juan", edad=30, ciudad="Mexico")

#Funciones lambda (funciones anónimas)
#Las funciones lambda son funciones pequeñas y anónimas, que puedes definir en una sola línea de código. 
#Se utilizan cuando se necesita una función simple para usarla en un solo lugar, sin la necesidad de nombrarla.

lambda argumentos: Exception

# Una función lambda que suma dos números
suma = lambda x, y: x + y
print(suma(3, 5))  # Imprime 8

#Funciones recursivas
#Una función recursiva es una que se llama a sí misma. 
#Esto puede ser útil para resolver problemas que pueden dividirse en subproblemas similares, 
#como el cálculo de factoriales o la búsqueda en estructuras como árboles.

def factorial(n):
    if n == 0: #Caso base
        return 1
    else:
        return n * factorial(n-1) #Llamada recursiva (se llama asi misma)
    
print(factorial(5))

"""Aquí, factorial(5) llama a factorial(4), luego factorial(3), y 
así sucesivamente, hasta que llega a la base (factorial(0)), donde se devuelve 1."""