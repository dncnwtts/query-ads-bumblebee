from __future__ import division
from lxml import html
import requests


url='http://physics-astronomy.jhu.edu/people/graduate-students/'
import urllib2
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
con = urllib2.urlopen(req)
'''
from urllib.request import urlopen, Request
req = Request(url, headers={'User-Agent' : "Magic Browser"})
con = urlopen(req)
'''
tree = con.read()

# List of names, including "Last name, Firstname" occasionally with added
# nickname. 
fullnames = tree.split('<td class="column-1">')[1:]
names = [n.split(',')[0] + ', ' + n.split(',')[1][1] for n in fullnames]

beginning = 'https://ui.adsabs.harvard.edu/#search/'
# Ensures all listed publications are referreed
display = 'fq={!type%3Daqp v%3D%24fq_property}&fq_property=(property:refereed)&'
# But this ignores things that are just on arXiv.
display = ''
# Affiliation of first author is "Hopkins", Physics department or IQM
affil = 'q=((pos(aff:"Hopkins",1) AND (pos(aff:"Quantum",1) OR pos(aff:"Physics",1)) AND ('
# This is a little too restrictive though.
affil = 'q=((pos(aff:"Hopkins",1) AND ('
# Ignores publications before authors were graduate students
ending = ')) AND year:2007-2099)&sort=date desc'

len_query = 45
urls = [beginning + display + affil]*(len(fullnames)//len_query + 1)
for i, name in enumerate(names):
    j = i//len_query
    if i % len_query == 0:
        author = 'author:"^' + name + '"'
    else:
        author = ' OR author:"^' + name + '"'
    urls[j] += author
urls = [url + ending for url in urls]

for url in urls:
    print(url)
