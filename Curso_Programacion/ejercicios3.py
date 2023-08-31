#Formula general para resolver ecuaciones#
from cmath import sqrt


from math import sqrt
a = int(input('Asigne el valor de "A": '))
b = int(input('Asigne el valor de "B": '))
c = int(input('Asigne el valor de "C": '))

if ((b ** 2) - (4*a*c)) < 0 :
    print('no se puede realizar la operacion matematica')
else :
    x1 = (-b + sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - sqrt((b**2) - (4*a*c))) / (2*a)
print('La 1er solucion es:' ,x1, '\nLa 2da solucion es:' ,x2 )

#Ejercicio 2#

p1 = float(input('Ingrese la calificacion de la practica 1: ')) #practica1#
p2 = float(input('Ingrese la calificacion de la practica 2: ')) #practica2#
p3 = float(input('Ingrese la calificacion de la practica 3: ')) #practica3#
Ep = float(input('Ingrese la calificacion del Examen parcial: ')) #Examen parcial#
Ef = float(input('Ingrese la calificacion del Examen final ')) #Examen Final#

Pp = ((p1 + p2 + p3) / 3 ) #promedio de practica#
Prom = ((Pp + (2*Ep) + (3*Ef)) / 6) #Promedio final#

print('El promedio de practica del alumno es:' ,Pp, '\nEl promedio final de el alunmo es de:' ,Prom )