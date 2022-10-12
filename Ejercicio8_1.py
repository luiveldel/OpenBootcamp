"""
Crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo.
Para ello, tendréis que acceder dos veces al archivo creado.
"""

def creartxt(fichero):
    archivo = open(fichero, 'w')
    archivo.close()

def modificatxt(fichero):
    f = open(fichero, 'a')
    f.write("Este archivo se ha creado para practicar con la creacion de ficheros")
    f.close()


def main():
    creartxt('ejercicio.txt')
    modificatxt('ejercicio.txt')


if '__main__' == __name__:
    main()