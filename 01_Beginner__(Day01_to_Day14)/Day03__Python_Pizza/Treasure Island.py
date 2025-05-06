print(r'''
*******************************************************************************
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
resp = input('Type "left" or "right"\n')
if resp == "left" or resp == "Left":
    print("Game Over")
    exit()
elif resp == "right" or resp == "Right":
    print("You've come to a lake. There an Island in the middle of the lake.")
    resp = input('Type "wait" to wait for a boat.'
                    'Type "swim" to swim across\n')
    if resp == "wait" or resp == "Wait":
        print("You arrive at the Island unharmed. There is a house with 3 doors.\n"
                "One Gold, One Black and One White")
        resp = input("Which color you choose ? -> ")
        if resp == "Gold" or resp == "gold":
            print("Congratulations, you are the richest person on Earth.")
        elif resp == "Black" or resp == "black":
            print("A black hole sucked you in. Goodbye")
        elif resp == "White" or resp == "white":
            print("You have found the Salvation of the Soul.")
        else:
            print("You have been kicked out of the quest.")
            exit()
    elif resp == "swim" or "Swim":
        print("The great white shark didn't spare you. Nothing remains of you.")
        exit()
    else:
        print("You have been kicked out of the quest.")
        exit()
else:
    print("You have been kicked out of the quest.")
    exit()