#Tweepy Authentication

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys

from nickibot_cred import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Ambitious Version

#Import Python's CSV functions
import csv
import random

#Open the timestamps spreadsheet as a file called "catalog" and create a dictionary called "d"
catalog = csv.reader(open('timestamps.csv', 'r'))
d = {}

#In dictionary d, save each song title as a key and the timestamp data (verse start and verse end) and YouTube link as values associated with each key.
for song in catalog:
    title, stamp_start, stamp_end, spotify, youtube = song
    d[title] = stamp_start, stamp_end, spotify, youtube

#Check my @ mentions
mentions = api.mentions_timeline(count=1)

#Assign twitter handle and tweet contents to their own variables
for mention in mentions:
    request = mention.text[17:]
    requester = mention.user.screen_name

#The first part of this If statement will return a random song and corresponding link if the user types "random."
if request.lower() == "shuffle":
    rand_song = random.choice(d.keys())
    api.update_status(status="@{0} SHUFFLE! Here's Nicki's verse on {1}: http://youtu.be/{2}?t={3}m{4}s".format(requester, rand_song, d[rand_song][3][32:], d[rand_song][0][0], d[rand_song][0][2:]))
else:
    for title in d: #Iterate through all the keys in dictionary "d"
        if request.lower() == title.lower(): #If the request matches a key, return a YouTube link timestamped for when Nicki's verse starts
            if d[title][0] == "0:00": #If her verse starts right at the beginning of the song, just share the bare YouTube link
                api.update_status(status="@{0} Here's Nicki's verse on {1}: {2}".format(title, d[title][3]))
            else:
                api.update_status(status="@{0} Here's Nicki's verse on {1}: http://youtu.be/{2}?t={3}m{4}s".format(requester, title, d[title][3][32:], d[title][0][0], d[title][0][2:]))
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
