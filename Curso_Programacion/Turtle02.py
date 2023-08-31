import turtle

s = turtle.Screen()

t = turtle.Turtle()

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

turtle.done()