from tkinter import *

def doNothing():
    print("Nothing", sep=' ', end='n', file=sys.stdout, flush=False)

root = Tk()

menuNico = Menu(root)
root.config(menu=menuNico)

subMenuNico = Menu(menuNico)
menuNico.add_cascade(label="File",menu=subMenuNico)
subMenuNico.add_command(label="New Project...", command=doNothing)
subMenuNico.add_command(label="New...",command=doNothing)
subMenuNico.add_separator()
subMenuNico.add_command(label="Exit",command=root.quit)

editMenu=Menu(menuNico)
menuNico.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Nottin",command=doNothing)


root.mainloop()
