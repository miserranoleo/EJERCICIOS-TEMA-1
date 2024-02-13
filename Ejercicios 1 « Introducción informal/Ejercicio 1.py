# Función para identificar el tipo de dato de un valor literal
def identificar_tipo(valor):
    return type(valor).__name__

# Valores literales
valores = [
    "Hola Mundo",
    [1, 10, 100],
    -25,
    1.167,
    ["Hola", "Mundo"],
    ' '
]

# Identificar el tipo de dato de cada valor literal
tipos = list(map(identificar_tipo, valores))

# Imprimir los tipos de datos
for tipo in tipos:
    print(tipo)


