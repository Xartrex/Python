import random

print("Vamos a jugar")
palabras = ["silla", "mesa", "extintor", "habia", "sandia", "hacia"]
x = random.randint(0,len(palabras)-1)
sol = palabras[x]

y = []
for i in range(0, len(sol)):
    y.append("_")

fallos = []

intentos = 0;
limite = 5;

while(intentos <= limite):

    print(y)

    print("Introduce una letra")
    cmd = input()

    if cmd in sol:
        print("yeah")
        for i in range(0, len(sol)):
            if cmd == sol[i]:
                print("yes")
                y[i] = cmd

        if "_" not in y:
            break;

    elif(cmd in fallos):
        print("esa ya la has dicho")

    else:
        print("fallaste noob")
        intentos += 1
        fallos.append(cmd)


if intentos > limite:
    print("loser")

else:
    print("you win")
