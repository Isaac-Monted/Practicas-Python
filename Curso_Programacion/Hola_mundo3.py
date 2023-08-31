#mostrar datos en pantalla#
nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))

print('Hola {} tu tienes {} años '.format(nombre , edad))

#Booleanos#
verdadero = True
falso = False
print(type(verdadero))
print(verdadero)

uno = 1000
dos = 100
print(uno > dos)

#Metododos booleanos#
cadena = 'Estoy usando los metodos booleanos'
cadena2 = cadena.upper()

print(cadena.startswith('E')) #Startwith# 
print(cadena.endswith('a')) #Endswith# 
print(cadena2.isupper()) #Isupper#
print(cadena.islower()) #Islower#

#condicionales#
nombre1 = int(len(nombre))

if edad >= 18:
    print('Tu eres mayor de edad')
else:
    print('Tu no eres mayor de edad')

if nombre1 <= 3:
    print('tu nombre es muy corto')
elif nombre1 >= 3 and nombre1 <= 5:
    print('tu nombre es normal')
else:
    print('tu nombre es muy largo')

