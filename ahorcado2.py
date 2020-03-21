'''En esta clase importaremos un archivo de texto externo al codigo
para jugar al ahorcado'''

import random

import os



def ahorcado():


    f = open ('listado-general.txt','r') # Importo el texto
    text = f.read()                      # Lo hago legible a python


    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)        # Creo una transicion de tildes

    text2 = text.translate(trans)      # Creo un texto igual al importado pero sin tildes

    message = text.split("\n")          # Transformo ambos textos a listas
    message2 = text2.split("\n")


    attempts = 0                   # Intentos fallidos realizados
    answers = ["You're more stupid than I thought", "Try again asshole", "Are you f*cking kidding me?"]

    x = random.randint(0,len(message))  # Genero un numero aleatorio igual al numero de palabras mi lista

    word = message[x]          # Obtengo una palabra aleatoria de la lista con tildes
    word2 = message2[x]         # Obtengo una palabra aleatoria de la lista sin tildes

    told = []           # Creo un array para almacenar las letras que escribire mas tarde

    array = []          # Creo y relleno un array con tantas  "_" como letras tenga mi palabra aleatoria
    for i in range(0,len(word)):
        array.append("_")

    find = False  # Creo este boolenao para salir del loop del juego

    print("Guess my word... if you can")

    while(attempts < 5 and find == False):

        print(array)
        print("\n")
        cmd = input()
        os.system('clear')  #incluir esta linea para limpiar la pantalla por cada letra dada por teclado

        if len(cmd)>1:
            cmd = cmd[0]

        if cmd not in told:  # Si no habia dicho esa letra, se añade a una lista creada antes
            told.append(cmd)

            if cmd in word2:        # Si la letra esta en la palabra a buscar, se printea "yeah" y se sustituye dicha letra en el array en los sitios correspondientes
                print("Yeah!","\t", "fails:", attempts, "\t","written words:",told)       # Tanto las que llevan como las que no llevan tildes

                for i in range(0,len(array)):
                    if cmd == word2[i]:
                        array[i] = word[i]

                    if "_" not in array:  # Si ya he hallado la palabra, salgo del while
                        find = True


            else:  # La letra escrita no esta en mi palabra a buscar, sumo un intento y printeo un insulto aleatorio
                attempts += 1
                if attempts == 5:
                    break;
                y = random.randint(0,2)
                print(answers[y], "\t", "fails:", attempts, "\t","written words:",told )


        else:  # La letra escrita ya la he dicho, porque esta almacenada en la lista "told"
            print("You already wrote it bastard!,  fails:", attempts, "\t","written words:",told )





    f.close()  # NO se exactamente para que es, pero venia en la pagina en la que lo mire XD, creo que no es necesario, tipo Scan.close() en Java

    if attempts < 5 :
        print(array)
        print("You won!, the word was: ",word)
        print("Genius, crack")
    else:
        print("Loser")
        print("My word was " + word)



ahorcado()
