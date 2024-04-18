lista = [1, 2, 3, 4, 5]
try:
    print(lista[10])
except IndexError:
    print("Error: Índice fuera de rango. Asegúrate de seleccionar un índice válido.")