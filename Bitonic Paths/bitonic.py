# Dynamic programming...

from sys import setrecursionlimit
from random import random
from math import radians, cos, sin, sqrt, atan2
from DrawBitonic import createMap

#-----------------------------------------------------------------------------
# To successfully complete the assignment, you must implement all the
# functions/methods which are maked with this exception:

class TODO_Exception :
    pass

#-----------------------------------------------------------------------------
# Representing points on Earth

class GeoPoint :
    def __init__ (self,name,lat,lon) :
        """Creates points on Earth using latitude and longitude (in degrees).
        Use http://www.latlong.net to find the coordinates of your
        favorite locations.
        >>> indianapolis = GeoPoint('Indianapolis',39.768403,-86.158068)
        >>> bloomington = GeoPoint('Bloomington',39.165325,-86.526386)
        >>> chicago = GeoPoint('Chicago',41.878114,-87.629798)
        >>> louisville = GeoPoint('Louisville',38.252665,-85.758456)
        >>> cincinnati = GeoPoint('Cincinnati',39.103118,-84.512020)
        >>> stlouis = GeoPoint('St. Louis',38.627003,-90.199404)
        >>> columbus = GeoPoint('Columbus',39.961176,-82.998794)
        """
        raise TODO_Exception

    def distance_to(self, other):
        """
        Calculate the great circle distance between two points 
        on Earth. The points are specified using latitude and longitude
        in decimal degrees.
        >>> indianapolis = GeoPoint('Indianapolis',39.768403,-86.158068)
        >>> bloomington = GeoPoint('Bloomington',39.165325,-86.526386)
        >>> chicago = GeoPoint('Chicago',41.878114,-87.629798)
        >>> louisville = GeoPoint('Louisville',38.252665,-85.758456)
        >>> cincinnati = GeoPoint('Cincinnati',39.103118,-84.512020)
        >>> stlouis = GeoPoint('St. Louis',38.627003,-90.199404)
        >>> columbus = GeoPoint('Columbus',39.961176,-82.998794)
        >>> round(bloomington.distance_to(indianapolis))
        46.0
        >>> round(bloomington.distance_to(bloomington))
        0.0
        >>> round(bloomington.distance_to(chicago))
        196.0
        >>> round(bloomington.distance_to(louisville))
        75.0
        >>> round(bloomington.distance_to(cincinnati))
        108.0
        >>> round(bloomington.distance_to(stlouis))
        201.0
        >>> round(bloomington.distance_to(columbus))
        196.0
        """
        raise TODO_Exception

    def __repr__ (self) :
        return '{name}({x},{y})'.format(name=self.name,x=self.lat,y=self.lon)

#-----------------------------------------------------------------------------
# Points to experiment with...

indianapolis = GeoPoint('Indianapolis',39.768403,-86.158068)
bloomington = GeoPoint('Bloomington',39.165325,-86.526386)
chicago = GeoPoint('Chicago',41.878114,-87.629798)
louisville = GeoPoint('Louisville',38.252665,-85.758456)
cincinnati = GeoPoint('Cincinnati',39.103118,-84.512020)
stlouis = GeoPoint('St. Louis',38.627003,-90.199404)
columbus = GeoPoint('Columbus',39.961176,-82.998794)

cities = \
  [indianapolis,bloomington,chicago,louisville,cincinnati,stlouis,columbus]

def generate_points (p,n) :
    """Generate 'n' points near point 'p' (approximately +/- 5 degrees)
    """
    res = []
    for i in range(n) :
        dlat = (random() - 0.5) * 10
        dlon = (random() - 0.5) * 10
        res.append(GeoPoint('p'+str(i),p.lat+dlat,p.lon+dlon))
    return res

#-----------------------------------------------------------------------------
# A path is a sequence of points

class Path :
    def __init__ (self,start_point) :
        """
        Creates a path with a single point.
        >>> Path(GeoPoint('p0',10,12))
        [p0(10,12)]
        >>> Path(GeoPoint('p3',3,1))
        [p3(3,1)]
        """
        raise TODO_Exception
    
    def extend (self,point) :
        """
        Adds the given point to the current path.
        >>> pt = Path(GeoPoint('p0',10,12))
        >>> pt
        [p0(10,12)]
        >>> pt.extend(GeoPoint('p1',8,1))
        >>> pt
        [p0(10,12), p1(8,1)]
        >>> pt.extend(GeoPoint('p2',18,7))
        >>> pt
        [p0(10,12), p1(8,1), p2(18,7)]
        >>> pt.extend(GeoPoint('p3',3,1))
        >>> pt
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        """
        raise TODO_Exception

    def reverse (self) :
        """
        Reverses the current path.
        >>> pt = Path(GeoPoint('p0',10,12))
        >>> pt.extend(GeoPoint('p1',8,1))
        >>> pt.extend(GeoPoint('p2',18,7))
        >>> pt.extend(GeoPoint('p3',3,1))
        >>> pt
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        >>> pt.reverse()
        >>> pt
        [p3(3,1), p2(18,7), p1(8,1), p0(10,12)]
        """
        raise TODO_Exception

    def clone (self) :
        """
        Makes a copy of the sequence of the points and returns it.
        >>> pt = Path(GeoPoint('p0',10,12))
        >>> pt.extend(GeoPoint('p1',8,1))
        >>> pt.extend(GeoPoint('p2',18,7))
        >>> pt.extend(GeoPoint('p3',3,1))
        >>> pt
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        >>> pt2 = pt
        >>> pt2
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        >>> pt == pt2
        True
        >>> pt3 = pt.clone()
        >>> pt3
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        >>> pt == pt2
        True
        >>> pt == pt3
        False
        >>> pt2 == pt3
        False
        >>> pt.extend(GeoPoint('p4',4,9))
        >>> pt
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1), p4(4,9)]
        >>> pt2
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1), p4(4,9)]
        >>> pt3
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        >>> pt.reverse()
        >>> pt
        [p4(4,9), p3(3,1), p2(18,7), p1(8,1), p0(10,12)]
        >>> pt2
        [p4(4,9), p3(3,1), p2(18,7), p1(8,1), p0(10,12)]
        >>> pt3
        [p0(10,12), p1(8,1), p2(18,7), p3(3,1)]
        """
        raise TODO_Exception

    def __repr__ (self) :
        raise TODO_Exception

# Visualize paths on Google maps

def draw_cities_path (fileName) :
    """
    Takes the name of a file (.html) and writes to this file the necessary
    information to overlay the cities path on a Google map. The function
    createMap takes a point which is the 'center' of the map, a path to draw,
    and a filename.
    """
    cities_path = Path(indianapolis)
    cities_path.extend(bloomington)
    cities_path.extend(chicago)
    cities_path.extend(louisville)
    cities_path.extend(cincinnati)
    cities_path.extend(stlouis)
    cities_path.extend(columbus)
    createMap(indianapolis,cities_path,fileName)

def generate_path (p,n,fileName) :
    """Generates 'n' points near point 'p', connects them in a path, and
    writes the path to the given filename."""
    points = generate_points(p,n)
    path = Path(points[0])
    for i in range(1,n) :
        path.extend(points[i])
    createMap(p,path,fileName)

#-----------------------------------------------------------------------------
# Now solve shortest path with east-west-east restriction.

class Bitonic :
    def __init__ (self,points=None,center=None,size=None) :
        """The constructor should either provide a sequence of points
        or an initial point and a size 'n'. In the second case, 'n' random
        points in the neighborhood of the initial point are generated and
        used for the calculation."""
        raise TODO_Exception

    def tour (self) :
        raise TODO_Exception

def generate_bitonic_path_cities (fileName) :
    """For testing the bitonic path calculation on the 7 sample cities."""
    path = Bitonic(cities).tour()
    createMap(indianapolis,path,fileName)

def generate_bitonic_path (p,n,fileName) :
    """For testing the bitonic path calculation on 'n' random locations in
    the neighbordhood of 'p'."""
    path = Bitonic(center=p, size=n).tour()
    createMap(p,path,fileName)

#-----------------------------------------------------------------------------

if __name__ == "__main__" :
    setrecursionlimit(100000)

    import doctest
    doctest.testmod()

#-----------------------------------------------------------------------------
