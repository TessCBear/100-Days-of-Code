print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type a shift number between 0 and 25:\n"))

def caesar(text, shift, direction):
    message = ""
    if direction == "encode":
        for letter in text:
            if letter == " " or letter == "." or letter == "!" or letter =="," or letter == "?":
                message += letter
            else:
                current_index = alphabet.index(letter)
                new_index = current_index + shift
                if new_index > 25:
                    new_index -= 26
                letter_coded = alphabet[new_index]
                message += letter_coded
        print(message)
    else:
        for letter in text:
            if letter == " " or letter == "." or letter == "!" or letter =="," or letter == "?":
                message += letter
            else:
                current_index = alphabet.index(letter)
                new_index = current_index - shift
                letter_coded = alphabet[new_index]
                message += letter_coded
        print(message)

caesar(text, shift, direction)