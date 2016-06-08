'''
Created on Jun 8, 2016

@author: Sameer Adhikari
'''

from graphs.src.graph import Graph
from random import random
from graphs.src.edge import Edge

class RandomGraph(Graph):
    def add_random_edges(self, p):
        '''
        Add edges at random.
        p: probability that there is an edge between any two nodes.
        '''
        vs = self.vertices()
        n = len(vs)
        for i in range(n - 1):
            for j in range(i + 1, n):
                r = random()
                if r < p:
                    self.add_edge(Edge(vs[i], vs[j]))
                
        
        
