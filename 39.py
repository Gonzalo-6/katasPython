#Escribe una función que tome dos parámetros: figura 
# (una cadena que puede ser "rectangulo", "circulo" o "triangulo") 
# y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math
def calcular_area(figura, datos):
    if figura == "rectangulo":
        largo, ancho = datos
        return largo * ancho
    elif figura == "circulo":
        radio, = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no reconocida"
if __name__ == "__main__":
    figura_usuario = input("Introduce la figura (rectangulo, circulo, triangulo): ").strip().lower()
    if figura_usuario == "rectangulo":
        largo = float(input("Introduce el largo del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))
        area = calcular_area(figura_usuario, (largo, ancho))
    elif figura_usuario == "circulo":
        radio = float(input("Introduce el radio del círculo: "))
        area = calcular_area(figura_usuario, (radio,))
    elif figura_usuario == "triangulo":
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        area = calcular_area(figura_usuario, (base, altura))
    else:
        area = "Figura no reconocida"
    print(f"El área del {figura_usuario} es: {area}.")

    