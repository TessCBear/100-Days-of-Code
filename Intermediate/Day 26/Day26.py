import pandas

data = pandas.read_csv(".\Intermediate\Day 26\\nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
phonetic = [phonetic_dictionary[letter] for letter in word]
print(phonetic)

