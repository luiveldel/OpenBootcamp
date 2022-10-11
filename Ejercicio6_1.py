"""
Ejercicio de clases y objetos
"""


class Color:
    tipo = "Rojo"


class Ruedas:
    cantidad = 4


class Puertas:
    cantidad = 4


class Velocidad:
    cantidad = 250


class Cilindrada:
    cantidad = 3000


class Vehiculo:
    """Creamos instancias"""
    color = Color()
    ruedas = Ruedas()
    puertas = Puertas()


class Coche(Vehiculo):
    """Coche hereda las propiedades y los metodos de Vehiculo"""
    velocidad = Velocidad()
    cilindrada = Cilindrada()

c = Coche()
print("Color del coche es", c.color.tipo)