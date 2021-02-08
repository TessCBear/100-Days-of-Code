# Day 12 of 100 Days of Code
# Guess the Number

Today's lesson was about scopes, both local and global. I learnt about how variables will only be locally defined inside a function and therefore won't be accessible outside of a function. I also learnt that this does not apply to other blocks like *if* statements and loops. For example:

```python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # new_enemy is accessible outside of the if
```

```python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy) # new_enemy is not accessible outside of create_enemy()
```

I also learnt how to access and edit a global variable within a local scope. However, this method must be used with caution since it's not always a good idea to change a global variable. For this reason, global constants are usually written in all caps so that one remembers not to change them.

```python
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
```
The project for the day was a more complex version of something I've previously coded. The computer randomly chooses a number between 1 and 100 and the user must guess this number. If the user is wrong, the computer responds with a "higher" or "lower" until the user guesses correctly. This program also included two levels - easy and hard - with different numbers of lives accordingly.