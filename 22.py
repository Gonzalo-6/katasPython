#Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

from functools import reduce

numeros = [1, 2, 3, 4, 5]
producto_total = reduce(lambda x, y: x * y, numeros)
print(producto_total)