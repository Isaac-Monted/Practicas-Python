#Ejercicio 1#
i = 0
numero = int(input('Escribe un numero que quierass multiplicar: '))

while i < 10:
    i += 1
    print('{} X {} = {}'.format(numero , i , (numero * i)))


#Ejercicio 2#
edad = int(input('Escribe cuantos años vas a cummplir en esete año: '))
i = 0
lista = []
no = edad
while i != edad:
    i += 1
    lista.append(no)
    no -= 1

lista.reverse()
tm = int(len(lista)) #tm = timer#
tt = tm #tt = total timer#
i = 0
print('Tu naciste en el año: {}'.format(2022-edad))
while i != (tm-1):
    print('En el Año {} tu tenias {} años'.format((2023-tt),lista[i]))
    i += 1
    tt -= 1
print('En el Año {} tu tienes {} años'.format(2022,lista[-1]))