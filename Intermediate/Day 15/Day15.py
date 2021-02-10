import data

money_in_machine = 0

def make_drink(drink):
    data.resources["water"] -= data.MENU[drink]["ingredients"]["water"]
    data.resources["milk"] -= data.MENU[drink]["ingredients"]["milk"]
    data.resources["coffee"] -= data.MENU[drink]["ingredients"]["coffee"]
    print(f"Here is your {drink}. Enjoy!")

def money(drink):
    ones = int(input("How many R1 coins? "))
    twos = int(input("How many R2 coins? ")) * 2
    fives = int(input("How many R5 coins? ")) * 5
    tens = int(input("How many R10 notes? ")) * 10
    twenties = int(input("How many R20 notes? ")) * 20
    fifties = int(input("How many R50 notes? ")) * 50
    hundreds = int(input("How many R100 notes? ")) * 100

    total_money_paid = ones + twos + fives + tens + twenties + fifties + hundreds
    if total_money_paid >= data.MENU[drink]["cost"]:
        serve(drink)
        global money_in_machine
        money_in_machine += total_money_paid
        if total_money_paid > data.MENU[drink]["cost"]:
            change = total_money_paid - data.MENU[drink]["cost"]
            money_in_machine -= change
            print(f"Your change is R{change}.")
    else:
        print("Sorry, that isn't enough money.")
        return

def serve(drink):
    
    for ingredients in data.resources:
        if data.resources[ingredients] < data.MENU[drink]["ingredients"][ingredients]:
            print("Sorry, there are not enough ingredients to make your order.")
            return
    make_drink(drink)

while True:
    drink = input("What would you like to drink? (espresso/latte/cappuccino) ") 
    if drink == "report":
        print(f"Current resources are: \n Water: {data.resources['water']}ml \n Milk: {data.resources['milk']}ml \n Coffee: {data.resources['coffee']}g \n Money: R{money_in_machine}")
        
    elif drink == "off":
        exit()
    else:
        money(drink)

