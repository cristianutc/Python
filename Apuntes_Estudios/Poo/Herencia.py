#Herencia
"""En un lenguaje orientado a objetos cuando hacemos que una clase
(subclase) herede de otra clase (superclase) estamos haciendo que la
subclase contenga todos los atributos y métodos que tenía la supercla-
se. No obstante al acto de heredar de una clase también se le llama a
menudo “extender una clase”."""

#Para indicar que una clase hereda de otra se coloca el nombre de la cla-
#se de la que se hereda entre paréntesis después del nombre de la clase:

class Instrumentos: #clase
    def __init__(self, precio, marca):
        self.precio = precio
        self.marca = marca

    def tocar(self):
        print("Estamos tocando")

    def romper(self):
        print("Eso lo pagas tu")
        print("Son", self.precio, "$$$")

class Bateria(Instrumentos): #sub clase
    def __init__(self, precio, marca, tambores):
        super().__init__(precio, marca)
        self.tambores = tambores

    def redoble(self):
        return "Redoble de tambores\nratataatatata" # -> retornamos el valor para pode imprimir
    pass

class Guitarra(Instrumentos): # sub clase
     def __init__(self, precio, marca, cuerdas):
         super().__init__(precio, marca)
         self.cuerdas = cuerdas
     pass

"""Como Bateria y Guitarra heredan de Instrumento, ambos tienen un
método tocar() y un método romper(), y se inicializan pasando un
parámetro precio. Pero, ¿qué ocurriría si quisiéramos especificar un
nuevo parámetro tipo_cuerda a la hora de crear un objeto Guitarra?
Bastaría con escribir un nuevo método __init__ para la clase Guitarra
que se ejecutaría en lugar del __init__ de Instrumentos. Esto es lo que
se conoce como sobreescribir métodos."""

bateria = Bateria(15000, "yamaha", 20)
print(bateria.marca)
print(bateria.precio,"$ Bateria")
print(bateria.tambores, " Tambores")
print(bateria.redoble()) # -> en este lo imprimimos porque devulve un return print
bateria.tocar()
print("Love mylab")


guitarra = Guitarra(10000, "yamaha", 6)
print(guitarra.marca)
print(guitarra.precio, "Guitarra gibson")
bateria.tocar()
print("chop suey")
print(guitarra.cuerdas, " Cuerdas de Titanio")
guitarra.romper()