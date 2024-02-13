#Ejercicio 6
#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
#Nombre Apellido ha sacado un Nota de nota.
#Ayuda
#Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"

# Invertir la cadena
cadena_invertida = cadena[::-1]

# Extraer el nombre y la nota
nombre, nota = cadena_invertida[3:], cadena_invertida[:3]

# Formatear la cadena
resultado = f"{nombre} ha sacado un Nota de {nota}."

print(resultado)