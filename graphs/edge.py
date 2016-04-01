'''
Created on Apr 1, 2016

@author: Sameer Adhikari
'''

class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'E(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""
