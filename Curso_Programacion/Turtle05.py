from time import time
import turtle

s = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.clear()

#Ciclo for#
for i in range(4):
    t.forward(100)
    t.right(90)

t.clear()

#Ciclo while#
t.speed(10)
while i <= 100:
    t.circle(i)

    i += 10

t.clear()

#Automatizacion#
while True:
    try:
        Resultado = str(input("Quieres que la tortuga vuelva a moverse?"))
        break
    except:
        print('Ingresaste un dato erroneo')
    finally:
        print('Gracias por Responder')

Resultado = Resultado.lower()

if Resultado == "si":
    t.speed(10)
    i = 0
    while i <= 100:
        t.circle(i)

        i += 10

    t.clear()
else:
    print("La tortuga se eliminara en: ")
    
    i = 5
    while i >= 0:
        import time
        time.sleep(1.5)
        print(i)
        i -= 1
    time.sleep(0)
    print("La tortuga se a eliminado")

turtle.done()