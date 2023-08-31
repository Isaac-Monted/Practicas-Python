#ejercicio 1#
Lista = [20, 50, "Curso", "Pyton", 3.14]
print('Estos son los valores actuales de la lista:',Lista)

palabra1 = input('ingrese el primer valor para sustituit en uno: ')
palabra2 = input('Ingrese el segundo valor para sustituir el espacio dos: ')

Lista[0] = palabra1
Lista[1] = palabra2
print('Estos son los nuevos valores de la lista: ',Lista)

#Ejercicio 2#
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[3] *= 2 #Short couth
lista[6] *= 2
lista[8] *= 2

print(lista)