'''
Created on Apr 3, 2016

@author: Sameer Adhikari
'''

import pytest
from graphs.vertex import Vertex
from graphs.edge import Edge
from graphs.graph import Graph

@pytest.fixture(scope = 'module')
def test_graph():
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    e1 = Edge(v, w)
    g = Graph([v, w], [e1])
    e2 = Edge(u, v)
    g.add_vertex(u)
    g.add_edge(e2)
    return g

def test_get_edge(test_graph):   
    u = Vertex('u')
    v = Vertex('v') 
    etest = Edge(u, v)
    ereturn = test_graph.get_edge(u, v)
    assert( etest == ereturn)