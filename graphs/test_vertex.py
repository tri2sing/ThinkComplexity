'''
Created on Apr 3, 2016

@author: Sameer Adhikari
'''

from graphs.vertex import Vertex

def test_equal():
    u1 = Vertex('u')
    u2 = Vertex('u')
    assert (u1 == u2)

def test_hash():
    u1 = Vertex('u')
    u2 = Vertex('u')
    d = {}
    d[u1] = 1
    d[u2] = 2
    assert(len(d.keys()) == 1)