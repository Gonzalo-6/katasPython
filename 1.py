#Escribe una función que reciba una cadena de texto como parámetro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.

def frecuencias_letras(cadena):

    cadena = cadena.replace(" ", "")

    frecuencias = {}

    for letra in cadena:
        letra = letra.lower()
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias



texto = "Como apruebe todo, me voy al resu"
resultado = frecuencias_letras(texto)
print(resultado)


