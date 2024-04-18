import sys

if len(sys.argv) != 2:
    print("Uso: python descomposicion.py [numero]")
    sys.exit()

try:
    numero = int(sys.argv[1])
    if numero <= 0:
        raise ValueError
except ValueError:
    print("El argumento debe ser un número entero positivo.")
    sys.exit()

numero_str = str(numero)
longitud = len(numero_str)

for i in range(longitud):
    print(f"{int(numero_str[i]) * 10 ** (longitud - i - 1):04d}")
