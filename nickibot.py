
#Ambitious Version
import csv

catalog = csv.reader(open('timestamps.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start, stamp_end, spotify, youtube = song
    d[title] = stamp_start, stamp_end, spotify, youtube

request = raw_input('What song do you want to hear Nicki on? ')

for title in d:
    if request.lower() == title.lower():
        #print "Nicki's verse starts at {0} minute and {1} seconds".format(d[title][0][0],d[title][0][2:])
        print "Here's {0} on youtube: http://youtu.be/{1}?t={2}m{3}s".format(request, d[title][3][32:], d[title][0][0], d[title][0][2:])
'''

#This looks at a CSV with only two columns (song title and beginning time stamp) because it's less complicated than the full database

import csv

catalog = csv.reader(open('timestamps_2col.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start = song
    d[title] = stamp_start

inquiry = raw_input('What song do you want to hear Nicki on? ')
inquiry = inquiry.lower()

for title in d:
    if inquiry == title:
        print "Nicki's verse starts at {0}".format(d[title])
'''
