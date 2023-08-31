#Ejercicio 1#
print(((3+2)/(2*5))**2)

#Ejercicio 2#
payasos = 112
munecas = 75 
cantidad1 , cantidad2 = 23 , 54

print('El peso total es de:',(payasos * cantidad1)+(munecas * cantidad2),'g.')

#Strings#
numero = 1
cadena = "Esto es un ejemplo de cadena de texto"
print(cadena)

cadena2 = "y con esto se forma una nueva cadena juntando las dos"
print(numero ,cadena ,cadena2)
print(type(str(numero)))
print(len(cadena))
print(cadena[11 : 18])
print(cadena[-1])

#metodos caracter#
print(cadena.lower()) #Lower#
print(cadena.upper()) #Upper#
print(cadena.capitalize()) #Capitalizer#
print(cadena.title()) #Title#
print(cadena.swapcase()) #Swapcase#