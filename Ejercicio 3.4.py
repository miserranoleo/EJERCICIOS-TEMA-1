#Ejercicio 4
#Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
numeros = int(input("¿Cuántos números quieres introducir? "))
suma = 0

for i in range(numeros):
    numero = float(input("Introduce un número: "))
    suma += numero

media = suma / numeros
print("La media aritmética es:", media)
