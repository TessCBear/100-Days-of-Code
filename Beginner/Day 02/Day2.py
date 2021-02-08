#Welcome Message
print('Welcome to the Tip Calculator')

#Asks for bill amount
bill_total = round(float(input('What was the bill amount? R')) , 2)

#Asks for percentage tip
tip_percentage = float(input('What percentage would you like to tip? '))
actual_percentage = tip_percentage / 100 + 1

#Number of people splitting
splits = int(input('How many people are splitting the bill? '))

#Each person pays
#Had to use the "{:.2f}".format() to get it to put all of the decimals even when there are no cents eg. put R24.00 not just R24.0
each = "{:.2f}".format(bill_total * actual_percentage / splits)
print(f"Each person should pay R{each}")
