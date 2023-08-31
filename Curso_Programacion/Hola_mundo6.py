#                       Funciones                   #
#Funciones de Python#
from cmath import sqrt
from errno import EADDRNOTAVAIL

from numpy import mat, true_divide


num = 7
lista = [1,2,3,4,5,6,7,8,9]

print(type(num)) #se puede ver que tipo de funcion es algo#
print(type(str(num)))
print(type(float(num)))
print(' ')

print(len(lista))
print(max(lista))
print(min(lista))
print(' ')
print(' ')

#Funciones creadas#

'''def <Nombre de la funcion>():
    <sentencias> '''#muy importante la intentacion#
def saludo():
    print('Hola Mundo')
    print('esta es otra sentencia')
    print(' ')
saludo()
saludo()
saludo()

def Tabla7():
    for i in range(1 , 11):
        print('7 X {} = {}'.format(i , i * 7))

Tabla7()

#Librerias#

import math
print(math.pow(10, 2))
print(math.sqrt(64))
print(math.isqrt(64))
print(math.sin(90))
print(math.tan(90))
print(math.factorial(9))

import random
print(random.randint(1,100))

#Return#
'''def <Nombre de la funcion>():
    <sentencias>''' #muy importante la intentacion#
'''return'''

def entero():
    print('Este es un numero entero')
    return 10
print(entero())

def decimal():
    print('Este es un numero decimal')
    return 10.101010
print(decimal())

def frase():
    return 'Esta es una frase'
print(frase())

def asignacion():
    return 1, 2, 3, 4, 5
a, b, c, d, e = asignacion()
print(a,b,c,d,e)

#Parametros y variables#

def suma(num1, num2): #Esos son los parametros#
    suma = num1 + num2
    return suma

print(suma(10, 20))#Estos son los argumentos#
print(suma(30, 50))

#Valores globales#
def valores ():
    global num1
    global num2
    num1 = 110
    num2 = 40
    suma = num1 + num2
    return suma

print(valores()) #Funcion Global#

resta = num1 - num2
print(resta)

#Parametros indefinidos#
def argumento(num):
    return type(num)

print(argumento(5))

def argumentoi(*num): #Se agrega un asterisco para poder ingresar valores indefindos#
    return type(num)

print(argumentoi(5,4,3,2,1))

def argumentoii(*num):
    for i in num:
        print(i)

print(argumentoii(5,4,3,2,1))

#Manejo de errores#
try:
    edad = int(input('Ingresa tu edad: '))
    print('Tu edad es: {}'.format(edad))
except:
    print('Ingresaste un dato erroneo')

#se puede agregar un bucle para que se repita hasta que ingrese bien los datos#
while True:
    try:
        edad = int(input('Ingresa tu edad: '))
        print('Tu edad es: {}'.format(edad))
        break
    except:
        print('Ingresaste un dato erroneo')
    finally:
        print('La ejecucion a finalizado')
#Exepciones multiples#
while True:
    try:
        num = int(input('Ingresa un numero: '))
        resultado = 100 / num
        print(resultado)
        break
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    except ValueError:
        print('Por fabor ingrese un numero')
    except KeyboardInterrupt:
        print('\n Has canselado la ejecucion')
        break
