print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

dir1 = input('Do you want to go left (L) or right (R)? \n')
if dir1 == 'L':
    tree = input('You come to a palm tree. Do you climb it (C), shake it (S) or keep walking (W)? \n')
    if tree == 'W':
        sand = input('The sand here feels bumpy. Do you dig (D) or keep walking (W)? \n')
        if sand == 'D':
            box = input('You find three boxes. Do you open the red (R), green (G) or purple (P)? \n')
            if box == 'R' or box == 'P':
                print('Snakes and scorpions pour out and you die. Game over.')
            else:
                print('The treasure was the journey of the game <3') 
        else:
            print('Okay, bye.')
    elif tree == 'S':
        print('Game over. A coconut hit you on the head.')
    else:
        print('Congratulations, you are stuck in the tree.')    
else: print('Game over. You were captured by pirates and made to walk the plank.')
