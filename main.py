from lxml import html
import requests

import urllib2
url='http://physics-astronomy.jhu.edu/people/graduate-students/'
# Follows http://docs.python-guide.org/en/latest/scenarios/scrape/ to scrape URL
# of authors, in this case JHU Physics and Astronomy graduate students
#page = requests.get(url)
#tree = html.fromstring(page.content)

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
con = urllib2.urlopen(req)
tree = con.read()

# List of names, including "Last name, Firstname" occasionally with added
# nickname. 
#fullnames = tree.xpath('//td[@class="column-1"]/text()')
fullnames = tree.split('<td class="column-1">')[1:-1]
for i in range(len(fullnames)):
    fullnames[i] = fullnames[i].split('<')[0]
    if fullnames[i].find('"') != -1:
        fullnames[i] = fullnames[i].split('"')[0]
    #elif fullnames[i].find("'") != -1:
    #    fullnames[i] = fullnames[i].split("'")[0]
print(fullnames)

# Makes author name "Last name, First initial"
lastnames = [student.split(',')[0] + ', ' + student.split(',')[1][1] for student
        in fullnames if student.split(',')[0] != '\n']
beginning = 'https://ui.adsabs.harvard.edu/#search/'
# Ensures all listed publications are referreed
display = 'fq={!type%3Daqp v%3D%24fq_property}&fq_property=(property%3Arefereed)'
# Affiliation of first author is "Hopkins", Physics department
affil = '&q=((pos(aff%3A"Hopkins",1) AND pos(aff%3A"Physics",1) AND ('
# Ignores publications before authors were graduate students
ending = ')) AND year%3A2005-2099)&sort=date desc'


urls = [beginning + display + affil]*4
#url2 = beginning + display + affil
#url3 = beginning + display + affil
#url4 = beginning + display + affil
for i, lastname in enumerate(lastnames):
    j = i/30
    if i % 30 == 0:
        author = 'author%3A"^' + lastname + '"'
    else:
        author = ' OR author%3A"^' + lastname + '"'
    urls[j] += author
urls = [url + ending for url in urls]

print(urls)
