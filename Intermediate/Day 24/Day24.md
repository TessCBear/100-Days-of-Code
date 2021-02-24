# Day 24 of 100 Days of Code
## Mail Merge

Today's lesson focussed on files, directories and paths. The first thing was how to read and write to files using Python:

```python
# Open and read a file
file = open(".\Intermediate\Day 24\my_file.txt")
contents = file.read()
print(contents)
file.close()

# Open and read a file (no need to remember to close)
with open(".\Intermediate\Day 24\my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write over the current file
with open(".\Intermediate\Day 24\my_file.txt", mode = "w") as file:
    file.write("This text will replace everything in the file")
    
# Append to the current file
with open(".\Intermediate\Day 24\my_file.txt", mode = "a") as file:
    file.write("This will be appended to the end.")
```

We then used these new skills to modify our Snake Game. Using a new data file, we could save a highscore of all time. 

The project of the day used the skills again to make a personalised version of the same letter for a number of people:

```
Dear [name]

I'm having a party on Saturday. Please come.

Thanks,
Tessa
```
It took a bit of thinking, but overall was not a difficult task to achieve. It's interesting to see how something like that is done!