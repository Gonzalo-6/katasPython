#Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista 
# y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado['nombre'] == nombre_completo:
            return empleado['puesto']
    return "La persona no trabaja aquí."    
empleados = [
    {'nombre': 'Ana Gómez', 'puesto': 'Desarrolladora'},
    {'nombre': 'Luis Pérez', 'puesto': 'Diseñador'},
    {'nombre': 'Marta Rodríguez', 'puesto': 'Gerente de Proyecto'}
]
nombre_completo = input("Introduce el nombre completo del empleado: ")
puesto = buscar_puesto(nombre_completo, empleados)
print(f"Puesto: {puesto}")

