#Ejercicio 2
#Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).
cadena = input("Introduce una cadena de texto: ")
longitud = len(cadena)
resultado = longitud >= 3 and longitud < 10
print(resultado)