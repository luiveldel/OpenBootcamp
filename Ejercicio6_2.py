"""
Composicion: una clase esta compuesta de otras clases
"""

"""
Imprimir todos los atributos de Alumno y mostrar la nota y si ha aprobado o no
"""


class Nombre:
    name = "Carlos"


class Nota:
    grade = 4

class Test:
    aprobado = "Aprobado"
    suspenso = "Suspenso"

class Alumno:
    nombre = Nombre()
    nota = Nota()
    test = Test()

    def is_approved(self):
        if Alumno.nota.grade >= 5:
            return self.test.aprobado
        else:
            return self.test.suspenso

a = Alumno()
print(f"El alumno {a.nombre.name} ha obtenido un {a.nota.grade} y esta {a.is_approved()}")