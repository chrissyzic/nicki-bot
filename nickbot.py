
#Ambitious Version
import csv

catalog = csv.reader(open('timestamps.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start, stamp_end, spotify, youtube = song
    d[title] = stamp_start, stamp_end, spotify, youtube

inquiry = raw_input('What song do you want to hear Nicki on? ')

for title in d:
    if inquiry == title:
        print d[title]
'''

#This looks at a CSV with only two columns (song title and beginning time stamp) because it's less complicated than the full database

import csv

catalog = csv.reader(open('timestamps_2col.csv', 'r'))
d = {}
for song in catalog:
    title, stamp_start = song
    d[title] = stamp_start

inquiry = raw_input('What song do you want to hear Nicki on? ')

for title in d:
    if inquiry == title:
        print d[title]
'''
