#Ejercicio 1#
from math import pi
from math  import sqrt


def cuadrilatero(base, altura):
    area = base * altura 
    return area

def circulo(radio):
    area = pi * (radio ** 2)
    return area

print(cuadrilatero(5, 5))

print(circulo(10))

#ejercicio 2#
def medida(*tupla):
    print('la tupla esta conformada por: ')
    for i in tupla:
        print (i)
    return 'La medida de la tupla es:',len(tupla)
print(medida(1,2,3,4,5))

 