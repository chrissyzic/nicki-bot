print "It's a new day and this is Line 1: Off to a good start."
import os, site, sys

# Tell wsgi to add the Python site-packages to its path. 
site.addsitedir('/home/chrissyzic/webapps/findnickisverse/findnickisverse/nickibot-new/lib/python2.7/site-packages')

activate_this = os.path.expanduser("/home/chrissyzic/webapps/findnickisverse/findnickisverse/nickibot-new/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
print "This is Line 11: exec file worked."
project = '/home/chrissyzic/webapps/findnickisverse/findnickisverse'
print "This is Line 13: new project path worked"
workspace = os.path.dirname(project)
print "This is Line 15: workspace defined OK with new project path"
sys.path.append(workspace)
print "This is Line 17: sys.path.append worked"

#Tweepy Authentication
#Import Tweepy (to authenticate with Twitter), Python's time and sys modules that Tweepy requires to run.
print "Line 21: everything pre-tweepy worked"
import tweepy
print "This is Line 23: import tweepy worked"

#Import credentials to authenticate with Twitter - these are stored in another file because they are SECRET. If they were public, anyone could tweet from my account.
from nickibot_cred import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
print "This is Line 27: successfully imported keys and secrets"

#Authenticate with Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
print "This is Line 31: auth variable created successfully."
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#Import Python's CSV functions for file handling purposes and Python's random function for "Shuffle" requests
import csv
import random

#Open the timestamps spreadsheet as a file called "catalog" and create a dictionary called "d"
catalog = csv.reader(open('/home/chrissyzic/webapps/findnickisverse/findnickisverse/nicki-bot/timestamps.csv', 'r'))
d = {}

#In dictionary d, save each song title as a key and the timestamp data (verse start and verse end) and YouTube link as values associated with each key.
for song in catalog:
    title, stamp_start, stamp_end, spotify, youtube = song
    d[title] = stamp_start, stamp_end, spotify, youtube

#Create an empty list to store status IDs
statuses = []

#Loop through all tweets in my timeline, store the status IDs as a list
for status in api.user_timeline():
    statuses.append(status.id)

#Create a variable to hold most recent status ID
most_recent = statuses[0]

#Check for @ mentions since most recent status ID
if most_recent:
    mentions = api.mentions_timeline(since_id=most_recent)
else:
    mentions = ()
    print "No mentions, early end."

#Loop through list of mentions since last tweet and assign the user's twitter handle and tweet content to their own variables
for mention in mentions:
    request = mention.text[17:]
    requester = mention.user.screen_name

    #Check if the content of each tweet matches a song in the catalog.
    #The first part of this If statement will return a random song and corresponding link if the user types "shuffle"
    if request.lower() == "shuffle":
        rand_song = random.choice(d.keys())
        api.update_status(status=".@{0} SHUFFLE! Here's Nicki's verse on {1}: http://youtu.be/{2}?t={3}m{4}s".format(requester, rand_song, d[rand_song][3][32:], d[rand_song][0][0], d[rand_song][0][2:]))
    else:
        for title in d: #Iterate through all the keys (song titles) in dictionary "d"
            if request.lower() == title.lower(): #If the request matches a key, return a YouTube link timestamped for when Nicki's verse starts
                if d[title][0] == "0:00": #If her verse starts right at the beginning of the song, just share the bare YouTube link
                    api.update_status(status=".@{0} Here's Nicki's verse on {1}: {2}".format(requester, title, d[title][3]))
                else:
                    api.update_status(status=".@{0} Here's Nicki's verse on {1}: http://youtu.be/{2}?t={3}m{4}s".format(requester, title, d[title][3][32:], d[title][0][0], d[title][0][2:]))

