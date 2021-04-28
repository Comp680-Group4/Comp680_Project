import praw
from tkinter import *
from prawcore.exceptions import NotFound

class SubredditSearch:
    def __init__(self, clientID, clientSecret, username, password, userAgent):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.username = username
        self.password = password
        self.userAgent = userAgent
        self.reddit = praw.Reddit(client_id = self.clientID, client_secret = self.clientSecret, username = self.username, password = self.password, user_agent = self.userAgent)

    def searchUserExists(self, username):
        userExists=False
        try:
            reddit = praw.Reddit('reddit-configuration-bot1')
            reddit.redditor(username).id
            #self.reddit.user
        except NotFound:
            userExists=False
            return userExists
        userExists=True
        return userExists

    def searchSubredditExists(self, subreddit):
        #subredditExists= False
        exists = False
        try:
            reddit = praw.Reddit('reddit-configuration-bot1')
            reddit.subreddits.search_by_name(subreddit, exact=True)
        except NotFound:
            exists = False
            return exists
        exists= True
        return exists

        #print("reddit.Exists in subsearch:", reddit.userExists)

        ####TODO - add in fields for the user data that we're trying to track
        #self.usernameToTrack

    def searchSubreddit(self, subredditName, subredditCategory, submissionLimit):
        #define subreddit object
        subreddit = self.reddit.subreddit(subredditName)

        #figure out what subcategory of the subreddit to search, default will be 'hot'
        category = subreddit.hot(limit = int(submissionLimit))
        if subredditCategory == "hot":
            category = subreddit.hot(limit=int(submissionLimit))
        elif subredditCategory == "new":
            category = subreddit.new(limit = submissionLimit)
        elif subredditCategory == "controversial":
            category = subreddit.controversial(limit = submissionLimit)
        elif subredditCategory == "top":
            category = subreddit.top(limit = submissionLimit)

        for submission in category:
            if not submission.stickied:
                print('Title: {}, Ups: {}, Downs: {}, Have we visited: {}\n'.format(submission.title,
                                                                                    submission.ups,
                                                                                    submission.downs,
                                                                                    submission.visited))
                submission.comments.replace_more(limit=0)

                for comment in submission.comments.list():
                    print(20 * '-')
                    print('Parent ID: ', comment.parent())
                    print('Comment ID: ', comment.id)
                    print(comment.body)

    #This will take in all the user data, along with the subreddit you're tracking them in
    #   and it will output all posts that user has posted in that specific subreddit
    def searchUserDataInSubreddit(self):
        print("Not implemented yet")

