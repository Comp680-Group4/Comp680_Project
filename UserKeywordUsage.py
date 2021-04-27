import praw
import re


class UserKeywordUsage:
    def __init__(self, clientID, clientSecret, username, password, userAgent, userToTrack):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.username = username
        self.password = password
        self.userAgent = userAgent
        self.userToTrack = userToTrack

        self.reddit = praw.Reddit(client_id = self.clientID, client_secret = self.clientSecret, username = self.username, password = self.password, user_agent = self.userAgent)


        ####TODO - add in fields for the user data that we're trying to track
        #self.usernameToTrack

    def countOccurences(self, str, word):
        # split the string by spaces in a
        a = str.split(" ")

        # search for pattern in a
        count = 0
        for i in range(0, len(a)):

            # if match found increase count
            if (word.lower() == a[i].lower()):
                count = count + 1

        return count

    # This will take in all the user data, a number of "words", and then track how many times user has used those
    #   specific words in all posts they have made on reddit ever.
    # Out put will be a pie graph denoting precentages of how often they
    #   have used those words relative to the other words
    def searchTrackUserKeywordUsage(self, wordsDict):
        #redditor/person is of type subreddit
        person = self.reddit.redditor(self.userToTrack)
        comments = []
        for comment in person.comments.new(limit=50):
            comments.append(comment.body)
            #print(comment.body.split("\n", 1)[0][:79])

        keys_list = list(wordsDict)

        for comment in comments:

            #wordIndex = 0
            for word in keys_list:
                #key = keys_list[wordIndex]
                i = self.countOccurences(comment, word)
                #wordIndex += 1
                wordsDict[word] += i

        print(*comments, sep="\n")
        print(wordsDict)
        #comments = redditor.comments.new(limit=50)
        #print(person.link_karma)
        #print("Called into function for tracking user keyword usage!")

    def countOccurences(self, str, word):
        # split the string by spaces in a
        a = str.split(" ")

        # search for pattern in a
        count = 0
        for i in range(0, len(a)):

            # if match found increase count
            if (word.lower() == a[i].lower()):
                count = count + 1

        return count