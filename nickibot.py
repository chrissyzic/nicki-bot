#Tweepy Authentication

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import Tweepy (to authenticate with Twitter), Python's time and sys modules that Tweepy requires to run.
import tweepy, time, sys

#Import credentials to authenticate with Twitter - these are stored in another file because they are SECRET. If they were public, anyone could tweet from my account.
from nickibot_cred import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

#Authenticate with Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Import Python's CSV functions for file handling purposes and Python's random function for "Shuffle" requests
import csv
import random

#Open the timestamps spreadsheet as a file called "catalog" and create a dictionary called "d"
catalog = csv.reader(open('timestamps.csv', 'r'))
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

new_most_recent = int(most_recent)

print new_most_recent

for mention in mentions:
    if mention.id > most_recent:
        most_recent = mention.id

#Check my @ mentions
#mentions = api.mentions_timeline(count=1)

#Assign twitter handle and tweet contents to their own variables
for mention in mentions:
    request = mention.text[17:]
    requester = mention.user.screen_name

#The first part of this If statement will return a random song and corresponding link if the user types "random."
if request.lower() == "shuffle":
    rand_song = random.choice(d.keys())
    api.update_status(status=".@{0} SHUFFLE! Here's Nicki's verse on {1}: http://youtu.be/{2}?t={3}m{4}s".format(requester, rand_song, d[rand_song][3][32:], d[rand_song][0][0], d[rand_song][0][2:]))
else:
    for title in d: #Iterate through all the keys in dictionary "d"
        if request.lower() == title.lower(): #If the request matches a key, return a YouTube link timestamped for when Nicki's verse starts
            if d[title][0] == "0:00": #If her verse starts right at the beginning of the song, just share the bare YouTube link
                api.update_status(status=".@{0} Here's Nicki's verse on {1}: {2}".format(title, d[title][3]))
            else:
                api.update_status(status=".@{0} Here's Nicki's verse on {1}: http://youtu.be/{2}?t={3}m{4}s".format(requester, title, d[title][3][32:], d[title][0][0], d[title][0][2:]))

                
'''
#This uses a CSV with only two columns (song title and beginning time stamp). It only returns the start time of the verse, does not include a link to the veres on YouTube.

import csv

catalog = csv.reader(open('timestamps_2col.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start = song
    d[title] = stamp_start

#Ask the user what they want to hear.
#request = raw_input('What song do you want to hear Nicki on? ')

for title in d:
    if request.lower() == title.lower():
        print "Nicki's verse starts at {0}".format(d[title])
'''
