try:
    lista = [1, 2, 3, 4, 5]
    print(lista[10])
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")
