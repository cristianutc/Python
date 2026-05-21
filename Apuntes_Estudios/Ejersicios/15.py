"""Eliminar duplicados
 Dada esta lista:
 
 numeros = [1,2,2,3,4,4,5]"""

"""def elimanrDuplicados():
    numeros = [1,2,2,3,4,4,5]
    lista = []

    for i in numeros:
        if i not in lista:
            lista.append(i)

    print(lista)

elimanrDuplicados()"""

numeros = [1,2,2,3,4,4,5]

print(set(numeros))