import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
comp_cards = []

def deal(person, how_many):
    for num_cards in range(0, how_many):
        person.append(random.choice(cards))

deal(user_cards, 2)
deal(comp_cards, 2)

def comp_turn():
    deal(comp_cards, 1)
    print(f"The computer's cards are {comp_cards}. The total is {sum(comp_cards)}")
    if sum(comp_cards) >= 17:
        return
    else:
        comp_turn()

def user_turn():
    deal(user_cards, 1)
    print(f"Your cards are {user_cards}. Your total is {sum(user_cards)} \n The computer's first card is {comp_cards[0]}")

    if sum(user_cards)>21:
        return
    elif sum(user_cards)==21:
        comp_turn()
    else:
        hit = input("Would you like to hit (H) or pass (P)? ")
        if hit == "H":
            user_turn()
        else:
            comp_turn()

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   )
print(f"Your cards are {user_cards}. Your total is {sum(user_cards)} \n The computer's first card is {comp_cards[0]}")
hit = input("Would you like to hit (H) or (P)? ")
if hit == "H":
    user_turn()
else:
    comp_turn()


if sum(user_cards) == sum(comp_cards):
    print("Draw.")    
elif sum(user_cards) > 21:
    print("You lose.")
elif sum(comp_cards) > 21:
    print("You win.")
elif sum(user_cards) > sum(comp_cards):
    print("You win.")
else:
    print("You lose.")