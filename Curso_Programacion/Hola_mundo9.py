class Animales():
    def Habla(selft):
        print("Yo soy un animal")

    def Descripcion(selft):
        print("Yo soy un {}".format(selft.animal))

class perro(Animales):
    pass

class Abeja(Animales):
    def __init__(selft, animal):
        selft.animal = animal

animal = Animales()
animal.Habla()

perro = perro()
perro.Habla()

abeja = Abeja("Abeja")
abeja.Descripcion()

"Profundizando Herencias"

class Animales1():
    def __init__(selft, Nombre):
        selft.Nombre = Nombre

class Perro1(Animales1):
    def __init__(selft,Nombre, Sonido):
        super().__init__(Nombre)
        selft.Sonido = Sonido

perro1 = Perro1("Firulais", "Woow")
print(perro1.Nombre)
print(perro1.Sonido)

"         HERENCIA MULTIPLE        "

class A():
    def Primera(selft):
        return "Esta es la clase A"

class B():
    def Segunda(selft):
        return "Esta es la clase B"

class C(A, B):
    pass

c = C()
print(c.Primera())
print(c.Segunda())

"POLIMORFISMO"

class Cosas():
    def __init__(selft, Mensaje) -> None:
        selft.Mensaje = Mensaje

    def Sonido(selft):
        print(selft.Mensaje)

class objeto(Cosas):
    def Sonido(selft):
        print("Yo hago Woow")

class objeto2(Cosas):
    def Sonido(selft):
        print("Yo no Hablo")

cosa = objeto("Cosa numero 1")
cosa.Sonido()

cosa2 = Cosas("Cosa madre")
cosa2.Sonido()

cosa3 = objeto2("cosa numero 2")
cosa3.Sonido()