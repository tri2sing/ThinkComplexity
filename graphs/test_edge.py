'''
Created on Apr 3, 2016

@author: Sameer Adhikari
'''

from graphs.edge import Edge
from graphs.vertex import Vertex

def test_equal():
    u1 = Vertex('u')
    v1 = Vertex('v')
    e1 = Edge(u1, v1)
    u2 = Vertex('u')
    v2 = Vertex('v')
    e2 = Edge(u2, v2)
    assert(e1 == e2)

def test_hash():
    u1 = Vertex('u')
    v1 = Vertex('v')
    e1 = Edge(u1, v1)
    u2 = Vertex('u')
    v2 = Vertex('v')
    e2 = Edge(u2, v2)
    d = {}
    d[e1] = 1
    d[e2] = 3
    assert(len(d.keys()) == 1)
        