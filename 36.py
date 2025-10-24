#Crea una función llamada procesar_texto
# Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Código a seguir:
# Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
# Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
# Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
# Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
# Caso de uso:
# Verificar el funcionamiento completo de procesar_texto.


def contar_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        palabra = palabra.lower().strip('.,!?;"\'()')
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower().strip('.,!?;"\'()') != palabra_a_eliminar.lower()]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se requiere un argumento: palabra_a_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Use 'contar', 'reemplazar' o 'eliminar'.")
    
if __name__ == "__main__":
    texto = "Hola mundo hola programar en Python es divertido. Hola de nuevo mundo."

    print("Texto original:")
    print(texto)

    # 1️⃣ Contar palabras
    print("\n🔹 Conteo de palabras:")
    print(procesar_texto(texto, "contar"))

    # 2️⃣ Reemplazar palabra
    print("\n🔹 Reemplazo de palabra ('Hola' → 'Hey'):")
    print(procesar_texto(texto, "reemplazar", "Hola", "Hey"))

    # 3️⃣ Eliminar palabra
    print("\n🔹 Eliminación de palabra ('mundo'):")
    print(procesar_texto(texto, "eliminar", "mundo"))