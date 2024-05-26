def start():
    print("Welcome, this is a text adventure game.")
    print("I just wanted to let you know that the choices you make today will determine your future. So, think carefully about what you want for your future and make the best choices you can!")
    print("Good luck!")

    m = input("Are you ready?\n y/N")
    if m == 'y':
        moveOn()
    else:
        print("Maybe another time.")

def moveOn():
    print("It's a beautiful sunny day.\nWhere do you want to go?")
    print("1-Take a trip in the forest.")
    print("2-Entering a cave.")
    choose = input("1 or 2: ")
    if choose == '1':
        forest()
    elif choose == '2':
        cave()
    else:
        print("Invalid selection. Please try again.")
        moveOn()
def forest():
    print("\nYou're walking through the woods and you come to a fork in the road.")
    print("Which way do you want to go?")
    print("1-Go right.\n2-Go left.")
    choose = input("1 or 2: ")
    if choose == '1':
        right_way()
    elif choose == '2':
        left_way()
    else:
        print("Invalid selection. Please try again.")
        forest()

def right_way():
    print("\nWhen you go to the right, you reach a waterfall.")
    print("Would you like to cool off and relax at the waterfall?")
    print("Yes or No")
    choose = input("y/N")
    if choose == 'y':
        print("\nIt's marvellous! You had a pleasant time at the waterfall.")
    elif choose == 'n':
        print("\nYou continue.")
    else:
        print("Invalid selection. Please try again.")
        right_way()
        
def left_way():
    print("\nWhen you go left, you reach a dark cave.")
    print("Do you want to go in the cave?")
    print("1. Yes")
    print("2. NO")
    choose = input("Make your choice (1/2): ")

    if choose == '1':
        print("\nYou have entered the cave and are travelling deeper.")
        print("...")
        print("You are lost in the darkness. You have lost the game!")
    elif choose == '2':
        print("\nYou are moving away from the cave.")
    else:
        print("Invalid selection. Please try again.")
        left_way()

def cave():
    print("\nYou entered the cave.")
    print("You saw a sword at the entrance.")
    print("Would you like to take the sword?")
    print("1. Yes")
    print("2. No")
    choose = input("Make your choice (1/2): ")

    if choose == '1':
        print("\nYou have the sword and you continue your adventure.")
    elif choose == '2':
        print("\nYou do not take the sword and you leave the cave.")
    else:
        print("Invalid selection. Please try again.")
        cave()

start()