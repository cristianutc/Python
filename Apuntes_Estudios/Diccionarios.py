#diccionarios
#Un diccionario es mutable, indexado por claves y se define así:
#clave y valor
diccionario = {
    "nombre": "cris",
    "edad": 25,
    "deporte": "calistenia" # -> en el ultimo clave y valor no pones ,
}
#imprimimos los valores con .get
print(diccionario.get("nombre"))
print(diccionario.get("edad"))
print(diccionario.get("deporte"))


diccionario2 = {
    "anime": "kimetsu no yaiba",
    "genero": "shonen",
    "temporadas": 5,
    "emision": False
}
#imprimimos solo claves con un for in
for c in diccionario2:
    print(c)

#imprimimos solo claves con .keys() se usa cuando quieres dejar claro que solo estás iterando sobre las claves, especialmente
#  si después también usas .values() o .items().

for c in diccionario2.keys():
    print(c)

#imprimimos solo los valores con metodo .values():
for v in diccionario2.values():
    print(v)

#imprimimos clave y valores con el metodo .items():
for c,v in diccionario2.items():
    print(c," -> ", v)

#ahora imrpimiremos diccionarios anidados un diccionario donde guarda otro diccionario
#creamos diccionario usuario
usuarios = {
    "1.": {"nombre": "cris", "edad": 25, "pais": "Mexico"},
    "2.": {"nombre": "juan", "edad": 20, "pais": "Colombia"},
    "3.": {"nombre": "tiago", "edad": 18, "pais": "Londres"}
}

#imprimimos solo la clave del primer diccionario usuario que seria 1. 2. 3.
for usuario in usuarios:
    print(usuario)

#Claves del diccionario interno (por cada usuario)
#imrpimira claves del primer diccionario y claves del segundo diccionario aninado
for usuario in usuarios:
    print(f"Clave {usuario}:")
    for clave_interna in usuarios[usuario]:
        print(clave_interna)
    
#con .keys() (opcional, lo hace más explícito)
#Funciona exactamente igual, solo que deja claro que estamos iterando sobre las claves.
for usuario in usuarios.keys():
    print(f"Claves {usuario}:")
    for clave_interna in usuarios[usuario].keys():
        print(clave_interna)
    
#imprimimos el valor .values():
#solo imprimira el valor del primer diccionario
for usuario in usuarios.values():
    print(usuario)

#imprimir el valor del segundo diccionario .values():
for usuario in usuarios:
    print(f"Valor {usuario}:")
    for valor_interno in usuarios[usuario].values():
        print(valor_interno)

for dic_interno in usuarios.values():
    for valor_interno in dic_interno.values():
        print(valor_interno)

for usuario in usuarios:
    print(usuario)
    for valor in usuarios[usuario].values():
        print(valor)

#imprimimos Clave Valor con .items():
for usuario, datos in usuarios.items():
    print(f"Usuario: {usuario}")
    for clave, valor in datos.items():
        print(f" {clave}: {valor}")

#Modificar un valor en un diccionario

diccionario3 = {
    "genero": "terror",
    "nombre": "masacre en texas",
    "duracion": "2:15:23",
    "calificacion": 5
}

diccionario3["nombre"] = "scream"
print(diccionario3.get("nombre"))
#modificar todos los valores del diccionario
# Iterar sobre las claves del diccionario
for clave in diccionario3:
    # Cambiar el valor de cada clave
    if isinstance(diccionario3[clave], int): # Ejemplo: si el valor es un entero
        diccionario3[clave] += 5 #Aumentar 5 a cada valor entero

#imrpimimos todo para ver donde se hizo el cambio
for clave, valor in diccionario3.items():
    print(f"{clave}: {valor}")

# Modificar todos los valores del diccionario
for clave in diccionario3:
    diccionario3[clave] = str(diccionario3[clave]).upper() #modificamos los valores las canedenas de texto por mayusculas

for clave, valor in diccionario3.items():
    print(f"{clave}: {valor}")

# Para convertir todas las claves a mayúsculas
diccionario3 = {clave.upper(): valor for clave, valor in diccionario3.items()}
for clave, valor in diccionario3.items():
    print(f"{clave}: {valor}")

#Cómo cambiar la clave de un diccionario
diccionario3["pelicula"] = diccionario3.pop("NOMBRE") #como cambiamos las claves a mayusculas le pasamos el argumeto a mayusculas
#la forma de hacerlo es eliminarlo con pop() y asugnarle un nuevo valor en este caso pelicula
print(diccionario3)

#eliminar elementos del diccionario
diccionario4 = {
    "Nombre": "cris",
    "Edad": 20,
    "Ciudad": "mexico",
    "telefono": 5577843837,
    "genero": "m"
}

del diccionario4["genero"]
for clave, valor in diccionario4.items():
    print(f"{clave}: {valor}")

# Eliminar y obtener el valor de "edad"
edad_eliminada = diccionario4.pop("Edad")
print(diccionario4)
print("edad eliminada: ",edad_eliminada)

# Eliminar todos los elementos del diccionario
diccionario4.clear()

print(diccionario4)

# Comprobamos si "nombre" está en el diccionario
if "nombre" in diccionario3:
    print("La clave 'nombre' está presente.")
else:
    print("La clave 'nombre' no está presente.")
