#Polimorfismo
"""¿Qué es el polimorfismo en Python?
El polimorfismo es un concepto de la Programación Orientada a Objetos que significa “muchas formas”. En 
Python, permite que objetos de diferentes clases respondan al mismo método o función, pero cada uno a su 
manera. Dicho simple: Distintos objetos, mismo nombre de método, comportamiento diferente."""

class Perro:
    def hacer_sonido(self):
        return "Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau"
animales = [Perro(), Gato()]

#Ambas clases tienen el mismo método hacer_sonido(), pero hacen cosas distintas.

for animal in animales:
    print(animal.hacer_sonido())

#Python no necesita saber si es un perro o un gato, solo que tiene el método hacer_sonido().

