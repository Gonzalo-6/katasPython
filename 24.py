#Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

valores = [10, 4, 2]
diferencia_total = reduce(lambda x, y: x - y, valores)
print(diferencia_total)