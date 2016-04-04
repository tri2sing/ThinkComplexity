'''
Created on Apr 3, 2016

@author: Sameer Adhikari
'''

from graphs.vertex import Vertex

def test_equality():
    u1 = Vertex('u')
    u2 = Vertex('u')
    assert (u1 == u2)
