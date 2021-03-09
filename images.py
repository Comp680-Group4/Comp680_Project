from tkinter import *

root = Tk()
root.title('Learn to code!')
#root.iconbitmap('c:/gui/codemy.ico')



buttonQuit = Button(root, text="Exit", command=root.quit)
buttonQuit.pack()

root.mainloop()