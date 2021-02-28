from tkinter import *
from PIL import ImageTk, Image


root =Tk()
root.title('Image Viewer')
#root.iconbitmap('images/butterfly.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/cat.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/titanic.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/airline.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/rising_sun.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/koto.jpg"))

global img_pos
global my_label
global button_forward
global button_back
global image_list

img_pos = 0

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image=image_list[img_pos])
my_label.grid(row=0, column=0, columnspan=3)

def forward(img_pos, my_label, image_list):
    img_pos = img_pos+1
    if img_pos == 5:
        img_pos = 0

    my_label.grid_forget()
    my_label = Label(image=image_list[img_pos])
    my_label.grid(row=0, column=0, columnspan=3)
    

def back(img_pos, my_label, image_list):
    img_pos = img_pos-1
    if img_pos == -1:
        img_pos = 4

    my_label.grid_forget()
    my_label = Label(image=image_list[img_pos])
    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=lambda: back(img_pos, my_label, image_list))
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(img_pos, my_label, image_list))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
root.mainloop()