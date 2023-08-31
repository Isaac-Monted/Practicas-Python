import turtle
import time
import random

retraso = 0.1
cuenta = 0
Cuenta_Alta = 0
 
s = turtle.Screen()
s.setup(650,650)
s.bgcolor("Black")
s.title("Juego de la vivorita")

serpiente = turtle.Turtle()
serpiente.speed(10)
serpiente.shape("square")
serpiente.penup()
serpiente.color("Green", "Black")
serpiente.shapesize(1, 1, 3)
serpiente.goto(0,0)
serpiente.direction = "stop"

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.color("red", "Pink")
comida.shapesize(1, 1, 3)
comida.goto(0,100)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto.write("marcador: 0\t Marcador mas alto: 0", align="center", font=("Arial", 12, "normal"))

def Arriba():
    serpiente.direction = "up"

def Abajo():
    serpiente.direction = "down"

def Izquierda():
    serpiente.direction = "left"

def Derecha():
    serpiente.direction = "right"

def Movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)

s.listen()
s.onkeypress(Arriba, "Up")
s.onkeypress(Abajo, "Down")
s.onkeypress(Izquierda, "Left")
s.onkeypress(Derecha, "Right")

while True:
    s.update()

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(1)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()

        cuenta = 0
        texto.clear()

        texto.write("Marcador: {}\t Marcador mas Alto: {}".format(cuenta, Cuenta_Alta), align="center", font=("Arial", 12, "normal"))

    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)

        comida.goto (x, y)

        Nuevo_Cuerpo = turtle.Turtle()
        Nuevo_Cuerpo.speed(0)
        Nuevo_Cuerpo.shape("square")
        Nuevo_Cuerpo.penup()
        Nuevo_Cuerpo.color("Green", "Black")
        Nuevo_Cuerpo.shapesize(1, 1, 3)
        Nuevo_Cuerpo.goto(0,0)

        cuerpo.append(Nuevo_Cuerpo)

        cuenta += 10
        if cuenta > Cuenta_Alta:
            Cuenta_Alta = cuenta
            texto.clear()
            texto.write("Marcador: {}\t Marcador mas Alto: {}".format(cuenta, Cuenta_Alta), align="center", font=("Arial", 12, "normal"))

    total = len(cuerpo)
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()

        cuerpo[index].goto(x, y)

    if total > 0:
        x =  serpiente.xcor()
        y = serpiente.ycor()

        cuerpo[0].goto(x, y)

    Movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            time.sleep(1)
            for i in cuerpo:
                i.clear()
                
                i.hideturtle()
            serpiente.home()
            serpiente.direction = "stop"
            cuerpo.clear()

            cuenta = 0
            texto.clear()

            texto.write("Marcador: {}\t Marcador mas Alto: {}".format(cuenta, Cuenta_Alta), align="center", font=("Arial", 12, "normal"))
            
    time.sleep(retraso)

turtle.done()
