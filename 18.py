#Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes 
# (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 95},
    {"nombre": "Luis", "edad": 22, "calificación": 85},
    {"nombre": "Marta", "edad": 21, "calificación": 90},
    {"nombre": "Carlos", "edad": 23, "calificación": 78},
    {"nombre": "Sofía", "edad": 20, "calificación": 92}
]
mejores_estudiantes = list(filter(lambda estudiante: estudiante["calificación"] >= 90, estudiantes))
for estudiante in mejores_estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificación: {estudiante['calificación']}")