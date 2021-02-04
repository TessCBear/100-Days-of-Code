# Day 9 of 100 Days of Code
# Secret Auction

Today's lesson was all about dictionaries in python. Funnily enough, I actually have worked with dictonaries before and didn't realise. It makes a lot more sense now that I understand how to manipulate them! The first thing we learnt was the basic structure of a dictionary and how to index them:

```python
#A basic dictionary 
dictionary = {
    Key1 : Value1, 
    Key2 : Value2, 
    }

#Indexing a key
dictionary[Key]
```
The next thing we learnt was how to create empty dictionaries, new entries, and wipe an entire dictionary:
```python
#Create empty dictionary
empty = {}

#Add to existing dictionary
dictionary["new entry"] = "content"

#wipe entire dictionary
dictionary = {}
```

Finally, we saw how to nest dictionaries and lists inside other dictionaries and lists.

Nesting
```python
travel_log = {
    "France" : ["Paris" , "Lille", "Dijon"],
    "Germany" : {
        "Visits" : 1
        "Cities" : ["Berlin", "Hamburg"]
    }
}
```
The final product for the day was to create a Secret Auction. One person at a time enters their name and a bid, which stores into a dictionary before the screen clears and the next person enters their details. The program then calculates who bid the most and won the auction.