from tkinter import *

root = Tk()
root.geometry("200x200")


label_1 = Label(root, text="Name:")
label_2 = Label(root, text="Password:")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0,column=0,sticky=E)
label_2.grid(row=1,column=0,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

button_1 = Checkbutton(root, text="Keep me logged in")
button_2 = Button(root, text="Login")

button_1.grid(columnspan=2)
button_2.grid(columnspan=2)

root.mainloop()
#lol
