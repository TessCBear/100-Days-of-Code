# Day 3 of 100 Days of Code
## Treasure Island

Today's focus was all about conditional statements. The course started with basic *if else* loops and progressively got more complicated. I made a leap year calculator and learnt that the conditions of leap years are not just "every four years". I won't lie, this lesson really challenged my brain and took a lot of thinking power especially when the loops started becoming more and more nested.

```python
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  ```
  
  I also made an old fashioned "love calculator" which combined my new conditional statement skills with all of the previous string combination skills from days 1 and 2. 
  
  The day's challenge really allowed for some creativity and fun. Using conditional statements, I created a simple text-based choice game. The user must make decisions to find the hidden treasure. It was really fun to try and play around with the decisions and make sure every option worked. I also really enjoyed the freedom in making the game unique to me.
