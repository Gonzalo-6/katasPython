#Escribe una función que tome una cadena de texto y un número entero n como parámetros 
# y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas_que_n(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

frase = input("Introduce una frase: ")
n = int(input("Introduce un número entero: "))

print(palabras_mas_largas_que_n(frase, n))