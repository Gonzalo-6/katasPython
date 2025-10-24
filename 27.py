#Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    return sum(lista) / len(lista)
numeros = [float(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
print(f"El promedio de la lista es {promedio(numeros)}")