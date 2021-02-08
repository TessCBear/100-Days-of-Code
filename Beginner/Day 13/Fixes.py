# Describe Problem
def my_function():
  for i in range(1, 21): #Range excludes the last number, so needs to be one more than you think
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #By testing each case you can see it happens when dice_num is 6 since indices start from 0. Edit the range to correspond.
print(dice_imgs[dice_num]) 

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: #When 1994 is entered, there is no instruction. Should be >= 1994 (or <= 1994 above)
  print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?")) #needs to be an int so we can do comparisons later
if age > 18:
    print(f"You can drive at age {age}.") #Indentation error and not an f-string so {} wont input age variable

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(f"Pages is {pages}")
word_per_page = int(input("Number of words per page: "))
print(f"Words per page is {word_per_page}") #Use print statements to see that the variable word_per_page wasn't changing
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) #Using the debugger, you can see it was not going into this every time, just at the end.
  print(b_list)

mutate([1,2,3,5,8,13])