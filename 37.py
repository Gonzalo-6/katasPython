#Genera un programa que nos indique si es de noche, 
# de día o de tarde según la hora proporcionada por el usuario.

def determinar_momento_dia(hora):
    if 6 <= hora < 12:
        return "Día"
    elif 12 <= hora < 20:
        return "Tarde"
    else:
        return "Noche"
if __name__ == "__main__":
    try:
        hora_usuario = int(input("Introduce la hora del día (0-23): "))
        if 0 <= hora_usuario <= 23:
            momento_dia = determinar_momento_dia(hora_usuario)
            print(f"Es de {momento_dia}.")
        else:
            print("Por favor, introduce una hora válida entre 0 y 23.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")