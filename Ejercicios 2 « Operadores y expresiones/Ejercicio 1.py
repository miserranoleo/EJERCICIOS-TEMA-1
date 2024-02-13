#Ejercicio 1
#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):
#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Los dos números son iguales:", num1 == num2)
print("Los dos números son diferentes:", num1 != num2)
print("El primero es mayor que el segundo:", num1 > num2)
print("El segundo es mayor o igual que el primero:", num2 >= num1)
