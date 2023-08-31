import turtle

s = turtle.Screen()

t = turtle.Turtle()

s.bgcolor("red")
s.title("Proyecto 01")

t.shapesize(10, 5, 1)
t.shapesize(5, 10, 1)
t.shapesize(3, 3, 3)

t.fillcolor("Blue")

t.pencolor("White")
t.forward(100)

t.pencolor("pink")
t.backward(200)

t.color("blue", "purple")
t.right(90)
t.forward(100)

t.pensize(10)

t.left(90)
t.forward(200)

#Comandos especiales#

#Rellenar forma creada#
t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("White", "black")
t.circle(50)
t.end_fill()

#Cambiar la forma del puntero#
t.shape("turtle")

#Ya no pintar#
t.penup()
t.home()

#Volver a pintar#
t.pendown()

t.goto(100,100)
t.goto(-100,100)
t.home()
t.goto(-100,-100)
t.goto(100,-100)
t.home()

t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

t.home()
t.goto(100,0)
t.home()
t.goto(0,100)
t.home()

t.left(1080)
t.right(1080)

#Ctrl z#
t.undo()

#Limpiar#
t.clear()

#Reiniciar#
t.reset()


t.pencolor("pink")
t.backward(100)

#Sello#
t.stamp()

t.color("blue", "purple")
t.forward(200)


turtle.done()