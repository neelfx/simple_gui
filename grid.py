# Testing grid layout on Tkinter

from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Label 1")
myLabel2 = Label(root, text="Label 2")
myLabel3 = Label(root, text="                                       ")
myLabel4 = Label(root, text="Label 2")
# Shoving it onto the screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=2)
myLabel4.grid(row=1, column=3)


# Create Event Loop
root.mainloop()

