#Ejercicio 1#
from distutils.log import error
from inspect import Traceback


Diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid", "El Salvador": "San Salvador"}

Pais = input('Ingrese el nombre de un pais para conocer su capital: ')
Pais = Pais.title()


if Pais in Diccionario:
    print('La capital de {} es: {}'.format(Pais,Diccionario[Pais]))
else:
    print('El pais ingresado no esta disponible')

#Ejercicio 2#
diccionario = {1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

numero = int(input('Ingrese el numero de un jugador para conocer su nombre: '))
if numero in diccionario:
    print('El numero: {} es el jugador: {}'.format(numero,diccionario[numero]))
else:
    print('El numero que ingreso no se encuentra en el equipo')

