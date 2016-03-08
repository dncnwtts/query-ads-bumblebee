from lxml import html
import requests

# Follows http://docs.python-guide.org/en/latest/scenarios/scrape/ to scrape URL
# of authors, in this case JHU Physics and Astronomy graduate students
page = requests.get('http://physics-astronomy.jhu.edu/people/graduate-students/')
tree = html.fromstring(page.content)

# List of names, including "Last name, Firstname" occasionally with added
# nickname. 
fullnames = tree.xpath('//td[@class="column-1"]/text()')

# Makes author name "Last name, First initial"
lastnames = [student.split(',')[0] + ', ' + student.split(',')[1][1] for student
        in fullnames if student.split(',')[0] != '\n']
beginning = 'https://ui.adsabs.harvard.edu/#search/'
# Ensures all listed publications are referreed
display = 'fq={!type%3Daqp v%3D%24fq_property}&fq_property=(property%3Arefereed)'
# Affiliation of first author is "Hopkins"
affil = '&q=((pos(aff%3A"Hopkins",1) AND aff%3A"Astronomy" AND ('
# Ignores publications before authors were graduate students
ending = ')) AND year%3A2005-2099)&sort=date desc'

url = beginning + display + affil
for i, lastname in enumerate(lastnames):
    if i == 0:
        author = 'author%3A"^' + lastname + '"'
    else:
        author = ' OR author%3A"^' + lastname + '"'
    url += author
url += ending

print(url)
