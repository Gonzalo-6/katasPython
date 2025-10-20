#Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas. Usa la función map()

def mayusculas_minusculas(conjunto):

    caracteres_unicos = set(conjunto)

    resultado = list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))
    return resultado
texto = input("Introduce un conjunto de caracteres: ")
print(mayusculas_minusculas(texto))
