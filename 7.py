#Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map().

def tuplas_a_strings(lista_tuplas):

    return list(map(lambda t: " ".join(map(str,t)), lista_tuplas))

tuplas = [(4,7), ("Iron","Maiden"), (6.9, 3.8)]
resultado = tuplas_a_strings(tuplas)
print(resultado)