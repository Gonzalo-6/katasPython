#Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):

    if n < 0:
        return "El factorial no está definido para números negativos"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)

numero = 6
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")