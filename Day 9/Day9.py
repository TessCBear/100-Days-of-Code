import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("Welcome to the Secret Auction \n" + '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

all_bids = {}
repeat = True
while repeat:
    name = input("What is your name? ")
    bid = int(input("How much do you bid? R"))
    all_bids[name] = bid
    answer = input("Do you want to add another person? Y or N: ")
    if answer == "N":
        repeat = False
    cls()

highest = 0
for name in all_bids:
    if all_bids[name] > highest:
        highest = all_bids[name]
        highest_name = name

print(f"The highest bidder is {highest_name} with R{highest}")



