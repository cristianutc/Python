#Encapasulamiento
"""La encapsulación se refiere a impedir el acceso a determinados mé-
todos y atributos de los objetos estableciendo así qué puede utilizarse
desde fuera de la clase."""

"""En Python no existen los modificadores de acceso, y lo que se suele
hacer es que el acceso a una variable o función viene determinado por
su nombre: si el nombre comienza con dos guiones bajos (y no termina
también con dos guiones bajos) se trata de una variable o función pri-
vada, en caso contrario es pública."""

#ejemplo
class Ejemplo:
    def publico(self):
        print("funcion publico")

    def __privado(self):
        print("funcion privado")

e = Ejemplo()
e.publico()
#e.__privado()

#podemos acceder a él mediante una pequeña trampa
e._Ejemplo__privado()

"""En ocasiones también puede suceder que queramos permitir el acceso
a algún atributo de nuestro objeto, pero que este se produzca de forma
controlada. Para esto podemos escribir métodos cuyo único cometido
sea este, métodos que normalmente, por convención, tienen nombres
como getVariable y setVariable; de ahí que se conozcan también con
el nombre de getters y setters."""

class Fecha():
    def __init__(self):
        self.__dia = 1 #tiene doble guion bajo esto lo combuerte en atributo privado 
    #getter
    def getDia(self):
        return self.__dia #getDia permite acceder al dato sin tocar directamente el atributo privado
    #setter 
    def setDia(self, dia):
        if dia > 0 and dia < 31: #setDia sirve para modificar el valor del atributo privado
            self.__dia = dia #lo modifica
            return print(dia) #retorna el valor modificado
        else:
            print("Error")

    dia = property(getDia, setDia) #property Permite usar dia como si fuera un atributo, pero por detrás llama a getDia y setDia

mi_fecha = Fecha()
mi_fecha.dia = 3

#resumen: El encapsulamiento oculta los atributos de una clase y controla su acceso mediante métodos getter y setter; property permite acceder a esos métodos como si fueran atributos normales.

#por ultimo una manera mas lejible es usar @property(forma moderna)
class Fecha2:
    def __init__(self):
        self.__dia = 1

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, valor):
        if 0 < valor < 31:
            self.__dia = valor
            return print(f"el nuevo valor es :{valor}")
        else:
            print("Error")

mi_fecha2 = Fecha2()
mi_fecha2.dia = 33   # Error
mi_fecha2.dia = 15   # El nuevo valor es 15
print(mi_fecha2.dia) # 15
