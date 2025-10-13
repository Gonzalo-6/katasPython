#Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2

except ValueError:
    print("Error: Debes ingresar valores numéricos válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

else:
    print(f"La división fue exitosa. Resultado: {resultado}")

finally:
    print("Fin del programa.")
