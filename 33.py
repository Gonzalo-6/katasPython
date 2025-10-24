#Crea una función lambda que sume elementos correspondientes de dos listas dadas

suma_listas = lambda lista1, lista2: [a + b for a, b in zip(lista1, lista2)]
lista1 = [int(x) for x in input("Introduce la primera lista de números separados por espacios: ").split()]
lista2 = [int(x) for x in input("Introduce la segunda lista de números separados por espacios: ").split()]
resultado = suma_listas(lista1, lista2) 
print(f"La suma de las dos listas es: {resultado}")

