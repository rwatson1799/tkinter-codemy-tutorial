from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    e.insert(END, number)

def button_clear():
    e.delete(0, END)

def button_operation(operation):
    first_number = e.get()
    global f_num
    global math
    math = operation
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    result = 0

    # Determine operation
    if math == "add":
        result = f_num + int(second_number)
    elif math == "subtract":
        result = f_num - int(second_number)
    elif math == "multiply":
        result = f_num * int(second_number)
    elif math == "divide":
        result = f_num / int(second_number)

    # Print result
    e.insert(0, result)

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=137, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operation("add"))
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: button_operation("subtract"))
button_multiply = Button(root, text="*", padx=41, pady=20, command=lambda: button_operation("multiply"))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_operation("divide"))
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)


# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, columnspan=3)
button_clear.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()