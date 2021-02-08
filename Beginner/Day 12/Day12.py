import random

print("""
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
                                                                                      
""")

print("I'm thinking of a number between 1 and 100. Can you guess it?")

number = random.randint(1,100)
def game():
    guess = int(input("Guess a number "))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print("Correct!")
        global lives
        lives = 0
        
level = input('Would you like to play easy or hard? ')
if level == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:
    game()
    lives -= 1
    if lives >0:
        print(f"You have {lives} lives remaining")

print(f"The number was {number}")