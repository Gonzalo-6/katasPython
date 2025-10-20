#Genera una función que, al recibir una frase,
# devuelva una lista con la longitud de cada palabra.
# Usa la función map()

def longitud_palabras(frase):
    palabras =frase.split()
    longitudes = list(map(len, palabras))
    return longitudes

texto = input("Introduce una frase: ")
print(longitud_palabras(texto))