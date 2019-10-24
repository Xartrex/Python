
'''Python tiene un tipado dinamico, lo que quiere decir que una variable puede cambiar de tipo indistintamente, ademas de
que en python no se declara el tipo de variable al inicializarse esta'''

var = 5
print(var)

var ="hello"
print(var)

print("------------------------")

'''Ahora veremos la sintaxis de los bucles y condicionales de python'''

x = 0
y = 10

for i in range(x,y):   # i ahora se convertira en 0,1,2,3,4,5,6,7,8 y 9
    print(i)

print("------------------------")
for i in var:  # i ahora se conevrtira en cada objeto o atributo dentro de var, en este caso, cada char que compone el String
    print (i)

print("------------------------")
for i in range(0,30,3): # i se convertira en los numeros entre 0 y 30, empezando por 0 y sumando +3
    print(i)

print("------------------------")

k = "h"
la = "p"
x = input("introduce una palabra: ")

if(k in x):
    print("yes")
elif(la in x):
    print("yeah")
else:
    print("nope")

z = "yeah" if (k in x or la in x) else "nope"
print (z)
'''Creacion de matrices'''

'''Las matrices en Python son listas de listas, no son objetos matrices como tal'''
'''Al tratarse de listas usaremos las funciones: append(), pop(), insert(), extend(), remove(), index(), count(), sort(), reverse()'''

matriz = []
x = 0;
for i in range(0,3):
    matriz.append([])
    for j in range(0,3):
        matriz[i].append(x)
        x+=1



for i in matriz:
    print (i)

