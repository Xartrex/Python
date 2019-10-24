import random


class Player():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sleepiness = 0
        self.energy = 100
        self.hunger = 0
        self.happiness = 50
        self.alive = True

    def eat(self):
        self.hunger -= 30
        self.sleepiness += 20
        self.energy += 10
        self.happiness += 10

    def sleep(self):
        self.hunger += 50
        self.sleepiness = 0
        self.energy = 90
        self.happiness = 65

class Simulator():
    def __init__(self):
        pass

    def study(npc):
        npc.hunger += 30
        npc.energy -= 40
        npc.sleepiness += 40
        npc.happiness -= 40

    def go_out(npc):
        npc.hunger -= 20
        npc.energy -= 50
        npc.happiness = 70
        npc.sleepiness -= 50

    def options():
        print("1-Estudiar")
        print("2-Salir")
        print("3-Comer")
        print("4-Dormir")

    def status(npc):
        print("Tu nivel de hambre se encuentra al: " + str(npc.hunger) + "%")
        print("Tu  nivel de energia se encuentra al : " + str(npc.energy) + "%")
        print("Tu nivel de felicidad se encuentra al: ",  npc.happiness)
        print("Tu nivel de sueño se encuentra al : ", npc.sleepiness)


    player_name = input("Como te llamas?")
    player_age = input("Cual es tu edad?")
    player = Player(player_name, player_age)
    actions = []

    while(player.alive):

        answer = input("Que quieres hacer? (escribe help para mas informacion)")
        actions.append(answer)

        if answer == "help":
            if(actions[len(actions)-1]=="help" and actions[len(actions)-2]=="help"):
                print("Estas empezando a aburirme...")
            options()
            status(player)


        else:
            if(answer == "estudiar" or answer ==1):
                if(actions[len(actions)-1]=="estudiar" and actions[len(actions)-2]=="estudiar" or actions[len(actions)-1]== 1  and actions[len(actions)-2]== 1):
                    print("Me ha tocado el empollón de turno...")
                study(player)
                status(player)

            elif(answer == "salir" or answer == 2):
                if(actions[len(actions)-1]=="salir" and actions[len(actions)-2]=="salir" or actions[len(actions)-1]== 2  and actions[len(actions)-2]== 2):
                    print("El rollo de siempre, ¿no?")
                go_out(player)
                status(player)


            elif(answer == "comer" or answer == 3):
                if(actions[len(actions)-1]=="comer" and actions[len(actions)-2]=="comer" or actions[len(actions)-1]== 3  and actions[len(actions)-2]== 3):
                    print("¿Te crees Alex?")
                player.eat()
                status(player)


            elif(answer == "dormir" or answer == 4):
                if(actions[len(actions)-1]=="dormir" and actions[len(actions)-2]=="dormir" or actions[len(actions)-1]== 4  and actions[len(actions)-2]== 4):
                    print("Perezoso")
                player.sleep()
                status(player)

            if(player.sleepiness >= 100):
                player.alive = 0

        if(random.randint(0, 20)==16 and player.alive == True):
            player.alive = False
            print("Has perdido, la vida es dura, asumelo");
