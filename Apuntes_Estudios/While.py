#while
#el ciclo while en Python es un tipo de bucle que se ejecuta mientras una condición sea verdadera.
#Es útil cuando no sabes cuántas veces necesitas ejecutar el ciclo, pero sabes que el ciclo debe 
#continuar mientras se cumpla una condición específica.

i = 1
while i <= 5:
    print(i)
    i += 1 # Incrementamos 'i' para evitar un bucle infinito

#en python no existe el bucle do while pero lo podemos
#simular

n = 1
while True:
    print(n)
    n += 1
    if n > 8: #Condicion de salida
        break #Sale del bucle