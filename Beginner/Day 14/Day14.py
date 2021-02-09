import random
import game_data
import art 

A = random.choice(game_data.data)
B = random.choice(game_data.data)

print(art.logo)

repeat = True
score = 0
while repeat:
    while B == A:
        B = random.choice(game_data.data)

    print(f"A: {A['name']} ({A['description']}) from {A['country']} \n" + art.vs + f"B: {B['name']} ({B['description']}) from {B['country']}")
    choice = input("Who has more followers? (A or B) ")

    if A['follower_count'] > B['follower_count']:
        winner = A
    else:
        winner = B

    if choice == "A" and winner == A:
        score += 1
        print(f"Correct. Your score is {score}")
        A = B
        B = random.choice(game_data.data)
    elif choice == "B" and winner == B:
        score += 1
        print(f"Correct. Your score is {score}")
        A = B
        B = random.choice(game_data.data)
    else:
        print(f"Incorrect. You scored {score}")
        repeat = False

