from tkinter import *

root = Tk()

# Creating a Label widget
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0) # could do this, but not as clean
myLabel2 = Label(root, text="My Name Is Ryan Watson")
myLabel3 = Label(root, text="                      ")

# Putting it onto the screen
# myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myLabel3.grid(row=1, column=1)

root.mainloop()