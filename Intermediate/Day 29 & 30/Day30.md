# Day 30 of 100 Days of Code
## Password Manager

Today we continued the work on the password manager from yesterday with added improvements. The topic of the lesson today was Errors and Exceptions and Json. We learnt about the *try, except, else, finally* blocks of code which allow for checking of exceptions without an error stopping the code.

```python
Try: something that might cause an exception
try: 
    file = open(".\Intermediate\Day 29 & 30\\a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["non_existent_key"])
    
#Except: do this if there was an exception. If an exception is found, it will run that particular block of except and then go to finally (or exit if no finally)
except FileNotFoundError:
    file = open(".\Intermediate\Day 29 & 30\\a_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")

#Else: Do this if there were no exceptions
else:
    content = file.read()
    print(content)

#Finally: Do this no matter what
finally:
    file.close()
    print("File was closed")
```

We used json to create a better storage of the password data which could then be searched for via the GUI. Using exception blocks, we made sure that if a user searched for a non-existent file or non-existent password, a different pop-up would appear. If a user searched for a password in the json file, the data was displayed in a pop-up.