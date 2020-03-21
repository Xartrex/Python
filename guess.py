import random
import os
"""Funciones"""
"""Juego de azar"""

#print(dir(random))
x = 100
y = 0
print("""
Well sucker, I'm thinking in number within """ +str(y) + """ and """ +str(x) +""", you have 5 attemps,
good luck, you're gonna need it""")

x = random.randint(y,x)
wrong=[]
abuses=["Try again ", "What were you thinking", "You are more stupid than I thought"]
contador = 0;
print("Write your number")

while(contador<5):
    cmd = int(input())
    #cmd = lowercase(cmd)
    # os.system('clear')
    if cmd == x:
        print("You win , and you only needed " + str(contador+1) + " attemps")
        break;

    else:
        if cmd in wrong:
            print("You already wrote it ")
            contador+=1;
        else:
            a = random.randint(0, 2)
            print(abuses[a])
            wrong.append(cmd)
            contador+=1;

            if cmd > x:
                print("My number is lower")

            elif cmd < x:
                print("My number is greater")

if(contador >= 5): print("Loser, my number was " + str(x))
