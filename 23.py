#Concatena una lista de palabras. Usa la función reduce()

from functools import reduce
palabras = ['Hola', 'Antonio,', 'soy', 'Gonzalo.']
frase = reduce(lambda x, y: x + ' ' + y, palabras)
print(frase)