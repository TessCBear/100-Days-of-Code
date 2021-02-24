with open(".\Intermediate\Day 24\letter_names.txt") as letter_names:
    names = letter_names.readlines()

formatted_names = []   
for name in names:
    formatted_name = name.strip("\n")
    formatted_names.append(formatted_name)

for name in formatted_names:
    with open(".\Intermediate\Day 24\starting_letter.txt", mode="r") as starting_letter:
        data = starting_letter.read()
        replaced = data.replace("[name]", name)
    with open(f".\Intermediate\Day 24\Final Letters\{name}.txt", mode="w") as final_letter:
        final_letter.write(replaced)
