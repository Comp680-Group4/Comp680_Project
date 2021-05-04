from tkinter import *
import praw
from tkinter import scrolledtext
from numpy.distutils.tests.test_exec_command import emulate_nonposix
import SubredditSearch
import UserKeywordUsage
import UserActivityTracker

#######Can use this function to take in all user data to log in to your reddit account
def loginToRedditAccount(clientID, clientSecret, username, password, userAgent, functionToRun):
    ### If any user fields are empty, don't attempt to execute
    if(not(len(clientID) > 0) or not(len(clientSecret) > 0) or not(len(username) > 0) or not(len(password) > 0) or not(len(userAgent) > 0)):
        return
    ##Run whatever Reddit tracking function was passed
    functionToRun(clientID, clientSecret, username, password, userAgent)


##### JOSH Implementation - will call into UserKeywordUsage to track how many times a  "bag of words" is used
# in a user comment history
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
    i = 1
    listWordBoxes = []

    def createNewTextBox(ind):
        keyword = Entry(editor, width=30, borderwidth=5)
        keyword.grid(row=ind, column=1)
        keyword.insert(0, "")
        listWordBoxes.append(keyword)
        global i
        i += 1

    def executeTracking():
        wordsDict = {}
        for w in listWordBoxes:
            wordsDict[str(w.get())] = 0
            #listWords.append(str(w.get()))

        reddit = UserKeywordUsage.UserKeywordUsage(clientID, clientSecret, username, password, userAgent, str(usertoTrackEntry.get()), editor)
        reddit.searchTrackUserKeywordUsage(wordsDict)



    buttonKeywordUsage = Button(editor, text="+",
                                command= lambda: createNewTextBox(i)).grid(row=2, column=0)

    buttonExecuteTracking = Button(editor, text="Track Keywords:",
                                command= executeTracking).grid(row=2, column=5)


    root.destroy()



#### ARAHIKT part - tracks user activity in a specific subreddit. Will call into SubredditSearch to create that object
# and do the work
def createNewWindowActivityTracking(clientID, clientSecret, username, password, userAgent):
    #2nd Button in main window

    global editor
    editor = Tk()
    editor.title('Track User Activity')
    editor.geometry("650x750")
    global subredditExists
    subredditExists = False
    global userExists
    userExists = False
    userToTrack = Label(editor, text="Username To Track:").grid(row=0, column=0, sticky= E, pady=15,padx=15)
    usertoTrackEntry = Entry(editor, width=35, borderwidth=5)
    usertoTrackEntry.grid(row=0, column=1, sticky= W)
    usertoTrackEntry.insert(0, "")
    userExistLabel = Label(editor, text="")
    userExistLabel.grid(row=1, column=0,sticky=E)
    emptyLabel0 = Label(editor, text="")
    emptyLabel0.grid(row=0, column=3)

    def executeUserTracking():
        if(len(usertoTrackEntry.get())!=0):

            reddit =SubredditSearch.SubredditSearch(clientID, clientSecret, username, password, userAgent)

            userExists= reddit.searchUserExists(str(usertoTrackEntry.get()))

            if (userExists == False):
                userExistLabel.configure(text="User not found.    ", fg="#AEB6BF")
            else:
                userExistLabel.configure(text="User exists.     ", fg="#AEB6BF")
                userExists=True
        else:
            userExistLabel.configure(text="Please Enter Username.",fg="#AEB6BF" )


    searchButtonUser = Button(editor,text = "Search user", command= executeUserTracking)
    searchButtonUser.grid(row=2,column=1,sticky=W)

    emptyLabel= Label(editor, text="")
    emptyLabel.grid(row=3, column=0)

    subredditLabel = Label(editor, text="Subreddit To Search:")
    subredditLabel.grid(row=4, column=0,sticky= E, pady=15,padx=15)

    subredditTrackEntry = Entry (editor, width=35, borderwidth=5)
    subredditTrackEntry.grid(row=4, column=1, sticky= W)

    subredditTrackEntry.insert(0, "")
    subredditExistsLabel =Label (editor,text="")
    subredditExistsLabel.grid(row=5, column=0,sticky=E)


    def executeSubredditTracking():
        if (len(subredditTrackEntry.get()) != 0):

            reddit = SubredditSearch.SubredditSearch(clientID, clientSecret, username, password, userAgent)

            subredditExists= reddit.searchSubredditExists(str(subredditTrackEntry.get()))

            if (subredditExists == False):
                subredditExistsLabel.configure(text="Subreddit not found.    ", fg="#AEB6BF")
            else:
                subredditExistsLabel.configure(text="Subreddit exists.    ", fg="#AEB6BF")
                subredditExists= True
        else:
            subredditExistsLabel.configure(text="Please Enter Subreddit.", fg="#AEB6BF")

    searchButtonSubreddit = Button(editor , text= "Search Subreddit", command = executeSubredditTracking)
    searchButtonSubreddit.grid(row=6, column = 1, sticky=W)

###### change structure @@@@@@@@@@@@@@@@@@@@


    def searchUserWithSubreddit():
        text_area.delete('1.0', END)
        if((len(usertoTrackEntry.get())!=0) and (len(subredditTrackEntry.get()) != 0)):
           print("user exists:", userExists)
           #executeUserTracking()
           #executeSubredditTracking()
           if (userExistLabel.cget("text")=="User exists.     ") & ( subredditExistsLabel.cget("text")=="Subreddit exists.    "):

                print("hey")
                reddit = praw.Reddit('reddit-configuration-bot1')
                subreddit = reddit.subreddit(str(subredditTrackEntry.get()))
                username=str(usertoTrackEntry.get())
                ####### add button for time #########
                timeFiltter='day'
                results = list(subreddit.search('author:{}'.format(username), time_filter=timeFiltter))
                #############might need to change to submission
                if results:
                    for submission in results:
                        print('{} did post in {} {}!'.format(username, subreddit.display_name, timeFiltter))

                        text_area.insert(INSERT, "User Name:  " + username + "\n\n")
                        text_area.insert(INSERT, "Title:  \n" + submission.title + "\n")
                        if(len(submission.selftext)!= 0):
                            text_area.insert(INSERT, "\n" + "Text: \n" + submission.selftext + "\n")
                        text_area.insert(INSERT, "\n" + "Score: \n" + str(submission.score) + "\n *********************\n")

                else:
                    text_area.insert(INSERT, 'User Name:  {} did not post in {} in a {}!'.format(username, subreddit.display_name, timeFiltter)+"\n")
           else:
               text_area.insert(INSERT, "User or Subreddit does not exist.")

        else:
            if(len(usertoTrackEntry.get())==0):
                userExistLabel.configure(text="Please Enter Username.", fg="#AEB6BF")
            if(len(subredditTrackEntry.get()) == 0):
                subredditExistsLabel.configure(text="Please Enter Subreddit.", fg="#AEB6BF")



    emptyLabel1 = Label(editor, text="")
    emptyLabel1.grid(row=7, column=0)
    emptyLabel2 = Label(editor, text="")
    emptyLabel2.grid(row=8, column=0)
    searchButton = Button(editor, text="Search All",command = searchUserWithSubreddit)
    searchButton.grid(row=9, column=1)

    def prevPage():
        editor.destroy()
        import Configuration

    backButton = Button(editor, text="Previous Page", command=prevPage)
    backButton.grid(row=9, column=0)

    text_area_frame = Frame(editor)
    text_area_frame.grid(row=10, column=0, columnspan=3)

    text_area = scrolledtext.ScrolledText(text_area_frame, width=60, height=19, font=("Times New Roman", 13),bg="Alice blue")
    text_area.grid(row=0, column=0, pady=15, padx=15)


    root.destroy()

####SEVAK PART - will call into UserActivityTracker Class - track how many times users post over past X days.
#### UserActivityTracker needs to output a bar graph/histogram type graph to visually show this data
def createNewWindowTrackUserActivityOverTime(clientID, clientSecret, username, password, userAgent):
    #3rd Button in main window
    global editor
    editor = Tk()
    editor.title('Track User Activity Over Time')
    editor.geometry("600x300")


    #######Find the user
    #label
    #Entry(to get user name)
    #X=str(daysEntry.get())
    #Button call tro function
    #use my finction te search user

    #def fun:


    #numberOfDays=0
    #daysEntry=Entry(to get the number of days from user)
    #numberOfDays=str( daysEntry.get())
    # Button call to function


    #scrolledtext
    #insert(sdvsvd)


    #histogram

    root.destroy()



################ INITIAL WINDOW USER INTERFACE ##############################

root = Tk()
root.title('User Behaviour Tracking on Reddit')
root.geometry("600x400")

# Create Button Labels
labelKeywordUsage = Label(root, text="Track User Keyword Usage")
labelKeywordUsage.grid(row=0, column=0, padx = 20)
labelUserActivity = Label(root, text="Track User Activity in Subreddit")
labelUserActivity.grid(row=0, column=1, padx=20)
labelTrackSubmissionActivity = Label(root, text="Track User Activity Over Time")
labelTrackSubmissionActivity.grid(row=0, column=2, padx=20)

# Create Buttons to open up new window - will track keyword usage on user
buttonKeywordUsage = Button(root, text="Click Me!",
                    command=lambda: loginToRedditAccount(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get()),
                    createNewWindowKeyWordUsage), bg="brown").grid(row=4, column=0)
buttonUserActivity = Button(root, text="Search!", command=lambda: createNewWindowActivityTracking(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get())
                                                                                          ), bg="brown").grid(row=4, column=1)
buttonSubmissionActivity = Button(root, text="Click Me!", command=lambda: createNewWindowTrackUserActivityOverTime(str(clientIdEntry.get()), str(clientSecretEntry.get()), str(usernameEntry.get()), str(passwordEntry.get()), str(userAgentEntry.get())), bg="brown").grid(row=4, column=2)

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