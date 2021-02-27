import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.config(padx = 50, pady=50)

input = tkinter.Entry()
input.grid(column=1, row=0)

miles_label = tkinter.Label(text = "Miles")
miles_label.grid(column = 2, row=0)

equal_label = tkinter.Label(text = "is equal to")
equal_label.grid(column = 0, row = 1)

kilometers = tkinter.Label(text = "0")
kilometers.grid(column = 1, row = 1)

kilometers_label = tkinter.Label(text = "Km")
kilometers_label.grid(column = 2, row = 1)

def convert():
    miles = int(input.get())
    km = str(miles * 1.609)
    kilometers.config(text = km )

calculate = tkinter.Button(text = "Calculate", command = convert)
calculate.grid(column = 1, row = 2)

window.mainloop()