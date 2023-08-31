from tkinter import *
from tkinter import messagebox
import turtle
import time
import random

def Inicio():
    global NomJug1
    NomJug1 = Tk()
    NomJug1.title('Carrera de Tortugas')
    NomJug1.resizable(True,True)
    NomJug1.geometry("300x150+800+400")

    miFrame = Frame(NomJug1, width="300", height="200")
    miFrame.pack()

    miLabel1 = Label(miFrame, text="Carrera de tortugas", font=("Time New Roman", 12)).place(x=80, y=40)

    miButton = Button(NomJug1, text="Iniciar carrera", width=10, command=Cerrar).place(x=60, y=80)

    miButton2 = Button(NomJug1, text="Cerrar", width=10, command=Cerrar2).place(x=160, y=80)

    NomJug1.mainloop()

def Cerrar():
    NomJug1.destroy()

    s = turtle.Screen()
    s.title('Carrera de Tortugas')
    s.bgcolor('Black')

    t1 = turtle. Turtle()
    t1.hideturtle()
    t1.shape("turtle")
    t1.shapesize(2, 2, 3)
    t1.color("Blue", "Black")

    t2 = turtle. Turtle()
    t2.hideturtle()
    t2.shape("turtle")
    t2.shapesize(2, 2, 3)
    t2.color("Red", "Black")
    
    t1.penup()

    t2.penup()

    Jugador1 = turtle.textinput("Carrera de Tortugas", "Ingrese el nombre del jugadro 1")
    
    if Jugador1 == "":
        messagebox.showinfo("Carrera de tortugas", "Por Favor ingrese un nombre")
        respuesta = str(messagebox.askquestion("Carrera de Tortugas", "Quieres salir del juego?"))
        if respuesta == "yes":
            exit()
        else:
            Jugador1 = "Player 1"
    elif Jugador1 != "":
        Jugador1 = Jugador1
    else:
        exit()

    Jugador2 = turtle.textinput("Carrera de Tortugas", "Ingrese el nombre del jugadro 2")
    if Jugador2 == "":
        messagebox.showinfo("Carrera de tortugas", "Por Favor ingrese un nombre")
        respuesta = str(messagebox.askquestion("Carrera de Tortugas", "Quieres salir del juego?"))
        if respuesta == "yes":
            exit()
        else:
            Jugador1 = "Player 2"
    elif Jugador2 != "":
        Jugador2 = Jugador2
    else:
        exit()

    turtle.speed(100)

    t1.hideturtle()
    t1.goto(250,150)
    t1.pendown()
    t1.pensize(3)
    t1.circle(40)

    t2.hideturtle()
    t2.goto(250,-150)
    t2.pendown()
    t2.pensize(3)
    t2.circle(40)

    t1.penup()
    t1.goto(-300,185)
    t1.showturtle()

    t2.penup()
    t2.goto(-300,-115)
    t2.showturtle()

    dado = [1,2,3,4,5,6]

    for i in range(20):
        if t1.pos() >= (250, 185):
            t1.right(360)
            t1.left(360)
            t1.right(360)
            t1.left(360)
            time.sleep(2)
            messagebox.showinfo("Carrera de tortugas", "{}, El jugador 1 a ganado".format(Jugador1))
            time.sleep(0)
            break
        elif t2.pos() >= (250, -115):
            t2.right(360)
            t2.left(360)
            t2.right(360)
            t2.left(360)
            time.sleep(2)
            messagebox.showinfo("Carrera de tortugas", "{}, El jugador 2 a ganado".format(Jugador1))
            time.sleep(0)
            break
        else:
            Turno1 = str(messagebox.showinfo("Carrera de tortugas", "Presiona Aceptar para Avanzar un Turno"))

            tiro1 = random.choice(dado)

            t1.forward(tiro1 * 15)

            tiro2 = random.choice(dado)

            t2.forward(tiro2 * 15)

    while i <=100:
        Pregunta = str(messagebox.askquestion("Carrera de Tortugas", "Quieres volver a jugar?"))

        if Pregunta == "yes":
            t1.penup()
            t1.goto(-300,185)
            t1.showturtle()

            t2.penup()
            t2.goto(-300,-115)
            t2.showturtle()

            dado = [1,2,3,4,5,6]

            for i in range(20):
                if t1.pos() >= (250, 185):
                    t1.right(360)
                    t1.left(360)
                    t1.right(360)
                    t1.left(360)
                    time.sleep(2)
                    messagebox.showinfo("Carrera de tortugas", "{}, El jugador 1 a ganado".format(Jugador1))
                    time.sleep(0)
                    break
                elif t2.pos() >= (250, -115):
                    t2.right(360)
                    t2.left(360)
                    t2.right(360)
                    t2.left(360)
                    time.sleep(2)
                    messagebox.showinfo("Carrera de tortugas", "{}, El jugador 2 a ganado".format(Jugador2))
                    time.sleep(0)
                    break
                else:
                    Turno1 = str(messagebox.showinfo("Carrera de tortugas", "Presiona Aceptar para Avanzar un Turno"))

                    tiro1 = random.choice(dado)

                    t1.forward(tiro1 * 15)

                    tiro2 = random.choice(dado)

                    t2.forward(tiro2 * 15)
        else:
            messagebox.showinfo("Carrera de tortugas", "Gracias por Jugar")
            exit()
        
        turtle.done()

        exit()

def Cerrar2():
    NomJug1.destroy()


Inicio()




