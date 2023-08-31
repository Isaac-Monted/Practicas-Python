frase = "Hola mundo"
numero = 89
flotante = 3.141592

print(type(frase))
print(frase)

print(type(numero))
print(numero)

print(type(flotante))
print(flotante)

import keyword
from typing import Type
print(keyword.kwlist)

#las constantes se ponen en mayusculas, ejemplo PI = 3.141592 #
'''Esta 
es
otra 
forma de
comentar el texto'''

Nombre , Apellido = 'Juanito' , 'Banana'
print(Nombre + ' ' + Apellido)

#Apartado de numeros "Str" "Int" "Float" #

num1 = 5
num2 = 3.1415
print(type(num1))
print(type(num2))

#cambio de Int a Float #
print(type(float(num1)))
print(float(num1))

#cambio de Float a Int #
print(type(int(num2)))
print(float(num2))

#Operadores aritmeticos practica#
print(31.4159265 / 10)
print(2 ** 5)
print(31.4159265 // 10)
print(31.4159265 % 10) #Este operador muestra el residuo de una divicion#
