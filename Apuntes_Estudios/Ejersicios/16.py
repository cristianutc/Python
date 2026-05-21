#metodo burbuja

def metodoBurbuja():

    lista = [5,6,1,7,2,9,3,8,4]

    n = len(lista)

    for i in range(n):

        for j in range(0, n - 1):

            if lista[j] > lista[j + 1]:

                temp = lista[j]

                lista[j] = lista[j + 1]

                lista[j + 1] = temp

    print(lista)


metodoBurbuja()