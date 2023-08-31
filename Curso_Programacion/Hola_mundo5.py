lista =  [1, 2, 3]
lista2 = [4 ,5 ,6]
lista3 = lista + lista2

print(lista3)

lista = []
edad = int(input('Ingresa tu edad: '))
lista.append(edad)
print(lista)

#Ciclos En Python#
#while#
i = 0
while i < 2: 
    i += 1
    print('Estoy iterando, voy en el ciclo: {}'.format(i))

#Tambien se puede utilizar != para iterar#

#For#
lista =  ["Uno" , "Dos" , "Tres" , "Cuatro" , "Cinco" , "Seis" , "Siete" , "Ocho" , "Nueve" , "Diez"]
Tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in lista:
    print(i)
for j in Tupla:
    print(j)

#Range#
for i in range(1 , 5): #es un rango que se le pone#
    print(i)

for i in range(1 , 11, 2): #con este otro numero le dices como quieres que se recorra#
    print(i)

#Continue y break#
for i in range(1 , 11,): #con este otro numero le dices como quieres que se recorra#
    print(i)
    if i == 5:
        break #Detiene el ciclo#

for i in range(1 , 11,): #con este otro numero le dices como quieres que se recorra#
    if i <=6:
        continue #el ciclo no toma en cuenta lo que if le dice#
    print(i)