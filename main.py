from tkinter import *

root = Tk()

def test():
    print("Test")

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


Dropdownmenu = Menu(root)
root.config(menu=Dropdownmenu)
Submenu = Menu(Dropdownmenu)
Dropdownmenu.add_cascade(label="File", menu=Submenu)
Submenu.add_command(label="New", command=test)
Submenu.add_command(label="Save", command=test)
Submenu.add_command(label="Load", command=test)

Dropdownmenu.add_cascade(label="Edit", menu=Submenu)

toolbar = Frame(root, bg="blue")
insertButton = Button(toolbar, text="Insert Image",command=test)
insertButton.pack(side=LEFT,padx=2,pady=2)
printButton = Button(toolbar, text="Print",command=test)
printButton.pack(side=LEFT,padx=2,pady=2)
toolbar.pack()  #(side=TOP, fill=X)

root.mainloop()
#lol
