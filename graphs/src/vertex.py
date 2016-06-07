'''
Created on Apr 1, 2016

@author: Sameer Adhikari
'''

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return '%s' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""

    def __eq__(self, other):
        if type(other) is type(self):
            return self.label == other.label
        return False

    def __hash__(self):
        return hash(self.label)

