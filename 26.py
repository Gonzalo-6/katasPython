#Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda x, y: x % y
num1 = int(input("Introduce el primer número: "))   
num2 = int(input("Introduce el segundo número: "))
print(f"El resto de la división entre {num1} y {num2} es {resto_division(num1, num2)}")
