import random
import Art

print("Let's play rock (R), paper (P), scissors (Sc), lizard (L), spock (Sp)!")

user_choice = input("What do you choose? \n")
choices = ["R", "P", "Sc", "L", "Sp"]
computer_choice = choices[random.randint(0,4)]

if user_choice == "R":
    print("You chose \n" + Art.rock)
elif user_choice == "P":
    print("You chose \n" + Art.paper)
elif user_choice == "Sc":
    print("You chose \n" + Art.scissors)
elif user_choice == "L":
    print("You chose \n" + Art.lizard)
else:
    print("You chose \n" + Art.spock)    

if computer_choice == "R":
    print("I chose \n" + Art.rock)
elif computer_choice == "P":
    print("I chose \n" + Art.paper)
elif computer_choice == "Sc":
    print("I chose \n" + Art.scissors)
elif computer_choice == "L":
    print("I chose \n" + Art.lizard)
else:
    print("I chose \n" + Art.spock)    



if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == "R":
    if computer_choice == "Sc":
        print("Rock crushes scissors. You win.")
    elif computer_choice == "Sp":
        print("Spock vaporises rock. I win.")
    elif computer_choice == "L":
        print("Rock crushes lizard. You win.")
    else:
        print("Paper covers rock. I win")     
elif user_choice == "Sc":
    if computer_choice == "Sp":
         print("Spock smashes scissors. I win.")
    elif computer_choice == "L":
        print("Scissors decapitates Lizard. You win.") 
    elif computer_choice == "P":
        print("Scissors cuts paper. You win.")
    elif computer_choice == "R":
        print("Rock crushes Scissors. I win.")
elif user_choice == "Sp":
    if computer_choice == "L":
        print("Lizard poisons Spock. I win.")
    elif computer_choice == "P":
        print("Paper disproves Spock. I win.")
    elif computer_choice == "R":
        print("Spock vaporises Rock. You win.")
    elif computer_choice == "Sc":
        print("Spock smashes scissors. You win.") 
elif user_choice == "L":
    if computer_choice == "P":
        print("Lizard eats paper. You win.")
    elif computer_choice == "R":
        print("Rock crushes lizard. I win.")
    elif computer_choice == "Sc":
        print("Scissors decapitates lizard. I win.")
    else:
        print("Lizard poisons Spock. You win.") 
elif user_choice == "P":
    if computer_choice == "R":
        print("Paper covers rock. You win.")
    elif computer_choice == "Sc":
        print("Scissors cuts paper. I win.")
    elif computer_choice == "Sp":
        print("Paper disproves Spock. You win.")
    else:
        print("Lizard eats paper. I win.")
else:
    print("error") 
