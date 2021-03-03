# Day 28 of 100 Days of Code
## Pomodoro Timer

Today's lesson allowed us to practise more of the *tkinter* module and learn about the canvas feature. The lesson took form of a step-by-step project in which we created a timer to be used for the Pomodoro technique of productivity. 

The canvas used in the project was created with the following code:
```python
# Create a canvas with a background colour and no border
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)

# Insert the tomato image into the canvas
tomato_img = PhotoImage(file=".\Intermediate\Day 28\\tomato.png")
canvas.create_image(100, 112, image = tomato_img)

# Insert text into the canvas
timer_text = canvas.create_text(108, 130, text = "00:00", fill = "white", font = ("Courier", 30, "bold"))

# Position the canvas using grid
canvas.grid(column = 1, row = 1)
```
It was a fun project and got me much more familiar with using a canvas and *tkinter*. The implementation of the timer was the most interesting to get correct.