# Day 17 of 100 Days of Code
## Quiz 

I've really fallen behind! I will make the time to catchup as soon as I can, life just got crazy.

Today's lesson continued the learning on Object Oriented Programming (OOP). I learnt how to make classes which I can then use to construct objects. 

To make attributes for a class, the *init* or *initialise* function is required and methods are made as separate functions as needed. For example, a basic social media platform which has users that follow one another may have a user class as follows:

```python
class User:
    
    # Initialise attributes
    def __init__(self, id, name): 
        self.id = id
        self.username = name
        self.followers = 0 
        self.following = 0 

    # Creating methods
    def follow(self, user): 
        user.followers += 1
        self.following += 1
```

We then applied this knowledge to the programme for the day. Our quiz presents trivia True/False questions to the user and then keeps track of score until the end. This could have been done using methods previously learnt, but OOP allowed for a much cleaner version of the program. It also meant that if we changed the questions, not much would have to be changed at all for the programme to continue working.