from bs4 import BeautifulSoup
import urllib2

#NOTE to put soup into readable format: table.prettify())
#Step one: connect to the relevant game's play by play page
#Not sure what this is doing
opener = urllib2.build_opener()

#Must declare a user agent or some sites will take a dump on the GET request
headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',}
opener.addheaders = headers.items()
url = raw_input('URL to scrape:')
baseURL = '/'.join(url.split('/')[:3])
getWebsite = opener.open(url)
pageContent = getWebsite.read()
soup = BeautifulSoup(pageContent)

#Should have the full source of the page at this point

#Grab each event by identifying this tag on the page: <tr onmouseover="hl(this)" onmouseout="uhl(this)">
seasonTable = soup.find_all('tr', onmouseover='hl(this)', onmouseout='uhl(this)')

#Grab relevant data points for each event:
for i in seasonTable:
    try:

        #Grab event date by identifying this tage on the page: <span style="font-size:1.2em">
        eventInfo = i.find('span', style='font-size:1.2em').string
        eventMonth = eventInfo.split(' ')[1]
        eventDay = eventInfo.split(' ')[2].split('\n')[0]
        eventTime = eventInfo.split('\n')[1]

        eventOpponent = i.find('a', style='text-decoration:none').string

        #Find the parent <td> tag for each box score, then acquire the associated href path from the anchor tag for the box score
        eventBoxScorePath = i.find('td', nowrap='', style='font-weight:bold;font-size:.9em;border-bottom:1px solid #ddd').a["href"]
        #eventBoxScoreURL = baseURL eventBoxScore.find('a')

        print('Month = %s, Day = %s, Time = %s, Opponent = %s.' % (eventMonth, eventDay, eventTime, eventOpponent))
        print(str(baseURL) + str(eventBoxScorePath))

    except:
        print('SOMETHING HAS GONE TERRIBLY WRONG')