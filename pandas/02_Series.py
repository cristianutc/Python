"""Comenzaremos con una descripción general rápida y no exhaustiva 
de los datos fundamentales estructuras en pandas para empezar. 
El comportamiento fundamental sobre los datos Los tipos, la indexación,
el etiquetado de ejes y la alineación se aplican en todos los objetos. 
Para comenzar, importe NumPy y cargue pandas en su espacio de nombres:"""

import numpy as np
import pandas as pd

# Serie
"""Series es una matriz etiquetada unidimensional capaz de contener 
cualquier dato tipo (enteros, cadenas, números de punto flotante, 
objetos Python, etc.). El eje Las etiquetas se denominan colectivamente 
índice. El método básico para crear un Series es llamar:"""

# s = pd.Series(data, index=index)

# Aici, data pueden ser muchas cosas diferentes:
# Es un dictado de Python
# un ndarray
# un valor escalar (como 5)
# El pasado índice es una lista de etiquetas de ejes. El comportamiento del constructor depende de datos’tipo s:
# Desde ndarray
# Si data es un ndarray, índice debe tener la misma longitud que datos. Si no se pasa el índice, se creará uno que tenga valores .[0, ..., len(data) - 1]

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"], dtype='str')
print(s)

# Desde dict
# Series puede instanciar a partir de dictados:

d = {
    "b": 1,
    "a": 0,
    "c": 2
}

print(pd.Series(d))

#Si se pasa un índice, los valores en los datos correspondientes a las etiquetas en el Se extraerá el índice.

di = {
    "a": 0.0,
    "b": 1.0,
    "c": 2.0
}
print(pd.Series(di, index=["b", "c", "d", "a"]))

# Nota
# NaN (no un número) es el marcador de datos faltante estándar utilizado en pandas.

"""Series (una columna)
Es básicamente una sola columna con índice.
Sirve para:
Calcular promedio -> s.mean()
Máximo -> s.max()
Filtrar -> s[s > 20]
En análisis real:
 notas
 precios
 edades
 ventas"""