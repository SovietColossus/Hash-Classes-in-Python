import time
import random
import sys
import unittest

from a11 import *   # solution

# Set up for dense graphs

def make_graphs (max_weight=100,num_nodes=60) :
    nodes = map(lambda x : Item('node-'+str(x),x),range(num_nodes))
    neighbors = { n: [] for n in nodes }
    weights = {}
    for s in nodes :
        for t in nodes :
            if s == t :
                continue
            else : 
                neighbors[s].append(t)
                weights[(s,t)] = random.randrange(max_weight)
    s = random.choice(nodes)
    g2 = Graph(nodes,neighbors,weights,2)
    gd = Graph(nodes,neighbors,weights,num_nodes)
    return (s,g2,gd)

# Testing...

class Test (unittest.TestCase) :

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    #-------------------------------------------------------------------------

    def test_Positions (self) :
        h = D_Heap(5)
        for i in range(16) :
            h.insert(Item('X',1))
        # children of root
        self.assertEquals(h.getChildIndex(1,1),2)
        self.assertEquals(h.getChildIndex(1,2),3)
        self.assertEquals(h.getChildIndex(1,3),4)
        self.assertEquals(h.getChildIndex(1,4),5)
        self.assertEquals(h.getChildIndex(1,5),6)
        # children of leftmost child of root
        self.assertEquals(h.getChildIndex(2,1),7)
        self.assertEquals(h.getChildIndex(2,2),8)
        self.assertEquals(h.getChildIndex(2,3),9)
        self.assertEquals(h.getChildIndex(2,4),10)
        self.assertEquals(h.getChildIndex(2,5),11)
        # children of second leftmost child of root
        self.assertEquals(h.getChildIndex(3,1),12)
        self.assertEquals(h.getChildIndex(3,2),13)
        self.assertEquals(h.getChildIndex(3,3),14)
        self.assertEquals(h.getChildIndex(3,4),15)
        self.assertEquals(h.getChildIndex(3,5),16)
        # getting second parent 
        self.assertEquals(h.getParentIndex(12),3)
        self.assertEquals(h.getParentIndex(13),3)
        self.assertEquals(h.getParentIndex(14),3)
        self.assertEquals(h.getParentIndex(15),3)
        self.assertEquals(h.getParentIndex(16),3)
        # getting first parent
        self.assertEquals(h.getParentIndex(7),2)
        self.assertEquals(h.getParentIndex(8),2)
        self.assertEquals(h.getParentIndex(9),2)
        self.assertEquals(h.getParentIndex(10),2)
        self.assertEquals(h.getParentIndex(11),2)
        # getting root parent
        self.assertEquals(h.getParentIndex(2),1)
        self.assertEquals(h.getParentIndex(3),1)
        self.assertEquals(h.getParentIndex(4),1)
        self.assertEquals(h.getParentIndex(5),1)
        self.assertEquals(h.getParentIndex(6),1)
        # changing d = 7
        h = D_Heap(7)
        for i in range(22) :
            h.insert(Item('X',1))
        # children of root
        self.assertEquals(h.getChildIndex(1,1),2)
        self.assertEquals(h.getChildIndex(1,2),3)
        self.assertEquals(h.getChildIndex(1,3),4)
        self.assertEquals(h.getChildIndex(1,4),5)
        self.assertEquals(h.getChildIndex(1,5),6)
        self.assertEquals(h.getChildIndex(1,6),7)
        self.assertEquals(h.getChildIndex(1,7),8)
        # children of leftmost child of root
        self.assertEquals(h.getChildIndex(2,1),9)
        self.assertEquals(h.getChildIndex(2,2),10)
        self.assertEquals(h.getChildIndex(2,3),11)
        self.assertEquals(h.getChildIndex(2,4),12)
        self.assertEquals(h.getChildIndex(2,5),13)
        self.assertEquals(h.getChildIndex(2,6),14)
        self.assertEquals(h.getChildIndex(2,7),15)
        # children of second leftmost child of root
        self.assertEquals(h.getChildIndex(3,1),16)
        self.assertEquals(h.getChildIndex(3,2),17)
        self.assertEquals(h.getChildIndex(3,3),18)
        self.assertEquals(h.getChildIndex(3,4),19)
        self.assertEquals(h.getChildIndex(3,5),20)
        self.assertEquals(h.getChildIndex(3,6),21)
        self.assertEquals(h.getChildIndex(3,7),22)
        # getting second parent 
        self.assertEquals(h.getParentIndex(16),3)
        self.assertEquals(h.getParentIndex(17),3)
        self.assertEquals(h.getParentIndex(18),3)
        self.assertEquals(h.getParentIndex(19),3)
        self.assertEquals(h.getParentIndex(20),3)
        self.assertEquals(h.getParentIndex(21),3)
        self.assertEquals(h.getParentIndex(22),3)
        # getting first parent
        self.assertEquals(h.getParentIndex(9),2)
        self.assertEquals(h.getParentIndex(10),2)
        self.assertEquals(h.getParentIndex(11),2)
        self.assertEquals(h.getParentIndex(12),2)
        self.assertEquals(h.getParentIndex(13),2)
        self.assertEquals(h.getParentIndex(14),2)
        self.assertEquals(h.getParentIndex(15),2)
        # getting root parent
        self.assertEquals(h.getParentIndex(2),1)
        self.assertEquals(h.getParentIndex(3),1)
        self.assertEquals(h.getParentIndex(4),1)
        self.assertEquals(h.getParentIndex(5),1)
        self.assertEquals(h.getParentIndex(6),1)
        self.assertEquals(h.getParentIndex(7),1)
        self.assertEquals(h.getParentIndex(8),1)

    def test_Insert (self) :
        h = D_Heap(5)
        h.insert(Item('X',10))
        self.assertListEqual(h.getVals(),[10])
        h.insert(Item('X',15))
        self.assertListEqual(h.getVals(),[10,15])
        h.insert(Item('X',12))
        self.assertListEqual(h.getVals(),[10,15,12])
        h.insert(Item('X',22))
        self.assertListEqual(h.getVals(),[10,15,12,22])
        h.insert(Item('X',3))
        self.assertListEqual(h.getVals(),[3,15,12,22,10])
        h.insert(Item('X',6))
        self.assertListEqual(h.getVals(),[3,15,12,22,10,6])
        h.insert(Item('X',1))
        self.assertListEqual(h.getVals(),[1,3,12,22,10,6,15])
        h.insert(Item('X',4))
        self.assertListEqual(h.getVals(),[1,3,12,22,10,6,15,4])
        h.insert(Item('X',5))
        self.assertListEqual(h.getVals(),[1,3,12,22,10,6,15,4,5])
        h.insert(Item('X',7))
        self.assertListEqual(h.getVals(),[1,3,12,22,10,6,15,4,5,7])
        h.insert(Item('X',8))
        self.assertListEqual(h.getVals(),[1,3,12,22,10,6,15,4,5,7,8])
        h.insert(Item('X',18))
        self.assertListEqual(h.getVals(),[1,3,12,22,10,6,15,4,5,7,8,18])
        h.insert(Item('X',2))
        self.assertListEqual(h.getVals(),[1,3,2,22,10,6,15,4,5,7,8,18,12])

    def test_Min (self) :
        h = D_Heap(5)
        h.insert(Item('X',10))
        h.insert(Item('X',15))
        h.insert(Item('X',12))
        h.insert(Item('X',22))
        h.insert(Item('X',3))
        h.insert(Item('X',6))
        h.insert(Item('X',1))
        h.insert(Item('X',4))
        h.insert(Item('X',5))
        h.insert(Item('X',7))
        h.insert(Item('X',8))
        h.insert(Item('X',18))
        h.insert(Item('X',2))
        self.assertListEqual(h.getVals(),[1,3,2,22,10,6,15,4,5,7,8,18,12])
        self.assertEquals(h.extractMin().value,1)
        self.assertListEqual(h.getVals(),[2,3,12,22,10,6,15,4,5,7,8,18])

    def test_Min_Big (self) :
        def f (d) :
            size = 1000
            h = D_Heap(d)
            xs = range(size)
            random.shuffle(xs)
            for i in range(size) :
                h.insert(Item('X',i))
            ms = []
            while not h.isEmpty() :
                ms.append(h.extractMin().value)
            self.assertListEqual(ms,range(size))
        for i in range(1,20) :
            f(i)

    # a9 dijkstra tests should still pass

    def test_Item (self) :
        b = Item('Bloomington')
        self.assertEqual(b.name,'Bloomington')
        self.assertIsNone(b.position)
        self.assertIsNone(b.value)
        self.assertIsNone(b.previous)

    def test_Heap (self) :
        b = Item('Bloomington')
        b.value = sys.maxint
        b.position = 1

        i = Item('Indianapolis')
        i.value = sys.maxint
        i.position = 2

        h = D_Heap(2,fromList=[b,i])

        self.assertEqual(h.size,2)
        self.assertIsNone(h.elems[0])
        self.assertEqual(h.elems[1],b)
        self.assertEqual(h.elems[2],i)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)

        h.swap(1,2)
        
        self.assertEqual(h.elems[1],i)
        self.assertEqual(h.elems[2],b)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)

        h.updateKey(2,11)

        self.assertEqual(h.elems[1],b)
        self.assertEqual(h.elems[2],i)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)
        self.assertEqual(h.elems[1].value,11)
        self.assertEqual(h.elems[2].value,sys.maxint)

        c = Item('Chicago')
        c.value = 3
        h.insert(c)

        self.assertEqual(h.elems[1],c)
        self.assertEqual(h.elems[2],i)
        self.assertEqual(h.elems[3],b)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)
        self.assertEqual(h.elems[3].position,3)
        self.assertEqual(h.elems[1].value,3)
        self.assertEqual(h.elems[2].value,sys.maxint)
        self.assertEqual(h.elems[3].value,11)

        h.updateKey(2,2)
        
        self.assertEqual(h.elems[1],i)
        self.assertEqual(h.elems[2],c)
        self.assertEqual(h.elems[3],b)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)
        self.assertEqual(h.elems[3].position,3)
        self.assertEqual(h.elems[1].value,2)
        self.assertEqual(h.elems[2].value,3)
        self.assertEqual(h.elems[3].value,11)

        m = h.extractMin()

        self.assertEqual(m,i)
        self.assertEquals(h.size,2)
        self.assertEqual(h.elems[1],c)
        self.assertEqual(h.elems[2],b)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)
        self.assertEqual(h.elems[1].value,3)
        self.assertEqual(h.elems[2].value,11)
        
    def test_Path (self) :
        b = Item('Bloomington')
        i = Item('Indianapolis')
        c = Item('Chicago')
        p = Path(b)

        self.assertEqual(p.nodes,[b])
        self.assertEqual(p.len,0)

        p.append(i,259)
        
        self.assertEqual(p.nodes,[b,i])
        self.assertEqual(p.len,259)

        p.append(c,32)
        
        self.assertEqual(p.nodes,[b,i,c])
        self.assertEqual(p.len,291)

    def test_Graph_1 (self) :
        s = Item('s')
        t = Item('t')
        x = Item('x')
        y = Item('y')
        z = Item('z')

        nodes0     = [s,t,x,y,z]
        neighbors0 = { s:[t,y], t:[x,y], x:[z], y:[t,x,z], z:[s,x] }
        weights0   = { (s,t):10, (s,y):5, (t,y):2, (t,x):1, (x,z):4,
                       (y,t):3, (y,x):9, (y,z):2, (z,s):7, (z,x):6 }
        g0         = Graph(nodes0,neighbors0,weights0)

        self.assertEqual(g0.nodes,nodes0)
        self.assertEqual(g0.neighbors,neighbors0)
        self.assertEqual(g0.weights,weights0)

        g0.setSource(s)

        self.assertEqual(s.value,0)
        self.assertEqual(t.value,sys.maxint)
        self.assertEqual(x.value,sys.maxint)
        self.assertEqual(y.value,sys.maxint)
        self.assertEqual(z.value,sys.maxint)
        self.assertEqual(s.position,1)
        self.assertEqual(t.position,2)
        self.assertEqual(x.position,3)
        self.assertEqual(y.position,4)
        self.assertEqual(z.position,5)

        h = g0.q

        self.assertEquals(h.size,5)
        self.assertEqual(h.elems[1],s)
        self.assertEqual(h.elems[2],t)
        self.assertEqual(h.elems[3],x)
        self.assertEqual(h.elems[4],y)
        self.assertEqual(h.elems[5],z)
        self.assertEqual(h.elems[1].position,1)
        self.assertEqual(h.elems[2].position,2)
        self.assertEqual(h.elems[3].position,3)
        self.assertEqual(h.elems[4].position,4)
        self.assertEqual(h.elems[5].position,5)
        self.assertEqual(h.elems[1].value,0)
        self.assertEqual(h.elems[2].value,sys.maxint)
        self.assertEqual(h.elems[3].value,sys.maxint)
        self.assertEqual(h.elems[4].value,sys.maxint)
        self.assertEqual(h.elems[5].value,sys.maxint)
        
        u1 = h.extractMin()
        n11 = g0.neighbors[u1][0]
        n12 = g0.neighbors[u1][1]

        self.assertEqual(u1,s)
        self.assertEqual(n11,t)
        self.assertEqual(n12,y)
        
        g0.relax(u1,n11)

        self.assertEqual(n11.previous,u1)
        self.assertEqual(n11.value,10)
        self.assertEqual(n11.position,1)
        self.assertEqual(h.elems[1],n11)

        g0.relax(u1,n12)

        self.assertEqual(n12.previous,u1)
        self.assertEqual(n12.value,5)
        self.assertEqual(n12.position,1)
        self.assertEqual(n11.position,2)
        self.assertEqual(h.elems[1],n12)
        self.assertEqual(h.elems[2],n11)

        u2 = h.extractMin()

        self.assertEqual(u2,y)

    def test_Graph_2 (self) :
        s = Item('s')
        t = Item('t')
        x = Item('x')
        y = Item('y')
        z = Item('z')

        nodes0     = [s,t,x,y,z]
        neighbors0 = { s:[t,y], t:[x,y], x:[z], y:[t,x,z], z:[s,x] }
        weights0   = { (s,t):10, (s,y):5, (t,y):2, (t,x):1, (x,z):4,
                       (y,t):3, (y,x):9, (y,z):2, (z,s):7, (z,x):6 }
        g0         = Graph(nodes0,neighbors0,weights0)

        g0.compute_shortest_paths(s)

        ss = g0.build_shortest_path(s)
        ts = g0.build_shortest_path(t)
        xs = g0.build_shortest_path(x)
        ys = g0.build_shortest_path(y) 
        zs = g0.build_shortest_path(z)

        self.assertEqual(ss.nodes,[s])
        self.assertEqual(ss.len,0)

        self.assertEqual(ts.nodes,[t,y,s])
        self.assertEqual(ts.len,8)

        self.assertEqual(xs.nodes,[x,t,y,s])
        self.assertEqual(xs.len,9)

        self.assertEqual(ys.nodes,[y,s])
        self.assertEqual(ys.len,5)

        self.assertEqual(zs.nodes,[z,y,s])
        self.assertEqual(zs.len,7)

    # test dense graphs that have V ** 2 edges

    def test_Graph_Dense_2vsd (self) :
        (s,g2,gd) = make_graphs()
        g2.compute_shortest_paths(s)
        gd.compute_shortest_paths(s)
        for i in range(1000) :
            t = random.choice(g2.getNodes())
            p2 = g2.build_shortest_path(t)
            pd = gd.build_shortest_path(t)
            self.assertListEqual(p2.getList(),pd.getList())

    def test_Graph_Dense_2time (self) :
        (s,g2,gd) = make_graphs()
        g2.compute_shortest_paths(s)

    def test_Graph_Dense_dtime (self) :
        (s,g2,gd) = make_graphs()
        gd.compute_shortest_paths(s)
        
if __name__ == '__main__' :
    sys.setrecursionlimit(10**6)
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=0).run(suite)
