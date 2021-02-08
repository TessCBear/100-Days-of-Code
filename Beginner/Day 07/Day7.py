import random
import art
import words

#Randomly choose a word from word_list and split into list of characters
chosen_word = random.choice(words.word_list)
chosen_word_list = list(chosen_word)

#Logo
print(art.logo)

#generate a list of the correct number of _
display = []
for letter in chosen_word:
    display += "_" #display = ['_']*len(chosen_word)
print(display)

#Allow to guess until win or lose
lives = 6
while chosen_word_list != display and lives >=0:

    print(f'You have {lives} live/s remaining')

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Choose a letter: ").lower()    
    if guess in display:
        print("You already guessed that.")

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Replace _ with letter
    letter_position = 0
    for letter in chosen_word:
        if letter == guess:
            display[letter_position] = guess
        letter_position += 1
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1
        if lives == -1:
            print(f"No. The word was {chosen_word}. You lose")
            exit()
    print("\n" + ' '.join(display))
    print("\n" + art.stages[lives])

print(f"Yes! The word was {chosen_word}. You win")
