#Ejercicio 1#
from math import factorial
from re import I


lista = []
num = 0
def pedir():
    i = 0
    while i < 5:
        num = float(input('Ingresa un numero: '))
        lista.append(num)
        i += 1

pedir()

def ordenar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

ordenar()

#Ejercicio 2#
def i():
    num = int(input('Ingresa un numero para sacar su factorial: '))
    if num > 0:
        factorial = 1
        for i in range(1 , num + 1):
            factorial *= i
        print('El factorial de {} es: {}'.format(num, factorial))
    else:
        print('El numero tiene que ser positivo o diferenre a 0')
    
i()

#altenativa
def idss():
    num = int(input('Ingresa un numero para sacar su factorial: '))
    if num > 0:
        print('El factorial de {} es: {}'.format(num, factorial(num)))
    else:
        print('El numero tiene que ser positivo o diferenre a 0')
    
idss()
