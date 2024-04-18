import sys

# Verificar si se proporcionan los argumentos adecuados
if len(sys.argv) != 3:
    print("Uso: python tabla.py [filas] [columnas]")
    sys.exit(1)

# Obtener filas y columnas de los argumentos
try:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
except ValueError:
    print("Error: Los argumentos deben ser números enteros positivos del 1 al 9.")
    sys.exit(1)

# Verificar que los números estén en el rango correcto
if not (1 <= filas <= 9 and 1 <= columnas <= 9):
    print("Error: Los argumentos deben ser números enteros positivos del 1 al 9.")
    sys.exit(1)

# Bucle para iterar sobre las filas e imprimir la tabla
for i in range(filas):
    for j in range(columnas):
        print(" * ", end='')
    print()  # Salto de línea para pasar a la siguiente fila
