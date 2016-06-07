from edge import Edge

class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, u, v):
        """Returns an edge between two vertices if it exists or None otherwise."""
        try:
            return self[u][v]
        except Exception:
            return None

    def remove_edge(self, e):
        """Removes an edge if it exists
        """
        v, w = e
        try:
            if self[v][w]:
                del(self[v][w])
            if self[w][v]:
                del(self[w][v]) 
        except:
            raise ValueError("Trying to remove non-existent edge")
            
    def vertices(self):
        """Returns the list of vertices in the graph."""
        return [k for k in self]

    def edges(self):
        """ Returns a list of all edges in the graph"""
        # The add_edge function duplicates each edge, once for each vertex.
        # We use a set to ensure that we only return unique edges.
        answer = set()
        for src, val in self.iteritems():
            for dest, edge in val.iteritems():
                answer.add(edge)
        return list(answer)
        
        
    def out_edges(self, v):
        """ Returns the list of edges connected to the input vertex."""
        if(self[v]):
            return [self[v][k] for k in self[v]]
        else:
            return None
        
    def add_all_edges(self):
        vs = self.vertices()
        n = len(vs)
        for i in range(n - 1):
            for j in range(i + 1, n):
                self.add_edge(Edge(vs[i], vs[j]))
                