try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
    print(colores['blanco'])
except KeyError:
    print("Error: La clave 'blanco' no existe en el diccionario de colores.")
