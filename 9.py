#Escribe una función que tome una lista de nombres de mascotas como parámetro y
# devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter().

def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda m: m.title() not in prohibidas, lista_mascotas))

mascotas= ["Canario", "Tigre", "Gato", "Mapache", "Conejo", "Cocodrilo"]
resultado = filtrar_mascotas(mascotas)
print(resultado)