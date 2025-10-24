#Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
# Reglas:
        #0 - 69: insuficiente
        #70 - 79: bien
        #80 - 89: muy bien
        #90 - 100: excelente

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota inválida"
if __name__ == "__main__":
    try:
        nota_usuario = float(input("Introduce la calificación numérica del alumno (0-100): "))
        resultado = calificacion_texto(nota_usuario)
        print(f"La calificación en texto es: {resultado}.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entre 0 y 100.")
