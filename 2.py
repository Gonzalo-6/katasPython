#Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map().

lista=[2,4,6,8,10]

dobles = list(map(lambda x: x*2, lista))

print(dobles)