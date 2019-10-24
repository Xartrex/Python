'''Calculator'''

#Initializate variables without the type, because python has dynamic type



while(True):

    option = int(input('''\nHi, which operation do you wanna do?:
1) Addition
2) Substraction
3) Multiplication
4) Division
5) Square root
6) Potency
7) Exit\n'''))

    if option > 7  or option < 1:
        option = int(input("That's not an option, try again: "))

    elif(option == 7):
        break

    elif(option == 5):
        x = int(input("Insert the number: "))
        print("The result is: ",x**(1/2))

    else:

        x = int(input("Insert the first number: "))
        y =  int(input("Insert the second number: "))

        if(option == 1):
            print("The result is: ",x+y)

        elif(option == 2):
            print("The result is: ",x-y)

        elif(option == 3):
            print("The result is: ",x*y)

        elif(option == 4):
            print("The result is: ",x/y)

        elif(option == 6):
            print("The result is: ",x**y)
    break
print("see you")
