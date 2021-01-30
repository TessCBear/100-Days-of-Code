import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#easy level (no random order)
password_letters = ""
for letter in range(1, nr_letters+1):
    letter = random.choice(letters)
    password_letters += letter

password_symbols = ""
for symbol in range(1, nr_symbols+1):
    symbol = random.choice(symbols)
    password_symbols += symbol

password_numbers = ""
for number in range(1, nr_numbers+1):
    number = random.choice(numbers)
    password_numbers += number

easy_password = password_letters + password_symbols + password_numbers
print(f"Your (easy) password is: " + easy_password)    

#harder level (randomised order)
hard_password_list = []

for letter in range(1, nr_letters+1):
    letter = random.choice(letters)
    hard_password_list += letter

password_symbols = ""
for symbol in range(1, nr_symbols+1):
    symbol = random.choice(symbols)
    hard_password_list += symbol

password_numbers = ""
for number in range(1, nr_numbers+1):
    number = random.choice(numbers)
    hard_password_list += number

random.shuffle(hard_password_list)


hard_password = ""
for character in hard_password_list:
    hard_password += character

print("Your (harder to crack) password is: " + hard_password)
