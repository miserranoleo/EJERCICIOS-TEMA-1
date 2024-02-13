#Ejercicio 1
#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

# Leer dos números por teclado
numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

# Determinar aspectos
son_iguales = numero_1 == numero_2
son_diferentes = numero_1 != numero_2
primero_mayor_que_segundo = numero_1 > numero_2
segundo_mayor_igual_que_primero = numero_2 >= numero_1

# Mostrar resultados
print("Son iguales:", son_iguales)
print("Son diferentes:", son_diferentes)
print("El primero es mayor que el segundo:", primero_mayor_que_segundo)
print("El segundo es mayor o igual que el primero:", segundo_mayor_igual_que_primero)
