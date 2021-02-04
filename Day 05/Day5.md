# Day 5 of 100 Days of Code
## Password Generator

Today's lesson was all about *for* loops. This has often been a topic that confused me, so I was grateful for the very clear explanations from Angela. 

The first exercises involved taking the *len()*, *sum()* and *min()* or *max()* functions and using a *for* loop to reproduce what each function does. It was interesting to see what happens "behind the scenes" of each function.

```python
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

add = 0
length = 0
for n in student_heights:
    add += n
    length += 1

average = round(add / length)
print(f"There are {length} heights. The average is {average}.")
```
The above code could equivalently have been done as:
```python
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

add = sum(student_heights)
length = len(student_heights)

average = round(add / length)
print(f"There are {length} heights. The average is {average}.")
```

I also coded the classic "FizzBuzz" game. This was something I had done before so I didn't find it too hard.

The final project of the day was to create a random password generator. There were two "levels" of password. The easy level is more susceptible to cracking since it just cobmined a set number of letters, numbers and symbols in a string. The harder level is much more difficult to crack since it randomised the order of the characters too. It was challenging to figure out how to put everything together and randomise it, but I got there in the end.