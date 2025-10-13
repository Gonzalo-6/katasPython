#Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class lista_vacia(Exception):
    pass

def promedio(lista_numeros):
    if not lista_numeros:
        raise lista_numeros("Lista vacia. No se puede calcular.")

    return sum(lista_numeros) / len(lista_numeros)

try:
    numeros = [6,12,18]
    resultado = promedio(numeros)
except lista_vacia as v:
    print("ERROR: {v}")
else:
    print(f"El promedio es: {resultado}")

