#Ejercicio 4
#A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:

#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total
#Desarrolla un programa para calcular perfectamente la nota final:

nota_1 = 10
nota_2 = 7
nota_3 = 4

porcentaje_1 = 0.15
porcentaje_2 = 0.35
porcentaje_3 = 0.50

nota_final = nota_1 * porcentaje_1 + nota_2 * porcentaje_2 + nota_3 * porcentaje_3

print("La nota final es", nota_final)