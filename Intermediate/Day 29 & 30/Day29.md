# Day 29 of 100 Days of Code
## Password Manager

Today we continued to learn about *tkinter* and used it to create a program which takes in a Website, Username and Password, and stores them to a text file. The program is also able to generate a secure password using the code from Day 5. The new element of *tkinter* learnt today was how to make pop-up message boxes of various types. This was used to confirm a user's details and to warn a user if cells were not completed.

```python
messagebox.askokcancel(title = website_data, message=f"Add these details? \nUsername: {username_data} \nPassword: {password_data}")

messagebox.showwarning(title = "Invalid", message = "Missing information")
```

I enjoyed this project and look forward to adding to its functionality tomorrow.