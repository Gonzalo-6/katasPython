#Crea una función que convierta una variable en una cadena de texto y 
# enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_variable(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    else:
        enmascarado = '#' * (len(cadena) - 4) + cadena[-4:]
        return enmascarado
var = input("Introduce una variable: ")
print(f"Variable enmascarada: {enmascarar_variable(var)}")

