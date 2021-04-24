import praw


class UserActivityTracker:
    def __init__(self, clientID, clientSecret, username, password, userAgent):
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.username = username
        self.password = password
        self.userAgent = userAgent

        self.reddit = praw.Reddit(client_id = self.clientID, client_secret = self.clientSecret, username = self.username, password = self.password, user_agent = self.userAgent)


        ####TODO - add in fields for the user data that we're trying to track
        #self.usernameToTrack

    # This will take in all user data, a timeframe - (for simplicity, a number of days, which will be the X-axis on outputted histogram)
    #   Will count how many times user has posted on each of those days going back from current day to N (Number of days passed in)
    #   Will output a bar graph or histogram with each bar representing how many times the user has posted on that day
    def trackUserActivityOverTimeframe(self, numberDays):
        print("Not implemented yet")