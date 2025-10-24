#Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. 
# Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

def buscar_nombre_en_lista():
    nombres = input("Introduce una lista de nombres separados por comas: ").split(',')
    nombres = [nombre.strip() for nombre in nombres]
    nombre_a_buscar = input("Introduce un nombre para buscar en la lista: ").strip()
    
    if nombre_a_buscar in nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_a_buscar}' no fue encontrado en la lista.")
try:
    buscar_nombre_en_lista()
except ValueError as e:
    print(e)
    