
#Ambitious Version

#Import Python's CSV functions
import csv

#Open the timestamps spreadsheet as a dictionary called "catalog".
#For each entry, the song title is saved as the key, and the timestamp data (verse start and verse end) and YouTube link are the values associated with each key.
catalog = csv.reader(open('timestamps.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start, stamp_end, spotify, youtube = song
    d[title] = stamp_start, stamp_end, spotify, youtube

#Ask the user what they want to hear.
#This will evenutally be request = [tweet from user]
request = raw_input('What song do you want to hear Nicki on? ')

#This will give the user a link to a random song Nicki is featured on.
#if request.lower == "random":

#Match the user's request with a key in the catalog dictionary.
#Return YouTube link that jumps to Nicki's verse.
for title in d:
    if request.lower() == title.lower():
        if d[title][0] == "0:00":
            print "Here's Nicki's verse on {0}: {1}".format(title, d[title][3])
        else:
            print "Here's Nicki's verse on {0}: http://youtu.be/{1}?t={2}m{3}s".format(request, d[title][3][32:], d[title][0][0], d[title][0][2:])
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
