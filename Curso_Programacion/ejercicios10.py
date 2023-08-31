#Ejercicio 1#
from wsgiref.validate import InputWrapper


i = 0
while i < 10:
    i += 1
    if i == 0:
        continue
    print(i)
print('Deberas de escojer dos numero de los antes mostrados para conocer los numeros que hay entre ellos')
numero1 = int(input('Escribe el primer numero: '))
numero2 = int(input('Ingresa el segundo numero: '))

for i in range(numero1 , numero2 +1):
    print(i)

print(' ')
#Ejercicio 2#
print('Escoje dos numeros que quieras saber que numeros impares hay entre ellos')
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))

for i in range(num1 , num2 + 1):
    if i % 2 == 0:
        continue
    print(i)