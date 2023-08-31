from mailbox import NoSuchMailboxError


class Estudiante():
    def __init__(selft, Nombre, Nota):
        selft.Nombre = Nombre
        selft.Nota = Nota

    def Imprimir(selft):
        print("Nombre: {} \nNota: {}".format(selft.Nombre, selft.Nota))

    def Resultado(selft):
        if selft.Nota < 7:
            print("Has Reprobado")
        else:
            print("Has Aprobado")

def Datos():
    while True:
        try:
            Nom = str(input("Ingresa el nombre del alumno: "))
            cal = float(input("Ingrese la calificacion del Alumno: "))
            break
        except:
            print('Ingrese Correctamente los datos')
        finally:
            print('')

    Calificacion = Estudiante(Nom, cal)
    Calificacion.Imprimir()
    Calificacion.Resultado()
    print('')

Datos()
'Datos()'

#Ejercicio Numero 2#
class Calculadora():
    def __init__(selft, Valor1, Valor2):
        selft.Valor1 = Valor1
        selft.Valor2 = Valor2

    def Suma(selft):
        selft.sum = selft.Valor1 + selft.Valor2
        print("El Resultado de la suma es: ",selft.sum)

    def Resta(selft):
        selft.rest = selft.Valor1 - selft.Valor2
        print("El Resultado de la resta es: ",selft.rest)

    def Multiplicacion(selft):
        selft.multi = selft.Valor1 * selft.Valor2
        print("El Resultado de la multiplicacion es: ",selft.multi)

    def Divicion(selft):
        if selft.Valor1 == 0 or selft.Valor2 == 0:
            print("No se puede dividir entre 0")
        else:
            selft.div = selft.Valor1 / selft.Valor2
            print("El Resultado de la divicion es: ",selft.div)


def In():
    while True:
        try:
            Num1 = int(input("Ingresa el Primer Valor: "))
            Num2 = int(input("Ingrese el Segundo Valor: "))
            break
        except:
            print('Ingrese Correctamente los datos')
        finally:
            print('')

    Resultado = Calculadora(Num1, Num2)
    Resultado.Suma()
    Resultado.Resta()
    Resultado.Multiplicacion()
    Resultado.Divicion()
    print('')

In()

#Ejercicio Numero 3#

class Fabrica():
    def __init__(selft, Llanta, Color, Precio):
        selft.Llanta = Llanta
        selft.Color = Color
        selft.Precio = Precio

class Moto(Fabrica):
    def datos(selft):
        print('La Cantidad de llantas es de: ', selft.Llanta)
        print('El color de la moto es: ', selft.Color)
        print('El precio de la moto es de: $', selft.Precio)  

class Carro(Fabrica):
    def datos(selft):
        print('La Cantidad de llantas es de: ', selft.Llanta)
        print('El color del carro es: ', selft.Color)
        print('El precio del carro es de: $', selft.Precio)

moto = Moto(2, "Negro", 2500)
moto.datos()
print("")

carro = Carro(4, "Rojo", 10000)
carro.datos()
print("")

#Ejercicio Numero 4#

class Mariano():
    def Hablar(selft):
        print("Hola...")

class Pulpo(Mariano):
    def Hablar(selft):
        print("Soy un pulpo")

class Foca(Mariano):
    def Hablar(selft, Mensaje):
        selft.Mensaje = Mensaje
        print(selft.Mensaje)

pulpo = Pulpo()
pulpo.Hablar()

print("")

foca = Foca()
foca.Hablar("Soy una foca")

print("")

#Ejercicio Numero 5#

class Universidad():
    def __init__(selft, universidad):
        selft.Universidad = universidad
class Carrera():
    def carrera(selft, especialidad):
        selft.especialidad = especialidad
class Estudiante(Universidad, Carrera):
    def datos(selft, Nombre, Edad):
        selft.Nombre = Nombre   
        selft.Edad = Edad
        print("Mi nombre es: {}, Tengo {} años, Mi especialidad es: {} \nEstudio en la univesidad: {}".format(selft.Nombre, selft.Edad, selft.especialidad, selft.Universidad))

persona = Estudiante("Hardbard")
persona.carrera("Sisitemas")
persona.datos("Carlos", 20)
