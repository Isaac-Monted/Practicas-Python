#listas
from numpy import conjugate


lista = ['Python',3.10,'Nombre',1,'valor']
print(type(lista))
print(lista)
print('dato 3:{}, dato 1:{}'.format(lista[2],lista[0])) #Se pueden mandar a llamar los diferentes datos de la lista#

lista[0] = "python" 
print(lista) #Lista completa#
print(lista[2 : ]) #Ultimos dos#
print(lista[ : 2]) #Primeros dos#
print(lista[1 : 2]) #Del 1 al 2 #
print(lista[: : -1]) #Lista al reves#
print(lista[: : 2]) #Cada dos#

#Metodos listas#
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1)
lista1.append(10) #Append se utiliza para agregar elementos a la lista pero hasta el final#
lista1.append('python')
print(lista1)

lista1.insert(0 , 'Lista') #Insert se utiliza para agregar elementos a la lista pero se le puede indicar en donde se va a agregar#
print(lista1)
print(lista1.count(5))#Sirve para buscar cuantos elementos del mismo tipo hay en una lista#
print(lista1.index(5))#Sirve para buscar en donde esta un elemento en la lista#
lista2.sort() #sirve para ordenar la lista#
print(lista2)
lista2.reverse()#sirve para ordenar la lista de atras para adelante#
print(lista2)

#Actualizar datos en una lista#
lista[4] = 'Dato'
print(lista)
#Eliminar datos de la lista#
lista1.pop()#Elimina el ultimo dato de una lista#
print(lista1)
lista1.remove('Lista')#Elimina un dato en espesifico de una lista#
print(lista1)

#                               DICCIONARIOS                            #
diccionario = {'Usuarios' : 'nombre', 'Contrasena' : 123456,  }
print(type(diccionario))
print(diccionario)

#Elementos de un Diccionario#
Diccionario = {'Nombre' : 'Qwerty','Apellido' : 'Js.', 'Edad' : 19, 'Estatura' : 1.75}
print(Diccionario)
print(Diccionario.keys())#Solo muestra las llaves#

print(Diccionario.values())#Solo muestra los valores#

print(Diccionario['Edad'])#Mostrar solo valores especificos#

Diccionario['Numero'] = 5 #Agregar datos a un diccionario#
print(Diccionario)

Diccionario['Numero'] = 1 #Cambiar valores de un diccionario#
print(Diccionario)

#Metodos de los Diccionarios#
dic = {1 : 2, 2 : 3, 3 : 4, 4 : 5}
print(dic)

#Eliminar un valor del diccionario#
dic.pop(3)
print(dic)

#Agregar valoes a un diccionario#
dic.setdefault(3 , 4)
print(dic)

#Mostrar un valor del diccionario#
print(dic.get(2))

#Actualizar un diccionario#
dic.update(diccionario)
print(dic)

#Copiar un diccionario#
dic.copy()
print(dic)

#Limpiar un Diccionario#
dic.clear()
print(dic)

#                                    Conjuntos                                    #
conjunto = {1,2,3,4,5,6,7,8,9}
print(type(conjunto))
conjunto1 = set[1,2,3,4,5,6,7,8,9]
print(type(conjunto1))
conjunto2 = set((1,2,3,4,5,6,7,8,9))
print(type(conjunto2))

#Añadir un elemento a un conjunto#
conjunto.add(10)
print(conjunto)

#Eliminar un elemento de un conjunto#
conjunto.remove(10)
print(conjunto)

#Añadir un elemento iterable#
conjunto.update([1,2,3])
print(conjunto)

#Limpiar un conjunto#
conjunto.clear()
print(conjunto)

#                                    tuplas                                    #
tupla = (1,2,3,4,5,6,7,8,9,10)
tupla2 = (11,12,13,14,15,16,17,18,19,20)

print(type(tupla))
print(tupla)
print(tupla[2])#imprmir solo un fragmento de la tupla#
print(tupla[2 : 5]) #se pueden debanar#
print(tupla[: : -1])

print(tupla + tupla2)#Se pueden sumar#