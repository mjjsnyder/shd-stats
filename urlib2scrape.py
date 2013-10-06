from bs4 import BeautifulSoup
import urllib2
tempEvent = ''
eventTime = ''
eventTeam = ''
eventAction = ''
eventPlayer = ''
#Initialize scores to ridiculous number so that leaving them unchanged will be immediately apparent in stat analysis
homeScore = '10000'
awayScore = '10000'
count = 0

#NOTE to put soup into readable format: table.prettify())
#Step one: connect to the relevant game's play by play page
#Not sure what this is doing
opener = urllib2.build_opener()

#Must declare a user agent or some sites will take a dump on the GET request
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
}
opener.addheaders = headers.items()
url = 'http://statsheet.com/mcb/games/2013/03/15/unlv-75-colorado-state-65/play_by_play'
getWebsite = opener.open(url)
pageContent = getWebsite.read()
soup = BeautifulSoup(pageContent)

#Should have the full source of the page at this point

#Grab the whole play-by-play table by identifying this tag on the page: <table border="0" style="font-size:.9em" cellpadding="2" cellspacing="0">
table = soup.find('table', border="0", style="font-size:.9em", cellpadding="2")

#Filter for the game events
allEvents = table.find_all("tr", onmouseover="hl(this)", onmouseout="uhl(this)", style="")

#Obtain team names
homeTeam = table.next.next.next.nextSibling.nextSibling.nextSibling.string
awayTeam = table.next.next.next.nextSibling.string

#General banner for console output
print('GATHERED FROM %s' % (url))
print('The home team is %s and the away team is %s.' % (homeTeam, awayTeam))

#Loop through each event in the play-by-play
for i in allEvents:
    #Grab the game clock for the individual event
    eventTime = i.next.string

    #scoring is done in a weird way. will have to add logic to the eventAction object to control score
    #homeScore = i.next.nextSibling.nextSibling.string
    #awayScore = i.next.nextSibling.nextSibling.nextSibling.nextSibling.string

    #Determine which team the event is relevant to
    if i.next.nextSibling.next.string == None:
        eventTeam = homeTeam
        eventPlayer = i.find('a').string
        eventAction = i.find('span').string
    else:
        eventTeam = awayTeam
        eventPlayer = i.find('a').string
        eventAction = i.find('span').string

    #for when I fix the score tracking
    #print('Time = %s, Team = %s, Player = %s, Action = %s, Home Score = %s, Away Score = %s' % (eventTime[:-2], eventTeam, eventPlayer, eventAction, homeScore, awayScore))
    print('Time = %s, Team = %s, Player = %s, Action = %s' % (eventTime[:-2], eventTeam, eventPlayer, eventAction))
    count += 1
    if count == 2:
        break
