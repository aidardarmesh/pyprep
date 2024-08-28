"""
Iterator is an object that allows you to traverse through all elements 
of a collection one at a time without indexing them explicitly. 
Implements __iter__() that returns itself and __next__() that returns next time. 
"""

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index -= 1
        return self.data[self.index]


