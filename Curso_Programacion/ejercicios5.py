#Ejercicio 1"
letra = input("Escriba una letra: ")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print('Es vocal')
else:
    print('No es vocal')

#Ejercicio 2#
numero = int(input('Escribe un numero: '))

if numero >= 0:
    print('El resultado absoluto de |{}| es: {}'.format(numero,numero))
elif numero <= 0:
    print('El numero absoluto de |{}| es: {}'.format(numero,(numero*-1)))
else:
    print('ingrese un numero entero')

#Alternativa ejercicio 1#
if letra.lower() in "aeiou":
    print('Es una vocal')
else:
    print('No es una vocal')

#Alternativa ejercicio 2#
if numero > 0:
    print('El resultado absoluto de |{}| es: {}'.format(numero,numero))
elif numero < 0:
    print('El numero absoluto de |{}| es: {}'.format(numero,abs(numero)))
else:
    print('ingrese un numero entero')

#Ejercicio 1.1#
palabra1 = input('Escribe una palabra: ')
palabra2 = input('Escribe otra palabra: ')
palabra1 = palabra1.capitalize()
palabra2 = palabra2.capitalize()

if len(palabra1) < 3 or len(palabra2) < 3:
    print('Una de las palabras es muy corta')
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print('Las palabras si riman')
elif palabra1[-2: ] == palabra2[-2 : ]:
    print('Las palabras riman un poco')
else:
    print('Las palabras no riman')

#Ejercicio 2.1#
print('Candidatos: \nCandidato A: Partido Rojo \nCandidato B: Partido Verde \nCandidato C: Partido Azul')
voto = input('Elija a un candidato: "A","B","C" ')

if voto.upper() == "A":
    print('Usted a votado por el partido "Rojo"')
elif voto.upper() == "B":
    print('Usted a votado por el partido "Verde"')
elif voto.upper() == "C":
    print('Usted a votado por el partido "Azul"')
else:
    print('Opccion Erronea')
