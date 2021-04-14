from tkinter import *
import RedditModule

root = Tk()
root.title('User Behaviour Tracking on Reddit')
root.geometry("600x400")

def createNewWindowKeyWordUsage():
    #1st Button in main window
    #This will open up window to input stuff for the mechanic "Track User Keyword Usage"

    global editor
    editor = Tk()
    editor.title('Track User Keyword Usage')
    editor.geometry("600x300")

    clientIdLabel = Label(editor, text="Enter Client ID:").grid(row=0, column=0)
    clientIdEntry = Entry(editor, width=30, borderwidth=5)
    clientIdEntry.grid(row=0, column=1)
    clientIdEntry.insert(0, "J8BdcKH3pAoZ5g")

    clientSecretLabel = Label(editor, text="Enter Client Secret:").grid(row=1, column=0)
    clientSecretEntry = Entry(editor, width=30, borderwidth=5)
    clientSecretEntry.grid(row=1, column=1)
    clientSecretEntry.insert(0, "XSYxzeI8w-qQTFBJxraUHdzarAelOQ")

    usernameLabel = Label(editor, text="Enter Username:").grid(row=2, column=0)
    usernameEntry = Entry(editor, width=30, borderwidth=5)
    usernameEntry.grid(row=2, column=1)
    usernameEntry.insert(0, "FallenGalaxies123")

    passwordLabel = Label(editor, text="Enter Password:").grid(row=3, column=0)
    passwordEntry = Entry(editor, width=30, borderwidth=5)
    passwordEntry.grid(row=3, column=1)
    passwordEntry.insert(0, "Cronosphere123!")

    userAgentLabel = Label(editor, text="Enter User Agent:").grid(row=4, column=0)
    userAgentEntry = Entry(editor, width=30, borderwidth=5)
    userAgentEntry.grid(row=4, column=1)
    userAgentEntry.insert(0, "comp680project")



    root.destroy()

def createNewWindowActivityTracking():
    #2nd Button in main window
    global editor
    editor = Tk()
    editor.title('Track User Activity')
    editor.geometry("400x600")
    root.destroy()

def createNewWindowSubredditActivity():
    #3rd Button in main window
    global editor
    editor = Tk()
    editor.title('Track User Keyword Usage')
    editor.geometry("600x300")


    clientIdLabel = Label(editor, text="Enter Client ID:").grid(row=0, column=0)
    clientIdEntry = Entry(editor, width=30, borderwidth=5)
    clientIdEntry.grid(row=0, column=1)
    clientIdEntry.insert(0, "J8BdcKH3pAoZ5g")

    clientSecretLabel = Label(editor, text="Enter Client Secret:").grid(row=1, column=0)
    clientSecretEntry = Entry(editor, width=30, borderwidth=5)
    clientSecretEntry.grid(row=1, column=1)
    clientSecretEntry.insert(0, "XSYxzeI8w-qQTFBJxraUHdzarAelOQ")

    usernameLabel = Label(editor, text="Enter Username:").grid(row=2, column=0)
    usernameEntry = Entry(editor, width=30, borderwidth=5)
    usernameEntry.grid(row=2, column=1)
    usernameEntry.insert(0, "FallenGalaxies123")

    passwordLabel = Label(editor, text="Enter Password:").grid(row=3, column=0)
    passwordEntry = Entry(editor, width=30, borderwidth=5)
    passwordEntry.grid(row=3, column=1)
    passwordEntry.insert(0, "Cronosphere123!")

    userAgentLabel = Label(editor, text="Enter User Agent:").grid(row=4, column=0)
    userAgentEntry = Entry(editor, width=30, borderwidth=5)
    userAgentEntry.grid(row=4, column=1)
    userAgentEntry.insert(0, "comp680project")

    subredditNameLabel = Label(editor, text="Enter Subreddit Name:").grid(row=6, column=0)
    subredditNameEntry = Entry(editor, width=30, borderwidth=5)
    subredditNameEntry.grid(row=6, column=1)
    subredditNameEntry.insert(0, "python")

    subredditCategoryLabel = Label(editor, text="Enter Subreddit Category:").grid(row=7, column=0)
    subredditCategoryEntry = Entry(editor, width=30, borderwidth=5)
    subredditCategoryEntry.grid(row=7, column=1)
    subredditCategoryEntry.insert(0, "hot")

    submissionLimitLabel = Label(editor, text="Enter Submission Limit:").grid(row=8, column=0)
    submissionLimitEntry = Entry(editor, width=30, borderwidth=5)
    submissionLimitEntry.grid(row=8, column=1)
    submissionLimitEntry.insert(0, "5")

    #print(clientIdEntry.get())
    r = RedditModule.Reddit(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get()))

    buttonSubmissionActivity = Button(editor, text="Fetch Posts", command=lambda: r.searchSubreddit(str(subredditNameEntry.get()), str(subredditCategoryEntry.get()), int(submissionLimitEntry.get()))).grid(row=9,
                                                                                                             column=2)

    root.destroy()










# Create Button Labels
labelKeywordUsage = Label(root, text="Track User Keyword Usage")
labelKeywordUsage.grid(row=0, column=0, padx = 20)
labelUserActivity = Label(root, text="Track User Activity")
labelUserActivity.grid(row=0, column=1, padx=20)
labelTrackSubmissionActivity = Label(root, text="Track A Single Submission")
labelTrackSubmissionActivity.grid(row=0, column=2, padx=20)

# Create Buttons to open up new window - will track keyword usage on user
buttonKeywordUsage = Button(root, text="Click Me!", command=createNewWindowKeyWordUsage).grid(row=4, column=0)
buttonUserActivity = Button(root, text="Click Me!", command=createNewWindowActivityTracking).grid(row=4, column=1)
buttonSubmissionActivity = Button(root, text="Click Me!", command=createNewWindowSubredditActivity).grid(row=4, column=2)

root.mainloop()