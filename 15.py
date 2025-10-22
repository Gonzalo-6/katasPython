#Crea una función lambda que sume 3 a cada número de una lista dada.
def sumar_tres_a_lista(lista):
    return list(map(lambda x: x + 3, lista))
numeros = [1, 2, 3, 4, 5]
sumar_tres = sumar_tres_a_lista(numeros)

print(sumar_tres)  # Salida: [4, 5, 6, 7, 8]