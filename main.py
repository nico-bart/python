from tkinter import *

root = Tk()

<<<<<<< HEAD
def test():
    print("Test")
=======
def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")
>>>>>>> 534c80ee8a0c049d3b6d5984af2e4a7c3ecfc17b

# label_1 = Label(root, text="Name:")
# label_2 = Label(root, text="Password:")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0,column=0,sticky=E)
# label_2.grid(row=1,column=0,sticky=E)
# entry_1.grid(row=0,column=1)
# entry_2.grid(row=1,column=1)
#
# button_1 = Checkbutton(root, text="Keep me logged in")
# button_2 = Button(root, text="Login")
#
# button_1.grid(columnspan=2)
# button_2.grid(columnspan=2)


<<<<<<< HEAD
Dropdownmenu = Menu(root)
root.config(menu=Dropdownmenu)
Submenu = Menu(Dropdownmenu)
Dropdownmenu.add_cascade(label="File", menu=Submenu)
Submenu.add_command(label="New", command=test)
Submenu.add_command(label="Save", command=test)
Submenu.add_command(label="Load", command=test)
=======
button_1 = Checkbutton(root, text="Keep me logged in")
button_2 = Button(root, text="Login")
button_2.bind("<Button-1>", leftClick)
button_2.bind("<Button-3>", rightClick)
>>>>>>> 534c80ee8a0c049d3b6d5984af2e4a7c3ecfc17b

Dropdownmenu.add_cascade(label="Edit", menu=Submenu)

toolbar = Frame(root, bg="blue")
insertButton = Button(toolbar, text="Insert Image",command=test)
insertButton.pack(side=LEFT,padx=2,pady=2)
printButton = Button(toolbar, text="Print",command=test)
printButton.pack(side=LEFT,padx=2,pady=2)
toolbar.pack()  #(side=TOP, fill=X)

root.mainloop()
#lol
