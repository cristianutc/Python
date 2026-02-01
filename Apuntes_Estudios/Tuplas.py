#tuplas
"""las tuplas son similares a las listas pero en caso de las tuplas no son
mutables(modificables) y para crearlas se usa () """

tupla = (1,2,3)
tupla = tupla[:]
print(tupla) # -> (1,2,3)

print(type(tupla)) # -> para verificar que objeto es

#en las tuplas solo podemos consultar con slicing pero podemos anidar tuplas
tupla2 = (4,5,6)
tupla += tupla2
print(tupla) # -> (1,2,3,4,5,6)

#Acceso a elementos
tupla3 = (10,20,30,40,50)
#print(tupla3[0])
#print(tupla3[1:3])

print(tupla3[::-1]) # -> (50,40,30,20,10)

#la unica manera de modificar la tupla en convertiendo la tupla a lista

tupla4 = (1,2,3)
lista = list(tupla4) #convertimos la tupla a lista con list

lista.append(4) #agregamos elemento a la lista con .append()
lista.extend([5,6]) # agregamos varios elementos con extend()

tupla4 = tuple(lista) #convertimos la lista a tupla con tuple
print(tupla4) # -> (1,2,3,4,5,6)

#Otra forma rápida: concatenar tuplas. No necesitas listas si solo quieres agregar elementos:
tupla5 =  (1,2,3)
tupla5 = tupla5 + (4,) #agregas un solo elemento con solo ,
tupla5 = tupla5 + (5,6) #agregas varios elementos
print(tupla5) # -> (1,2,3,4,5,6)

#Ventajas de usar tuplas
"""Más rápido que listas para recorridos y acceso
Inmutables, así que puedes usarlas como llaves de diccionario
Más seguras si no quieres que los datos cambien accidentalmente"""