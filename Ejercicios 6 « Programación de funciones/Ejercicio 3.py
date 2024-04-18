def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

rel_1 = relacion(5, 10)
rel_2 = relacion(10, 5)
rel_3 = relacion(5, 5)

print("Relación entre 5 y 10:", rel_1)
print("Relación entre 10 y 5:", rel_2)
print("Relación entre 5 y 5:", rel_3)