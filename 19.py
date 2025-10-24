#Crea una función lambda que filtre los números impares de una lista dada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = list(filter(lambda x: x % 2 != 0, numeros))   
print(impares)  