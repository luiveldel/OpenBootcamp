"""
Ejercicio para comprobar si un ano es bisiesto
"""


def leap_year(year) -> int:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")


if '__main__' == __name__:
    leap_year(2011)
