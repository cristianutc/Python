# Lectura y escritura de archivos¶
"""open() devuelve un objeto de archivo, y se usa más comúnmente con dos argumentos posicionales
 y un argumento de palabra clave: open(filename, mode, encoding=None)"""

f = open('workfile', 'w', encoding="utf-8")

#El primer argumento es una cadena que contiene el nombre del archivo
#El segundo argumentos es una cadena algunos caracteres que describen la forma en que se encuentra el archivo será utilizado.
#Los modos más comunes son:

#Modo	Qué hace
#"r"	Leer
#"w"	Escribir (borra lo anterior)
#"a"	Agregar al final
#"x"	Crear (error si ya existe)
#"rb"	Leer binario
#"wb"	Escribir binario 

#Debido a que UTF-8 es el estándar de facto moderno, encoding="utf-8" es recomendado a menos que sepas que 
# necesitas utilizar una codificación diferente

with open('workfile', encoding="utf-8") as f:
    read_data = f.read() 
    f.closed #Podemos comprobar que el archivo se ha cerrado automáticamente.
True
"""""Si no estás usando el with palabra clave, entonces deberías llamar f.close() para cerrar el archivo y liberar inmediatamente cualquier sistema recursos utilizados por él."""
#Es una buena práctica utilizar el with palabra clave al tratar con objetos de archivo. La ventaja es que el 
# archivo está correctamente cerrado una vez finalizada su suite, incluso si se plantea una excepción en algún
#  momento punto. Usando with También es mucho más corto que escribir equivalente try-finally bloques:

#write() es una funcion para escribir en nuestro archivo 
