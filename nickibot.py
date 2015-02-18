#Tweepy Authentication

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Cn43n1RyUrETH7U0C5RbFPF2Y'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'HJAuwmoB2qQHyL3Epf2o3ODVZy1hh2yK5wLPeaxZijjKy01J3C'#keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '3039118167-O9BtuQkx8miSIX37zCBahcJSk638lvHCRsFq8cC'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'd5yBodiwTPgCybFLO3agFJB5OpdiKxxrhdiPI8Zj6JMgi'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(status="get ready world! nicki comin.")

# filename=open(argfile,'r')
# f=filename.readlines()
# filename.close()
 
# for line in f:
	# api = tweepy.API(auth)
	# api.update_status(status=line)
	# time.sleep(900)#Tweet every 15 minutes

'''	
#Import Python's CSV and random functions
import csv
import random

#Open the timestamps spreadsheet as a file called "catalog" and create a dictionary called "d"
catalog = csv.reader(open('timestamps.csv', 'r'))
d = {}

#In dictionary d, save each song title in "catalog" as a key and the timestamp data (verse start and verse end) and YouTube link as values associated with each key.
for song in catalog:
    title, stamp_start, stamp_end, spotify, youtube = song
    d[title] = stamp_start, stamp_end, spotify, youtube

#Ask the user what they want to hear.
#This will evenutally be request = [tweet from user]
request = raw_input('What song do you want to hear Nicki on? ')        

#The first part of this If statement will return a random song and corresponding link if the user types "random."
if request.lower() == "random":
    rand_song = random.choice(d.keys())
    print "Here's Nicki's verse on {0}: http://youtu.be/{1}?t={2}m{3}s".format(rand_song, d[rand_song][3][32:], d[rand_song][0][0], d[rand_song][0][2:])
else:
    for title in d: #Iterate through all the keys in dictionary "d"
        if request.lower() == title.lower(): #If the request matches a key, return a YouTube link timestamped for when Nicki's verse starts
            if d[title][0] == "0:00": #If her verse starts right at the beginning of the song, just share the bare YouTube link with no timestamp
                print "Here's Nicki's verse on {0}: {1}".format(title, d[title][3])
            else:
                print "Here's Nicki's verse on {0}: http://youtu.be/{1}?t={2}m{3}s".format(title, d[title][3][32:], d[title][0][0], d[title][0][2:])



#This uses a CSV with only two columns (song title and beginning time stamp). It only returns the start time of the verse, does not include a link to the veres on YouTube.

import csv

catalog = csv.reader(open('timestamps_2col.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start = song
    d[title] = stamp_start

request = raw_input('What song do you want to hear Nicki on? ')

for title in d:
    if request.lower() == title.lower():
        print "Nicki's verse starts at {0}".format(d[title])
'''
