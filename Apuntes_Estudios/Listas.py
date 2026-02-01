#las listas se crean con , pero para mejores practicas se usa []

lista = 1,2,3,4,5
print(lista) # -> (1,2,3,4,5)

#como veras en la listas2 imprimimos toda la lista gracias slicing [:]
#esto quiere decir [principio : fin : paso ]  (exepto el ultimo)
lista2 = [1,2,3,4,5]
lista2 = lista2[:]
print(lista2) # -> [1,2,3,4,5]

#como veran tambien en una lista podemos guardar csdenas de texto que su vez los
#caracteres lo representa como una lista y endicamos que imprima del 0:4 excepto el ultimo
lista3 = ["python"]
lista3 = lista3[0] [0:3]
print(lista3) #  -> [pyth]

#en la lista 4 imprimimos la lista al reves
lista4 = [1,2,3,4,5]
lista4 = lista4[::-1]
print(lista4) #-> [5,4,3,2,1]

#ahora en la lista5 usaremos el paso dode imprimire de dos en dos
lista5 = [1,2,3,4,5]
lista5 = lista5[0:5:2]
print(lista5) # -> [1,3,5]

#en la lista 6 aplicamos [::] quiere decir que imprimira el primero de la lista y
#saltara al indice 4
lista6 = [1,2,3,4,5]
lista6 = lista6[0::4]
print(lista6) # -> [1,5]

#agregar a la lista ya que la listas son mutables (modificadas)
#lo agrego con el metodo slicing
nueva_lista = [6,7,"final"]
lista2[5:5] = nueva_lista
print(lista2) #-> [1,2,3,4,5,6,7,final]

nueva_lista2 = ["A","B"]
lista2[2:2] = nueva_lista2
print(lista2) # -> [1,2,A,B,3,4,5,6,7,final]

#para eliminar elementos de la lista con slicing como tal no se puede pero hay una manera no recomenada

lista7 = [10,20,30,40,50]
lista7 = lista7[:2] + lista7[3:]
print(lista7) # -> [10, 20, 40, 50]
"""lista7[:2] obtiene todos los elementos antes del índice 2 (es decir, [10, 20]).
lista7[3:] obtiene todos los elementos después del índice 2 (es decir, [40, 50]).
Al concatenar ambos, el elemento en el índice 2 (30) se elimina de la lista resultante."""

#los metodos sirven para hacer mas rapido el agregar a una lista elementos
#El método append() agrega un solo elemento al final de la lista.
lista8 = [1,2,3]
lista8.append(4)
print(lista8) # -> [1,2,3,4]

#metodo insert()
#El método insert() permite insertar un elemento en una posición específica dentro de la lista.
lista9 = [1,2,3]
lista9.insert(1, "A") #agregas dentro del (indice, valor)
print(lista9) # -> [1, 'A', 2, 3]

#metodo extend()
#El método extend() agrega varios elementos de una secuencia (otra lista, tupla, etc.) al final de la lista original.
lista10 = [1,2,3]
lista10.extend([4,5,6])
print(lista10) # -> [1, 2, 3, 4, 5, 6]

#agregar a la lista con operador +=
lista11 = [1,2,3]
lista11 += [4,5] # -> inernamente llama extend()
print(lista11) # -> [1,2,3,4,5]

#metodos eliminar
#metodo remove()
#Elimina la primera coincidencia del valor.
lista12 = [1,2,3]
lista12.remove(2) # -> si no, existe el elemento da error
print(lista12) # -> [1,3]

#metodo pop()
#Elimina y retorna un elemento.
lista13 = [1,2,3]
lista13.pop() # -> elimina el ultimo elemento
print(lista13) # -> [1,2]

#metodo pop(n) por indice
#Elimina elemento por indice
lista14 = [1,2,3,4]
lista14.pop(2) # -> elimina el elemento del indice 2
print(lista14) # -> [1,2,4]

#metodo del
#Elimina por indice o rango
lista15 = [1,2,3,4,5,6]
del lista15[0] # -> elimina el elemonto del indice 0
del lista15[3:5] # -> elimina elementos por rango [3:5] elimina 5,6
print(lista15) # -> [2,3,4]

#metodo clear()
#Elimina todos los elementos
lista16 = [1,2,3,4,5,6,7,8,9,10]
lista16.clear()
print(lista16) # -> []

#slicing
#elimina rangos
lista17 = [1,2,3]
#lista17[:] = [] # -> vacia la lista
lista17[0:2] = [] # -> elimina rango
print(lista17) # -> [3]

#metodo filtrado
#Elimina elementos filtrados
lista18 = [1,2,3,4,3,5,3,6,3,3,3]
lista18 = [x for x in lista18 if x != 3]
print(lista18)