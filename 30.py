#Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
if son_anagramas(palabra1, palabra2):
    print(f'"{palabra1}" y "{palabra2}" son anagramas.')
else:
    print(f'"{palabra1}" y "{palabra2}" no son anagramas.')

    