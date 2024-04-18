cadena1 = "Hola Mundo"
print(f"{cadena1:>20}")  # Alineado a la derecha en 20 caracteres
print(f"{cadena1[:4]}")  # Truncamiento en el cuarto carácter (índice 3)
print(f"{cadena1.center(20)[:2]}")  # Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
numero1 = 150
print(f"{numero1:05d}")  # Formateo a 5 números enteros rellenados con ceros
numero2 = 7887
print(f"{numero2:7d}")  # Formateo a 7 números enteros rellenados con espacios
numero3 = 20.02
print(f"{numero3:.3f}")  # Formateo a 3 números enteros y 3 números decimales