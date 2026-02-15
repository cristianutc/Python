import os
from pathlib import Path

# Ruta del script
script_ruta = Path(__file__).resolve().parent

# Carpeta donde esta nuestro archivo
ruta_carpeta = script_ruta / "ruta_txt"

# Archivo dentro de la carpeta
ruta_archivo = ruta_carpeta / "prueba.txt"

# 1 Abrimos el archivo en modo escritura y escribimos texto
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Esta es una prueba.\n")
    archivo.write("Ahora estoy escribiendo dentro del archivo.\n")

# 2 Abrimos el archivo en modo lectura y mostramos su contenido
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()  # Lee todo el archivo
    print("Contenido del archivo:")
    print(contenido)

#Ahora leeremos linea por linea de un nuevo archivo2
#Ruta del script
script_ruta2 = Path(__file__).resolve().parent

# Carpeta donde esta nuesrto archivo
ruta_carpeta2 = script_ruta2 / "ruta_txt"

# Archivo dentro de la carpeta
ruta_archivo2 = ruta_carpeta2 / "prueba2.txt"

# 1 Abrimos el archivo en modo escritura y escribimos texto
with open(ruta_archivo2, "a", encoding="utf-8") as archivo2:
    archivo2.write("primera linea\n")
    archivo2.write("segunda linea\n")
    archivo2.write("tercera linea\n")
    archivo2.write("cuarta linea\n")

# 2 Leemos el archivo línea por línea usando readlines()
with open(ruta_archivo2, "r", encoding="utf-8") as archivo2:
    lineas = archivo2.readlines() # Devuelve una lista de líneas
    print("Usando readlines():")
    for i in lineas:
        print(i.strip()) # strip() elimina el salto de línea al final

# 3 Otra forma más eficiente: leer línea por línea con un bucle for
print("\nUsando bucle for directamente:")
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())