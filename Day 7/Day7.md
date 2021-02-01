# Day 7 of 100 Days of Code
## Hangman

I made it through the first week! I'm so proud of myself.

Today's lesson was a bit different because there was no new concept taught. Everything was focussed around creating a game of Hangman. This was done in 5 stages:

1. Picking a random word from a list and checking if a user's guessed letter is in the word.

2. Creating a display of the correct number of blank spaces and replacing with correct guesses.

```python
display = []
for letter in chosen_word:
    display += "_"
print(display)

letter_position = 0
    for letter in chosen_word:
        if letter == guess:
            display[letter_position] = guess
        letter_position += 1
```
3. Checking if the player has one and repeating the guessing process if not.

4. Keeping track of the player's lives and displaying the correct progression of the drawing. 

```python
lives = 6
while chosen_word_list != display and lives >=-1:

    guess = input("Choose a letter: ").lower()    

    letter_position = 0
    for letter in chosen_word:
        if letter == guess:
            display[letter_position] = guess
        letter_position += 1
    if guess not in chosen_word:
        lives -= 1
        if lives == -1:
            print("You lose")
            break
    print(display)
    print(art.stages[lives])


print("You win")
```
5. Finally, improving the user experience.

I found step 4 the hardest to do. I had a lot of challenges with making it stop asking for guesses when the user had lost and with displaying the correct drawing. 

I don't think my code came out as elegant as the solution given by Dr Angela Yu, but it works and I learnt a lot. This challenge really tested my ability to apply everything I'd learnt and make it work. I'm proud of how far I've come. 

On to week 2!