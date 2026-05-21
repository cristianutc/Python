#Crea una contraseña guardada en una variable.
#El usuario tiene 3 intentos para adivinarla.


def login():
    clave = "Calistenia200"

    i=1
    while i<=3:
        contraseña = str(input("Introdusca la contraseña: "))
        if contraseña == clave:
            print("Acceso permitido")
            break
        else:
            print("Acceso denegado")
        i += 1

login()