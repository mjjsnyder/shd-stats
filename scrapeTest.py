from bs4 import BeautifulSoup
import requests
import urllib2

#static declaration of the URL being scraped (do NOT include http:// here)
link = 'http://statsheet.com/mcb/games/2012/11/12/northern-arizona-54-unlv-92/play_by_play'
#link = 'http://espn.com'

#request website url (should return '<Response [200]>')
r = requests.request('GET', link, stream=True)
#r = urllib2.urlopen(link)
print(r)

#simplified with soup declaration
#obtain source of website in decoded unicode text
#data = r.text

#creates a BeautifulSoup object, which represents the source as a nested data structure
#note: simplified but adding .text
soup = BeautifulSoup(r.text)

#find all instances of <h1> tag in the data structure, and print them to the console
for table in soup.find_all('title'):
    print(table)

#print the content of the <title> tag in the data structure
#print(soup.title.string)