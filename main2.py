from tkinter import *

class NicosButtons:

    def __init__(self, master):
        frame = Frame(master=root, cnf={})
        frame.pack()
        self.printButton = Button(master=frame, text="Printed",command=self.printMessage, cnf={})
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(master=frame, text="Quit",command=frame.quit,cnf={})
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow this worked")


root = Tk()
b = NicosButtons(root)
root.mainloop()
