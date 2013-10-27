from bs4 import BeautifulSoup
import urllib2

#Initialize variables
tempEvent = ''
eventTime = ''
eventTeam = ''
eventAction = ''
eventPlayer = ''
homeScore = 0
awayScore = 0
count = 0
#Serves as a watcher to determine when the end of the half is
nearEndOfHalf = False
eventHalf = 1

#NOTE to put soup into readable format: table.prettify())
#Step one: connect to the relevant game's play by play page
#Not sure what this is doing
opener = urllib2.build_opener()

#Must declare a user agent or some sites will take a dump on the GET request
headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',}
opener.addheaders = headers.items()
url = raw_input('URL to scrape:')
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

    #Trigger watcher for the end of the half (True when less than 1 minute on the game clock in first half)
    if (int(eventTime.split(":")[0]) == 0):
        nearEndOfHalf = True

    #Identify when the second half has started (Second half started when the game clock resets to something other than "0:##" and watcher had been enabled)
    if (int(eventTime.split(":")[0]) != 0) and (nearEndOfHalf == True):
        eventHalf += 1
        nearEndOfHalf = False

    #Determine which team the event is relevant to
    try:
        if i.next.nextSibling.next.string == None:
            eventTeam = homeTeam
            eventPlayer = i.find('a').string
            eventAction = i.find('span').string
            if 'made' in eventAction:
                if 'free throw' in eventAction:
                    homeScore += 1
                if ('2-point' in eventAction) or ('dunk' in eventAction) or ('layup' in eventAction):
                    homeScore += 2
                if '3-point' in eventAction:
                    homeScore += 3
        else:
            eventTeam = awayTeam
            eventPlayer = i.find('a').string
            eventAction = i.find('span').string
            if 'made' in eventAction:
                if 'free throw' in eventAction:
                    awayScore += 1
                if ('2-point' in eventAction) or ('dunk' in eventAction) or ('layup' in eventAction):
                    awayScore += 2
                if '3-point' in eventAction:
                    awayScore += 3

        print('Half = %s, Time = %s, Team = %s, Player = %s, Action = %s, Home Score = %s, Away Score = %s' % (eventHalf, eventTime[:-2], eventTeam, eventPlayer, eventAction, homeScore, awayScore))
        count += 1
        if count == 40:
            break
    except:
        print ('TIMEOUT')