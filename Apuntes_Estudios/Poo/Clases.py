"""Clases y objetos
Para entender este paradigma primero tenemos que comprender qué es
una clase y qué es un objeto. Un objeto es una entidad que agrupa un
estado y una funcionalidad relacionadas. El estado del objeto se define
a través de variables llamadas atributos, mientras que la funcionalidad
se modela a través de funciones a las que se les conoce con el nombre
de métodos del objeto."""

class Coche:
    """Abstraccion de los objetos coche."""
    def __init__(self, gasolina): #-> __init__ sirve para realizar cualquier proceso de inicializacion que sea necesario
        self.gasolina = gasolina
        print("Tenemos", gasolina, "Litros")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")

    def conducir(self):
        if self.gasolina > 1:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "Litros")
        else:print("Se quedo sin comustible")

mi_coche = Coche(3)

print(mi_coche.gasolina)
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()