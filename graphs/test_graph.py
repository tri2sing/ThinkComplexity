'''
Created on Apr 3, 2016

@author: Sameer Adhikari
'''

import pytest
from graphs.vertex import Vertex
from graphs.edge import Edge
from graphs.graph import Graph

@pytest.fixture(scope='module')
def test_graph():
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    z = Vertex('z')

    e1 = Edge(u, v)
    e2 = Edge(v, w)
    e3 = Edge(x, y)
    e4 = Edge(y, z)
    e5 = Edge(v, y)
    e6 = Edge(w, z)

    g = Graph([u, v, w, x, y, z], [e1, e2, e3, e4, e5, e6])
    return g

def test_get_edge(test_graph):   
    u = Vertex('u')
    v = Vertex('v') 
    test_edge = Edge(u, v)
    returned_edge = test_graph.get_edge(u, v)
    assert(returned_edge == test_edge)
    
def test_remove_edge(test_graph):
    w = Vertex('w')
    z = Vertex('z')
    check_edge = Edge(w, z)
    returned_edge = test_graph.get_edge(w, z)
    assert(returned_edge == check_edge)
    test_graph.remove_edge(check_edge)
    returned_edge = test_graph.get_edge(w, z)
    assert(returned_edge == None)
    
def test_vertices(test_graph):
    returned_vertices = test_graph.vertices()
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    z = Vertex('z')
    check_vertices = [u, v, w, x, y, z]
    assert(len(returned_vertices) == len(check_vertices))
    # A set as test for equality requires the elements be hashable.
    # Also requires that no vertex has been removed from the fixture.
    assert(set(returned_vertices) == set(check_vertices))

def test_edges():
    # We do know the order in which individual tests are called.
    # We need to accommodate a possible call of remove_edge.
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')

    e1 = Edge(u, v)
    e2 = Edge(v, w)
    e3 = Edge(w, u)
    check_edges = [e1, e2, e3]
    g = Graph([u, v, w], check_edges)
    returned_edges = g.edges()
    assert(len(returned_edges) == len(check_edges))
    assert(set(returned_edges) == set(check_edges))
    
    
    
    
    