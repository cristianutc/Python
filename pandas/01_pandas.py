#¿Qué es Pandas?

"""Pandas es una librería de Python para análisis y manipulación de datos.
Te permite:
Leer y escribir datos (CSV, Excel, SQL, JSON…)
Limpiar datos
Filtrar, agrupar y resumir
Analizar patrones
Preparar datos para gráficos o machine learning"""

# Estructuras principales de Pandas
# Series Es como una columna única, con índice.
# Ejemplo:

import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s) # Los numero que aparecen en la izquierda son los indices

