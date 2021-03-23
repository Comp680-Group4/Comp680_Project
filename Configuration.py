from tkinter import *

root = Tk()
root.title('User Behaviour Tracking on Reddit')
root.geometry("400x600")

def createNewWindowActivityTracking():
    global editor
    editor = Tk()
    editor.title('Track User Activity')
    editor.geometry("400x600")




    root.destroy()

def createNewWindowKeyWordUsage():
    global editor
    editor = Tk()
    editor.title('Track User Keyword Usage')
    editor.geometry("600x300")

    usernameLabel = Label(editor, text = "Enter Username:").grid(row=0,column=0)
    usernameEntry = Entry(editor, width=30, borderwidth=5).grid(row=0,column=1)

    numWords = Label(editor, text="Enter Number of Words to Track:").grid(row=1, column=0)
    numWordsEntry = Entry(editor, width=30, borderwidth=5).grid(row=1, column=1)
    root.destroy()

# Create Button Labels
labelKeywordUsage = Label(root, text="Track User Keyword Usage")
labelKeywordUsage.grid(row=0, column=0, padx = 20)
labelUserActivity = Label(root, text="Track User Activity")
labelUserActivity.grid(row=0, column=1, padx=20)

# Create Buttons to open up new window - will track keyword usage on user
buttonKeywordUsage = Button(root, text="Click Me!", command=createNewWindowKeyWordUsage).grid(row=4, column=0)
buttonUserActivity = Button(root, text="Click Me!", command=createNewWindowActivityTracking).grid(row=4, column=1)


root.mainloop()