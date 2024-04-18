colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
try:
    print(colores['blanco'])
except KeyError:
    print("Error: La clave 'blanco' no existe en el diccionario.")