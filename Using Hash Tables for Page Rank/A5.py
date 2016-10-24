import httplib2
from bs4 import BeautifulSoup
from random import *

graph = {}
graphsize = 0

def creategraph(n, www):
    page = www
    fillgraph(page, n)
    return graphsize

def fillgraph(webpage, n):
    global graph
    global graphsize
    if (graphsize<n):
        linked = getlinks(webpage)
        graph[webpage] = linked
        graphsize += 1
        i = 0
        while (i<len(linked)):
            try :
                if (graph.has_key(linked[i]) == False):
                    fillgraph(linked[i], n)
                i += 1
            except :
                i += 1
    
def getlinks(webpage):
    http = httplib2.Http()
    status, response = http.request(webpage)
    soup = BeautifulSoup(response)
    links = soup.find_all('a')

    values = []
    i = 0
    while (i<len(links)):
        if (links[i].get('href') != None):
            if (links[i].get('href').startswith('http')):
                values.append(links[i].get('href'))
        i += 1

    return values


def collect_statistics (www,prob,k) :
	result = {}
	current = choice(www.keys())
	while k > 0 :
		if current in result:
			result[current] += 1
		else:
			result[current] = 1
		if random() * 100 < prob :
			current = choice(www.keys())
		else :
			neighbors = www.get(current)
			if neighbors == [] or neighbors == None:
				current = choice(www.keys())
			else:
				current = choice(neighbors)
		k -=1
	return result

def top (www) :
	d = collect_statistics(www,15,1000000).items()
	d.sort(key = lambda x : x[1], reverse = True)
	return d[:3]



creategraph(1000, 'http://www.reddit.com')
print graphsize
#print collect_statistics(graph, 15, 100)
print top(graph)