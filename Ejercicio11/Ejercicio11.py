"""
crear una tabla llamada Alumnos que constará de tres columnas:
la columna id de tipo entero,
la columna nombre que será de tipo texto y
la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import sqlite3

def main():
    alumno = input("Nombre de Alumno: ")

    if verifica_alumno(alumno):
        print("Nombre de alumno correcto")
    else:
        print("Nombre incorrecto")


def verifica_alumno(alumno):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM Alumnos WHERE nombre='{alumno}'"
    row = cursor.execute(query)
    data = row.fetchone() # porque solo quiero un elemento
    print("data es: ", type(data))

    cursor.close()
    conn.close()

    if alumno == None:
        return False

    return True

if '__main__' == __name__:
    main()