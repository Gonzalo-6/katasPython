#Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras
# de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

palabras = ["tomate", "jamón", "tonelada", "tormenta"]
objetivo = "to"

resultado = filtrar_palabras(palabras,objetivo)
print(resultado)
