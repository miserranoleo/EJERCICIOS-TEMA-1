#Ejercicio 3
#Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.
#Sugerencia
#Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
#El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

sum_of_even_numbers = sum(range(0, 101, 2))
print(sum_of_even_numbers)