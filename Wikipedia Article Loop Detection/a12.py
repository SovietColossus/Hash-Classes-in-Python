#Authors: Gleb Alexeev
#Problem: Finding loops in wikipedia articles

import httplib2
from bs4 import BeautifulSoup
from random import *

visited = {} #Visited dict
toVisit = [] #the links to be visited, queue if you will
Looped = {} #Loops

def getlinks(webpage):
    #this function finds all of the links on the current webpage

    http = httplib2.Http()
    status, response = http.request(webpage)

    soup = BeautifulSoup(response)
    links = soup.find_all('a')

    global toVisit
    i = 0
    while (i<len(links)):
        if (links[i].get('href')) != None \
        and links[i].get('href').startswith('/wiki') \
        and not links[i].get('href').startswith('/wiki/Help:') \
        and not links[i].get('href').startswith('/wiki/Category:') \
        and not links[i].get('href').startswith('/wiki/Portal:') \
        and not links[i].get('href').startswith('/wiki/Special:') \
        and not links[i].get('href').startswith('/wiki/Main_Page') \
        and not links[i].get('href').startswith('/wiki/Wikipedia:') : #checks on uninteresting pages
            toVisit.append("http://en.wikipedia.org" + links[i].get('href')) #appends the page to the site to be visited
        i += 1

def getLoops(webpage, desired): #BFS based search
    global visited
    global toVisit
    global Looped
    visited[webpage] = "visited" #add initial to visited
    getlinks(webpage) #get its links
    i = 0 #counter variable for BFS
    loops = 0 #counter for loop amount to get to desired
    justUsed = webpage
    while (loops < desired) :
        temp = toVisit[i]
        if temp in visited : #check if it's been visited
            if temp not in Looped : #Check for duplicate loops
                if temp != justUsed : #remove self linkage
                    print "Loop found when ", temp, " was visited."
                    loops += 1 #increment loops
                    Looped[temp] = "hello" #add to looped
                    justUsed = temp
        else :
            visited[temp] = "goodbye"
            if loops < 5 : #Basically, I assume toVisit will be large enough to no longer have to getlinks for every page in temp after 5. Works for up to 100 for me
                getlinks(temp)
            print "Visited",temp
            justUsed = temp
        i += 1
    print "Loops found: ", loops
    print "Loops:"
    for x in Looped.keys() :
        print x
    #print "Loops: ",list(Looped.keys()) #Final Loop list
    flush() #call on flush to clear history

def flush() : #clears history for new search
    global visited
    global toVisit
    global Looped
    visited = {}
    toVisit = []
    Looped = {}

'''Generally, the program is very Fast after 5 loops where found. Try Polimorphism 10, and Try Dog 100! :D, you have to enter the full webpage though: http://en.wikipedia.org/wiki/Dog'''
#getLoops("http://en.wikipedia.org/wiki/Dog", 100)
#getLoops("http://en.wikipedia.org/wiki/Philosophy", 30)
#getLoops("http://en.wikipedia.org/wiki/Polymorphism", 20)