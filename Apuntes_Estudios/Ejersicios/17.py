"""Mini login
Crear un sistema con:

usuario correcto
contraseña correcta
máximo 3 intentos"""

def MiniLogin():
    usuario = "zyzzgutierrez@gmail.com"
    contraseña = "streetworkout100"
    intentos = 3

    while intentos > 0:

        correo = str(input("Ingrese su correo: "))
        clave = str(input("Ingrese su contraseña: "))

        if ((correo == usuario) and (clave == contraseña)):
            print("Acceso concedido")
            break

        else:
            intentos -= 1
            print(f"Te quedan {intentos} intentos")

    if intentos == 0:
        print("Cuenta bloqueada")

MiniLogin()