import sys

if len(sys.argv) != 3:
    print("Uso: python tabla.py [filas] [columnas]")
    sys.exit()

try:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if not (1 <= filas <= 9 and 1 <= columnas <= 9):
        raise ValueError
except ValueError:
    print("Ambos argumentos deben ser números enteros positivos del 1 al 9.")
    sys.exit()

for i in range(filas):
    for j in range(columnas):
        print(" * ", end='')
    print()  # Para imprimir una nueva línea después de cada fila