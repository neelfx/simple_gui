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

img_pos = 0

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
status = Label(root, text= "Image " + str(img_pos) + " of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=image_list[img_pos])
my_label.grid(row=0, column=0, columnspan=3)

def forward():
    global img_pos, my_label, image_list, status
    img_pos += 1
    if img_pos == 5:
        img_pos = 0
    print(img_pos)
    my_label.grid_forget()
    my_label = Label(image=image_list[img_pos])
    my_label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text= "Image " + str(img_pos+1) + " of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back():
    global img_pos, my_label, image_list, status
    img_pos -= 1
    print(img_pos)
    if img_pos == -1:
        img_pos = 4

    my_label.grid_forget()
    my_label = Label(image=image_list[img_pos])
    my_label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text= "Image " + str(img_pos+1) + " of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<-", command=back)
button_quit = Button(root, text="Close Program", command=root.quit)
button_forward = Button(root, text="->", command=forward)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()