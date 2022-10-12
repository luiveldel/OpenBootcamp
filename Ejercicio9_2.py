"""
crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter
y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""

from functools import reduce

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def impar(x):
    if x % 2 != 0:
        return True

    return False

def sum(a, b):
    return a + b

resultado = list(filter(impar, num))
print("De la lista: ", num)
print("Los impares son: ", resultado)

reducido = reduce(sum, resultado)
print(f"La suma de todos estos impares es: {reducido}")
