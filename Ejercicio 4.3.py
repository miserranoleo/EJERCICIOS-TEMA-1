from collections import deque

tareas = [
    "Diseñar interfaz de usuario",
    "Desarrollar funcionalidades principales",
    "Testear la aplicación",
    "Optimizar el rendimiento"
]

tareas.sort()
cola_tareas = deque(tareas)

print("Cola de tareas sin números de orden:")
for tarea in cola_tareas:
    print("-", tarea)