"""
Generators are a simple and powerful tool for creating iterators. 
They are written like regular functions but use the yield statement whenever they want to return data.
Anything that can be done with generators can also be done 
with class-based iterators as described in the previous section.
"""

def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for ch in reverse('spam'):
    print(ch)
