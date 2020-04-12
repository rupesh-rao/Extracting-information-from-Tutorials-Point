from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.tutorialspoint.com/tutorialslibrary.htm"
furl = urlopen(url)
html = furl.read()
furl.close()

f = open('tutorials_point.csv','w')
headers = 'Tutorials, Sub-Topic, URL\n'
f.write(headers)

soup = BeautifulSoup(html,'html.parser')
containers = soup.findAll('div',{'class': 'featured-box'})
tutorials = 0
sub_topics = 0

for container in containers:
    headings = container.findAll('h4')
    ul = container.findAll('ul')
    no_of_headings = len(headings)
    tutorials += no_of_headings
    
    for i in range(no_of_headings):
        topics = ul[i].findAll('li')
        sub_topics += len(topics)
        
        for topic in topics:
            topic_name = topic.text
            url = 'https://www.tutorialspoint.com/' + topic.a['href']
            f.write(headings[i].text + ',' + topic_name + ',' + url + '\n')

print('Tutorials: ',tutorials)
print('Sub-Topics: ',sub_topics)

f.close()
