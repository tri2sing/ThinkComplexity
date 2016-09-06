'''
Created on Aug 22, 2016

@author: Sameer Adhikari
'''

class LinearMap(object):
    """Stores a list of tuples, where each tuple is a key-value pair.
    This is not a robust key-value structure as it allows a user to
    enter the same key with multiple values, and returns the first
    inserted value in in case there are multiple entries for a key.
    A real solution would would always return the last inserted value.
    """
    def __init__(self):
        self.items = []
    
    def put(self, key, val):
        """Inserts key-value pair into the map in O(1) time."""
        self.items.append((key, val))
        
    def get(self, key):
        """Returns the value for a key, if it exists, in O(n) time."""
        for k, v in self.items:
            if k == key:
                return v
        raise KeyError
    

class BetterMap(object):
    """Stores a list of tuples, where each tuple is a key-value pair.
    Improves the performance of the get by a constant factor, though it is still O(n) time.
    """
    def __init__(self, n=100):
        self.lmaps = []
        for _ in range(n):
            self.lmaps.append(LinearMap())
            
    def _find_map(self, key):
        index = hash(key) % len(self.lmaps)
        return self.lmaps(index)
            
    def put(self, key, val):  
        m = self._find_map(key)
        m.put(key, val)      
        
    def get(self, key):
        m = self._find_map(key)
        return m.get(key)
    
    
class HashMap(object):
    """Stores a list of tuples, where each tuple is a key-value pair.
    Improves the performance of the get to am amortized O(1) time.
    """
    def __init__(self):
        self.bmap = BetterMap(2)
        self.num = 0
        
    def get(self, key):
        self.bmap.get(key)
        
    def _resize(self):
        # Geometrically grow the hash table.
        new_maps = BetterMap(self.num * 2)
        for m in self.bmap.lmaps:
            # Violation of object-oriented design: direct access of BetterMap attributes.
            # An better alternative would be to write an iterator for BetterMap.
            for k, v in m.items:
                new_maps.put(k, v)
        self.bmap = new_maps

    def put(self, key, val):
        if self.num == len(self.bmap.lmaps):
            # This clause ensures that, on the average, there is only one element in each linear map.
            # Change this to self.num * k = len(self.bmap.maps), for an average of k elements in each linear map.
            self._resize()
     
        
        
        
        
        
        
