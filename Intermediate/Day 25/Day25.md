# Day 25 Of 100 Days of Code
## US Guessing Game

Today's lesson was an introduction to the *Pandas* module. Wow, what an incredible module that does **so** much!

The first thing we did was to play around with *.csv* file types. In particular, we worked with a squirrel census from central park in 2018. (Who knew there were so many squirrels?) We had to use the ginormous data file and extract the number of each colour of squirrel:

```python
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
```
The final project of the day was to create a United States guessing game. A map with no labels appears, and the user must guess as many states as they can. As a state is correctly guessed, the name appears over the correct location.

