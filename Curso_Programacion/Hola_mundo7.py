class FabricaDeTelefonos():
    pass

print(type(FabricaDeTelefonos))

celular = FabricaDeTelefonos()
celular2 = FabricaDeTelefonos()

print(type(celular))
print(type(celular2))

def FabricaTelefonos():
    pass

print(type(FabricaTelefonos))
print()

"================Atributos========================"
class Fabrica():
    marca = "Xiaomi"
    color = "Rojo"
    ram = "8 GB"
    Almacenamiento = "128 GB"

phone = Fabrica()
print(phone)
print()
"Acceder a los atributos"

phone.marca
print(phone.marca)

phone.Almacenamiento
phone.color
phone.ram

print(phone.Almacenamiento)
print()

"================Metodos========================"

class Faabrica():
    marca = "Xiaomi"
    color = "Rojo"
    ram = "8 GB"
    Almacenamiento = "128 GB"
    def Llamar(selft, mensaje):
        return mensaje

    def Escuchar(selft):
        print("Estas Escuchando Musica")

cosa = Faabrica()

print(cosa.Llamar("Hola, Con quien hablo?"))
cosa.Escuchar()
print()

"=========================================================="
"Selft"

class Fabrica1():
    marca = "samsung"

    def ElaborarHuawei(selft):
        selft.marca = "Huawei"

telefono1 = Fabrica1()
print(telefono1.marca)

telefono1.ElaborarHuawei()
print(telefono1.marca)

telefono1 = Fabrica1()
print(telefono1.marca)
print()

"Init "

class Fabrica2():
    def __init__(selft):
        print("Estoy usando el metodo Int por que se creo un nuevo objeto")

telefono2 = Fabrica2()
telefono22= Fabrica2()

class Fabrica3():
    def __init__(selft, marca, color):
        selft.marca = marca
        selft.color = color

telefono3 = Fabrica3("Samsung", "negro")
print(telefono3.color)
print(telefono3.marca)
print()

"==============METODOS ESPECIALES================"
"init"
class Fabrica4():
    def __init__(selft, Marca, Color):
        selft.Marca = Marca
        selft.Color = Color

telefono4 = Fabrica4("Xiaomi", "Rojo")

print(telefono4.Marca)
print()

"del"
class Fabrica5():
    def __init__(selft, Marca, Color):
        selft.Marca = Marca
        selft.Color = Color
        print("el objeto {} ha sido creado".format(selft.Marca))

    def __del__(selft):
        print("el objeto {} ha sido destuido".format(selft.Marca))

telefono5 = Fabrica5("Xiaomi", "Rojo")

print(telefono5.Marca)
print()

"str"
class Fabrica6():
    def __init__(selft, Marca, Color):
        selft.Marca = Marca
        selft.Color = Color
        print("el objeto {} ha sido creado".format(selft.Marca))

    def __str__(selft):
        return "El Objeto es {}".format(selft.Marca)

    def __del__(selft):
        print("el objeto {} ha sido destuido".format(selft.Marca))

telefono6 = Fabrica6("Xiaomi", "Rojo")

print(telefono6.Marca)



