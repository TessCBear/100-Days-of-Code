import pandas

data = pandas.read_csv(".\Intermediate\Day 26\\nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

def nato_conversion():
    word = input("Enter a word: ").upper()
    try:
        phonetic = [phonetic_dictionary[letter] for letter in word]
        print(phonetic)
    except KeyError:
        print("Please only use letters of the alphabet.")
        nato_conversion()
    
nato_conversion()

