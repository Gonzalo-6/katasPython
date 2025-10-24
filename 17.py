#Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)
digitos = [5, 7, 2]
print(lista_a_numero(digitos)) 