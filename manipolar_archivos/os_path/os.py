"""La libreria os econtraremos algunas funciones útiles en nombres de rutas. Leer o escribir archivos ver open()
, y para acceder al sistema de archivos consulte el os módulo. Los parámetros de ruta se pueden pasar como 
cadenas, bytes o cualquier objeto implementando el os.PathLike protocolo."""

#os.path es un módulo que sirve para trabajar con rutas de 
# archivos y carpetas sin tener que escribirlas manualmente.
#importamos la libreria os
import os
from pathlib import Path
#ejemplo
ruta_del_archivo = os.path

"""El problema es que:
Windows usa \
Linux/Mac usa /
os.path se encarga de que eso funcione en cualquier sistema automáticamente."""

ruta_del_archivo2 = os.path.dirname() #os.path.dirname(...) Devuelve SOLO la carpeta donde está el archivo.

ruta_del_archivo3 = os.path.abspath(__file__) #os.path.abspath(__file__) Convierte esa ruta en absoluta (por si fuera relativa).

#Obtener ruta al directorio donde esta el script de este archivo(os.py)
ruta_del_archivo4 = os.path.dirname(os.path.abspath(__file__))

ruta_del_archivo5  = os.path.join(ruta_del_archivo4, "DB") #join() Une partes de una ruta correctamente.
#tenemos la ruta_del archivo4 que es donde se ecuentra nuestro archivo os.py y en la nueva variable 
#ruta_de_archivo5 = os.path.join unimos las rutas de archivo4 con el de la ruta "DB" que es una carpeta

#Ahora tambien podemos unir con join() un archivo en una nueva variable
ruta_del_archivo6 = os.path.join(ruta_del_archivo5, "prueba.txt")

#Funciona perfecto  Pero es más "procedural".

"""Forma moderna (más clara)
Hoy se recomienda usar pathlib en lugar de os.path.
Sería así:"""

script_dir = Path(__file__).resolve().parent

db_dir = script_dir / "DB"

TXT_FILE = db_dir / "prueba.txt"

#Más limpio 
#Más legible 
#Más orientado a objetos 
#os.path ya es multiplataforma 
#pathlib también es multiplataforma
#pathlib es la evolución moderna de os.path
#No necesitas usar ambos, puedes usar solo pathlib

#link de la documentacion
#https://docs.python.org/3/library/os.path.html