print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")

direction = input("Left or right?: ")
if direction == "Left" or direction == "left":
    print("You arrive at a lake and there is an island in the middle of it. What would you like to do next?")
elif direction == "Right" or direction == "right":
    print("You fell into a hole. GAME OVER.")
    exit()
else:
    print("Please type left or right and try again.")
    exit()

swim_or_wait = input("Swim or wait for a boat? (Type swim or wait): ")
if swim_or_wait == "Swim" or swim_or_wait == "swim":
    print("You were attacked by a shark. GAME OVER.")
    exit()
elif swim_or_wait == "Wait" or swim_or_wait == "wait":
    print("Luckily a boat came by and carried you to the island unharmed. You now see a house with 3 doors.")
else:
    print("Please type swim or wait and try again.")
    exit()

door_choice = input("Which door will you enter? Red, blue or yellow?: ")
if door_choice == "Red" or door_choice == "red":
    print("You were burned alive inside. GAME OVER.")
    exit()
elif door_choice == "Blue" or door_choice == "blue":
    print("You were killed by the ant king inside. GAME OVER.")
    exit()
elif door_choice == "Yellow" or door_choice == "yellow":
    print("You found the treasure! Congrats!")
    exit()
else:
    print("Please type red, blue, or yellow and try again.")
    exit()
