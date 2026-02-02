#Herencia
"""En un lenguaje orientado a objetos cuando hacemos que una clase
(subclase) herede de otra clase (superclase) estamos haciendo que la
subclase contenga todos los atributos y métodos que tenía la supercla-
se. No obstante al acto de heredar de una clase también se le llama a
menudo “extender una clase”."""

#Para indicar que una clase hereda de otra se coloca el nombre de la cla-
#se de la que se hereda entre paréntesis después del nombre de la clase:

class Instrumentos:
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("Estamos tocando")

    def romper(self):
        print("Eso lo pagas tu")
        print("Son", self.precio, "$$$")

class Bateria(Instrumentos):
    def __init__(self, precio, tambores):
        super().__init__(precio)
        self.tambores = tambores
        print(tambores, "Tambores")

    def redoble(self):
        print("Redoble de tambores")
        print("ratataatatata")
    pass

class Guitarra(Instrumentos):
     def __init__(self, precio, cuerdas):
         super().__init__(precio)
         self.cuerdas = cuerdas
         print(cuerdas, "Cuerdas de titanio")
     pass

"""Como Bateria y Guitarra heredan de Instrumento, ambos tienen un
método tocar() y un método romper(), y se inicializan pasando un
parámetro precio. Pero, ¿qué ocurriría si quisiéramos especificar un
nuevo parámetro tipo_cuerda a la hora de crear un objeto Guitarra?
Bastaría con escribir un nuevo método __init__ para la clase Guitarra
que se ejecutaría en lugar del __init__ de Instrumentos. Esto es lo que
se conoce como sobreescribir métodos."""

bateria = Bateria(15000, 20)
bateria.romper()
bateria.redoble()

guitarra = Guitarra(10000, 6)
guitarra.romper()
