import sys

# Verificar si se proporciona el argumento adecuado
if len(sys.argv) != 2:
    print("Uso: python descomposicion.py [numero]")
    sys.exit(1)

# Obtener el número del argumento
try:
    numero = int(sys.argv[1])
except ValueError:
    print("Error: El argumento debe ser un número entero positivo.")
    sys.exit(1)

# Convertir el número en cadena y obtener su longitud
numero_str = str(numero)
longitud = len(numero_str)

# Bucle para descomponer el número e imprimir cada parte con ceros a la izquierda
for i in range(longitud):
    parte = int(numero_str[i]) * 10 ** (longitud - i - 1)
    print("{:04d}".format(parte))
