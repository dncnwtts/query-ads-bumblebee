from lxml import html
import requests

import urllib2
url='http://physics-astronomy.jhu.edu/people/graduate-students/'
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
con = urllib2.urlopen(req)
tree = con.read()

# List of names, including "Last name, Firstname" occasionally with added
# nickname. 
fullnames = tree.split('<td class="column-1">')[1:-1]
names = [n.split(',')[0] + ', ' + n.split(',')[1][1] for n in fullnames]

beginning = 'https://ui.adsabs.harvard.edu/#search/'
# Ensures all listed publications are referreed
display = 'fq={!type%3Daqp v%3D%24fq_property}&fq_property=(property%3Arefereed)'
# Affiliation of first author is "Hopkins", Physics department or IQM
affil = '&q=((pos(aff%3A"Hopkins",1) AND (pos(aff%3A"Quantum",1) OR pos(aff%3A"Physics",1)) AND ('
# Ignores publications before authors were graduate students
ending = ')) AND year%3A2007-2099)&sort=date desc'

len_query = 30
urls = [beginning + display + affil]*(len(fullnames)/len_query + 1)
for i, name in enumerate(names):
    j = i/len_query
    if i % 30 == 0:
        author = 'author%3A"^' + name + '"'
    else:
        author = ' OR author%3A"^' + name + '"'
    urls[j] += author
urls = [url + ending for url in urls]

print(urls)
