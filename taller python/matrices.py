import random
print(dir(random))


matriz1 = []
matriz2 = []
for i in range(0,4):
    matriz1.append([])
    matriz2.append([])

    for j in range(0,4):
        x = random.randint(0,9)
        y = random.randint(0,9)
        matriz1[i].append(1)
        matriz2[i].append(1)

for i in matriz1:
    print(i)

print("-----------------------")
for j in matriz2:
    print(j)


print("-----------------------")

for i in matriz1:
    for j in i:
        print(j)
        break
print("-----------------------")

def sumar(x,y):

    matriz3 = x
    for i in range(0,4):
        for j in range(0,4):
            matriz3[i][j] = x[i][j] + y[i][j]
    return matriz3

def multiplicar(x,y):
    matriz3 = []
    for i in range(0, len(x)):
        matriz3.append([])
        for j in range(0, len(x)):
            matriz3[i].append(0)

    c = 0

    for i in range(0,4):
        for j in range(0,4):
            c = 0
            for k in range (0,4):
                c += x[i][k] * y[j][k]
            matriz3[i][j] = c

    return matriz3



z = sumar(matriz1, matriz2)
x = multiplicar(matriz1,matriz2)

for i in z:
    print(i)

for i in x:
    print(i)


