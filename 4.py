def diferencia_listas(lista1, lista2):
    return list(map(lambda x,y: x - y,lista1, lista2))

a = [2,4,6,8,10]
b = [1,3,5,7,9]

resultado = diferencia_listas(a,b)
print(resultado)