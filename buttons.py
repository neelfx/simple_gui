# Testing buttons on Tkinter

from tkinter import *

root = Tk()
def myClick():
    myLabel = Label(root, text="Look! I click a Button!!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=500, pady=500, command=myClick, fg="blue", bg="red")
myButton.pack()

# Create Event Loop
root.mainloop()

