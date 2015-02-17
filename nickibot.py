
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
            if d[title][0] == "0:00": #If her verse starts right at the beginning of the song, just share the bare YouTube link
                print "Here's Nicki's verse on {0}: {1}".format(title, d[title][3])
            else:
                print "Here's Nicki's verse on {0}: http://youtu.be/{1}?t={2}m{3}s".format(title, d[title][3][32:], d[title][0][0], d[title][0][2:])
'''

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
