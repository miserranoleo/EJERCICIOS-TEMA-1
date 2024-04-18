def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

recortado = recortar(15, 0, 10)
print("Número recortado entre 0 y 10:", recortado)