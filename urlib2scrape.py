from bs4 import BeautifulSoup
import urllib2

#Step one: connect to the relevant game's play by play page

#not sure what this is doing
opener = urllib2.build_opener()

#must declare a user agent or else statsheet.com will take a dump on the GET request
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
}
opener.addheaders = headers.items()
url = 'YOU MIGHT WANT TO ADD SOMETHING HERE, KNUCKLEHEAD!!!'
getWebsite = opener.open(url)
pageContent = getWebsite.read()
soup = BeautifulSoup(pageContent)
#should have the full source of the page at this point

#identify this tag on the page: <table border="0" style="font-size:.9em" cellpadding="2" cellspacing="0">
table = soup.find('table', border="0", style="font-size:.9em", cellpadding="2")

#NOTE to put into readable format: table.prettify())

#first event in the table
#print(table.next.next.nextSibling.nextSibling.prettify())

#Number of events in the game no longer needed with curated allEvents Object
#identify this tag for events: <tr onmouseover="hl(this)" onmouseout="uhl(this)" style="">
#totalNumEvents = len(table.find_all("tr", onmouseover="hl(this)", onmouseout="uhl(this)", style=""))
allEvents = table.find_all("tr", onmouseover="hl(this)", onmouseout="uhl(this)", style="")


#obtain team names
homeTeam = table.next.next.next.nextSibling.nextSibling.nextSibling.string
awayTeam = table.next.next.next.nextSibling.string

#game score at first event in table
#firstEventAwayScore = table.next.next.nextSibling.nextSibling.next.nextSibling.nextSibling.string
#firstEventHomeScore = table.next.next.nextSibling.nextSibling.next.nextSibling.nextSibling.nextSibling.nextSibling.string

print('GATHERED FROM %s' % (url))
print('The home team is %s and the away team is %s.' % (homeTeam, awayTeam))
#print('There are %d events in this game.' % (totalEvents))
#print('The first event occured with %s remaining on the game clock.' % (firstEventTime[:-2]))
#print('Score: %s - %s | %s - %s' % (awayTeam, firstEventAwayScore, homeTeam, firstEventHomeScore))

tempEvent = ''
eventTime = ''
eventTeam = ''
eventAction = ''
eventPlayer = ''
homeScore = 10000
awayScore = 10000
count = 0
for i in allEvents:
    eventTime = i.next.string
    tempEvent = i.next.nextSibling

    if tempEvent.next.string == None:
        eventTeam = homeTeam
        eventPlayer = tempEvent.parent.find('a').string
        eventAction = tempEvent.parent.find('span').string
    else:
        eventTeam = awayTeam
        eventPlayer = tempEvent.find('a').string
        eventAction = tempEvent.find('span').string

    print('Time = %s, Team = %s, Player = %s, Action = %s, Home Score = %d, Away Score = %d' % (eventTime[:-2], eventTeam, eventPlayer, eventAction, homeScore, awayScore))
    count += 1
    if count == 3:
        break
