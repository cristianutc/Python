#For in
#bucle for in en python

# imprime del 0 a 4 (excluyendo 5)
for i in range(5):
    print(i)

#tabla de multiplicar
m = 1
multi = 0

for i in range(1,11):
    multi = m * i
    print("1 x ",i," = ",multi)

#También puedes personalizar el inicio, el final y el paso con range(start, stop, step):
for i in range(2, 11, 2):
    print(i)

#recorer una lista con for in
lista = [1,2,3,4,5]
for i in lista:
    print(i)
#recorremos una lista al reves usamos el slicing
lista = lista[::-1]
for i in lista:
    print(i)