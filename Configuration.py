from tkinter import *
import praw
import SubredditSearch
import UserKeywordUsage
import UserActivityTracker

def loginToRedditAccount(clientID, clientSecret, username, password, userAgent, functionToRun):
    ### If any user fields are empty, don't attempt to execute
    if(not(len(clientID) > 0) or not(len(clientSecret) > 0) or not(len(username) > 0) or not(len(password) > 0) or not(len(userAgent) > 0)):
        return
    ##Run whatever Reddit tracking function was passed
    functionToRun(clientID, clientSecret, username, password, userAgent)

def createNewWindowKeyWordUsage(clientID, clientSecret, username, password, userAgent):
    #1st Button in main window
    #This will open up window to input stuff for the mechanic "Track User Keyword Usage"

    global editor
    editor = Tk()
    editor.title('Track User Keyword Usage')
    editor.geometry("1000x600")

    userToTrackLabel = Label(editor, text="Username to Track").grid(row=0, column=0)
    usertoTrackEntry = Entry(editor, width=30, borderwidth=5)
    usertoTrackEntry.grid(row=0, column=1)
    usertoTrackEntry.insert(0, "")

    global i
    i = 0
    listWordBoxes = []

    def createNewTextBox(ind):
        keyword = Entry(editor, width=30, borderwidth=5)
        keyword.grid(row=ind, column=3)
        keyword.insert(0, "")
        listWordBoxes.append(keyword)
        global i
        i += 1

    def executeTracking():
        reddit = UserKeywordUsage.UserKeywordUsage(clientID, clientSecret, username, password, userAgent, str(usertoTrackEntry.get()))
        reddit.searchTrackUserKeywordUsage()


    buttonKeywordUsage = Button(editor, text="+",
                                command= lambda: createNewTextBox(i)).grid(row=1, column=2)

    buttonExecuteTracking = Button(editor, text="Track Keywords:",
                                command= executeTracking).grid(row=2, column=5)


    root.destroy()

def createNewWindowActivityTracking(clientID, clientSecret, username, password, userAgent):
    #2nd Button in main window

    global editor
    editor = Tk()
    editor.title('Track User Activity')
    editor.geometry("400x600")

    userToTrack = Label(editor, text="Username to Track").grid(row=0, column=0)
    usertoTrackEntry = Entry(editor, width=30, borderwidth=5)
    usertoTrackEntry.grid(row=0, column=1)
    usertoTrackEntry.insert(0, "")

    def executeTracking():
        reddit =SubredditSearch.SubredditSearch(clientID, clientSecret, username, password, userAgent)

        reddit.searchUserDataInSubreddit()
        reddit.searchUserExists(str(usertoTrackEntry.get()))

        userExistLabel= Label(editor, text=" ")
        userExistLabel.grid(row=1, column=0)

        if (reddit.userExists == False):
            userExistLabel.configure(text="User not found.")
        else:
            userExistLabel.configure(text="User exists.")


    searchButton = Button(editor,text = "Search user", command= executeTracking())
    searchButton.grid(row=2,column=1)

    root.destroy()

def createNewWindowSubredditActivity(clientID, clientSecret, username, password, userAgent):
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
    r = SubredditSearch.Reddit(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get()))

    buttonSubmissionActivity = Button(editor, text="Fetch Posts", command=lambda: r.searchSubreddit(str(subredditNameEntry.get()), str(subredditCategoryEntry.get()), int(submissionLimitEntry.get()))).grid(row=9,
                                                                                                             column=2)

    root.destroy()



################ INITIAL WINDOW USER INTERFACE ##############################

root = Tk()
root.title('User Behaviour Tracking on Reddit')
root.geometry("600x400")

# Create Button Labels
labelKeywordUsage = Label(root, text="Track User Keyword Usage")
labelKeywordUsage.grid(row=0, column=0, padx = 20)
labelUserActivity = Label(root, text="Track User Activity")
labelUserActivity.grid(row=0, column=1, padx=20)
labelTrackSubmissionActivity = Label(root, text="Track A Single Submission")
labelTrackSubmissionActivity.grid(row=0, column=2, padx=20)

# Create Buttons to open up new window - will track keyword usage on user
buttonKeywordUsage = Button(root, text="Click Me!",
                    command=lambda: loginToRedditAccount(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get()),
                    createNewWindowKeyWordUsage), bg="brown").grid(row=4, column=0)
buttonUserActivity = Button(root, text="Search!", command=lambda: createNewWindowActivityTracking(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get())
                                                                                          ), bg="brown").grid(row=4, column=1)
buttonSubmissionActivity = Button(root, text="Click Me!", command=createNewWindowSubredditActivity, bg="brown").grid(row=4, column=2)

clientIdLabel = Label(root, text="Enter Client ID:").grid(row=8, column=0)
clientIdEntry = Entry(root, width=30, borderwidth=5)
clientIdEntry.grid(row=8, column=1)
clientIdEntry.insert(0, "J8BdcKH3pAoZ5g")

clientSecretLabel = Label(root, text="Enter Client Secret:").grid(row=9, column=0)
clientSecretEntry = Entry(root, width=30, borderwidth=5)
clientSecretEntry.grid(row=9, column=1)
clientSecretEntry.insert(0, "XSYxzeI8w-qQTFBJxraUHdzarAelOQ")

usernameLabel = Label(root, text="Enter Username:").grid(row=10, column=0)
usernameEntry = Entry(root, width=30, borderwidth=5)
usernameEntry.grid(row=10, column=1)
usernameEntry.insert(0, "FallenGalaxies123")

passwordLabel = Label(root, text="Enter Password:").grid(row=11, column=0)
passwordEntry = Entry(root, width=30, borderwidth=5)
passwordEntry.grid(row=11, column=1)
passwordEntry.insert(0, "Cronosphere123!")

userAgentLabel = Label(root, text="Enter User Agent:").grid(row=12, column=0)
userAgentEntry = Entry(root, width=30, borderwidth=5)
userAgentEntry.grid(row=12, column=1)
userAgentEntry.insert(0, "comp680project")

root.mainloop()

################ END INITIAL WINDOW ##############################
