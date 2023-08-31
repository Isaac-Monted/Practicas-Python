
from msilib.schema import Class


class Fabrica1():
    def __init__(selft, marca, *Colores, **Modelos):
        selft.marca = marca
        selft.Colores = Colores
        selft.Modelos = Modelos

telefono1 = Fabrica1("Alcatel", "Negro", "Azul", "Rojo", m1 = 500, m2 = 100)

print(telefono1.marca)
print(telefono1.Colores)
print(telefono1.Modelos)

"Atributo temporal"

telefono1.Memoria = 512
print(telefono1.Memoria)

"Encapsulamiento"
class A():
    def __init__(selft):
        selft.Contador = 0

    def Incrementar(selft):
        selft.Contador += 1

    def Cuenta(selft):
        return selft.Contador

a = A()
print(a.Cuenta())

a.Incrementar()
print(a.Cuenta())
print()

class B():
    def __init__(selft):
        selft.__Contador = 0

    def Incrementar(selft):
        selft.__Contador += 1

    def Cuenta(selft):
        return selft.__Contador

b = B()
print(b.Cuenta())
print(b.Incrementar())
print(b.Cuenta())
"print(b.__Contador)"
print()

"Profundizacion del Contador"
class AA():
    def __init__(selft):
        selft._Contador = 0
        selft.Cuenta = 0
    
    "Con un '_' Se encapsula un atributo "
    def Incrementar(selft):
        selft._Contador += 1
    
    def Cuenta(selft):
        return selft._Contador
aa = AA()

"      METODO GET          "

class A1():
    def __init__(selft):
        selft._Cuenta = 0
        selft._Contador = 0

    @property
    def Cuenta(selft):
        return selft._Cuenta
    @property
    def Contador(selft):
        return selft._Contador 

a1 = A1()

"Esta es la forma correcta de llamar a los atributos"
print(a1.Cuenta)
print(a1.Contador)
print()

"      METODO SET           "

class A2():
    def __init__(selft):
        selft._Cuenta = 0
        selft._Contador = 0

    @property
    def Cuenta(selft):
        return selft._Cuenta

    @Cuenta.setter
    def Cuenta(selft, Cuenta):
        selft._Cuenta = Cuenta

    @property
    def Contador(selft):
        return selft._Contador 

    @Contador.setter
    def Contador(selft, Contador):
        selft._Contador = Contador

a2 = A2()

"Esta es la forma correcta de modificar a los atributos"
print(a2.Cuenta)
a2.Cuenta = 20
print(a2.Cuenta)

print(a2.Contador)
a2.Contador = 20
print(a2.Contador)
print()
