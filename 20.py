#Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

elementos = [1, 'dos', 3, 'cuatro', 5, 'seis', 7, 'ocho']
enteros = list(filter(lambda x: isinstance(x, int), elementos))
print(enteros)