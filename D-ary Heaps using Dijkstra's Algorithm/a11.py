#Filename: dijkstra.py
#Part of: Assignment 10

from sys import maxint
from math import *

class NoParentE     : pass
class NoChildE      : pass
class NoLeftChildE  : pass
class NoRightChildE : pass

class D_Heap :
    def __init__ (self, d=2, fromList=None) :
        self.elems = [None]
        self.size = 0
        self.d = d
        if fromList :
            self.size = len(fromList)
            self.elems.extend(fromList[:])
            for i in range(self.size/2,0,-1) :
                self.moveDown(i)

    def getVals(self) :
        return [i.value for i in self.elems[1:]]

    def isEmpty (self) : return self.size == 0

    def getSize (self) : return self.size
    
    def findMin (self) : return self.elems[1]

    def getParentIndex (self,i) :
        if i == 1 :
            raise NoParentE
        else :
            return ((i - 2)/self.d)+1

    def getChildIndex (self,i,j) :
        answer = (((i-1)*self.d) + j) + 1
        if j >= 1 and answer <= self.size :
            return answer
        else :
            raise NoChildE

    def swap (self,i,j) :
        temp = self.elems[i]
        temppos = self.elems[i].position
        self.elems[i] = self.elems[j]
        self.elems[i].position = i
        self.elems[j] = temp
        self.elems[j].position = j

    def moveUp (self,i) :
        try :
            p = self.getParentIndex(i)
            if self.elems[i].value < self.elems[p].value :
                self.swap(i,p)
                self.moveUp(p)
        except NoParentE :
            pass

    def insert (self,k) :
        self.elems.append(k)
        self.elems[-1].position = k
        self.size += 1
        self.moveUp(self.size)

    def minChildIndex (self,i) : #Get NoChildE
        node = 2
        answer = self.getChildIndex(i,1)
        try :
            while node <= self.d :
                other = self.getChildIndex(i,node)
                if self.elems[other].value < self.elems[answer].value :
                    answer = other
                node += 1
            return answer
        except NoChildE :
            return answer

    def moveDown (self,i) :
        try :
            c = self.minChildIndex(i)
            if self.elems[i].value > self.elems[c].value :
                self.swap(i,c)
                self.moveDown(c)
        except NoChildE :
            pass

    def delMin (self) :
        self.elems[1] = self.elems[self.size]
        self.elems[1].position = 1
        self.size -= 1
        self.elems.pop()
        self.moveDown(1)

    def updateKey(self,i,v) :
        self.elems[i].value = v
        self.moveUp(i)

    def extractMin(self) :
        temp = self.elems[1]
        self.delMin()
        return temp
    
    def __repr__ (self) :
        return repr(self.elems[1:])

class Item :
    def __init__(self, name, value = None):
        self.name = name
        self.position = None
        self.value = value
        self.previous = None

class Path :
    def __init__(self, start):
        self.nodes = [start]
        self.len = 0

    def getList(self) :
        return self.nodes

    def append (self, newNode, distance) :
        self.nodes.append(newNode)
        self.len = self.len + distance
        
class Graph :
    def __init__(self, nodes, neighbors, weights, d=2):
        self.nodes = nodes
        self.neighbors = neighbors
        self.weights = weights
        self.d = d

    def getNodes(self) :
        return self.nodes

    def setSource (self, s) :
        for x in self.nodes :
            x.value = maxint
            x.position = self.nodes.index(x) + 1
        s.value = 0
        self.q = D_Heap(self.d, self.nodes)

    def relax (self, u ,v) :
        if v.value > u.value + self.weights[u,v] :
            self.q.updateKey(v.position, u.value + self.weights[u,v])
            v.previous = u

    def compute_shortest_paths (self, s) :
        self.setSource(s)
        while self.q.isEmpty() == False :
            mymin = self.q.extractMin()
            for neigh in self.neighbors[mymin] :
                self.relax(mymin,neigh)

    def build_shortest_path (self, u) :
        p = Path(u)
        prev = u.previous
        while prev != None :
            p.append(prev, self.weights[prev,u])
            u = prev
            prev = prev.previous
        return p