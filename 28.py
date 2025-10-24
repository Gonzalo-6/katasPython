#Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None
numeros = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
duplicado = primer_duplicado(numeros)
if duplicado is not None:
    print(f"El primer elemento duplicado es {duplicado}")
else:
    print("No hay elementos duplicados en la lista")
    