#Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5).
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado.
# Si es así, el estado será "aprobado"; de lo contrario, "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.


def evaluar_notas(notas, nota_aprovado=5):

    media = sum(notas) / len(notas)

    estado = "aprovado" if media >= nota_aprovado else "suspenso"
    return (media, estado)

notas_alumno = [5,8,6,3,9]
resultado = evaluar_notas(notas_alumno)

print(resultado)