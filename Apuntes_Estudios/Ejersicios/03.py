#Pide un número N y suma todos los números pares desde 1 hasta N.
#Entrada: 10
#Salida: 30  (2+4+6+8+10)

numero = int(input("Ingrese un numero entero: "))
resultado = 0
i = 0
#for i in range(numero):
 #   if (i%2) == 0:
  #      resultado += i

#print(resultado)

while i <= numero:
    if (i%2) ==0:
        resultado += i
    i += 1

print(resultado)