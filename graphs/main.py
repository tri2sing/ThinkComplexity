'''
Created on Apr 1, 2016

@author: Sameer Adhikari
'''

from graphs.vertex import Vertex
from graphs.edge import Edge
from graphs.graph import Graph


def main(script, *args):
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    g = Graph([v, w], [e])
    print "Graph with first edge"
    print g

    u = Vertex('u')
    g.add_vertex(u)
    e = Edge(u, v)
    g.add_edge(e)
    print "Graph with one more edge"
    print g

    print "list of vertices"
    print g.vertices()
    
    print "list of edges for vertex v"
    print g.out_edges(v)
    
    x = Vertex('X')
    print "Edge vx"
    print g.get_edge(v, x)
    print "Edge vw"
    print g.get_edge(v, w)
    
    g.remove_edge(e)
    print "Grah after removing edge uvs"
    print g.get_edge(v, w)
    
    

if __name__ == '__main__':
    import sys
    main(*sys.argv)