#Crea una función que retorne las palabras de una lista que
# comiencen con una letra en específico.
# Usa la función filter()

def filtrar_palabras_por_letras(lista_palabras, letra):

    resultado = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
    return resultado

palabras = ["Perro", "gato", "pájaro", "pez", "pantera", "caballo"]
letra = input("Introduce una letra: ")

print(filtrar_palabras_por_letras(palabras, letra))