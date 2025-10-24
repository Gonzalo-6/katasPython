#Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3
numero = int(input("Introduce un número para calcular su cubo: "))
print(f"El cubo de {numero} es {cubo(numero)}")