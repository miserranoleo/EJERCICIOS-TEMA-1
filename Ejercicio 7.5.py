def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
        else:
            lista.append(el)
    except ValueError as e:
        print(e)

elementos = [1, 5, -2]
agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos)
