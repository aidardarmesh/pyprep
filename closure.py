"""
Clouse is a function that remembers environment where it was created even though it doesn't exist anymore. 
"""

def make_counter():
    counter = 0

    def increase():
        nonlocal counter
        counter += 1
        return counter
    
    return increase

counter_a = make_counter()
print(counter_a())
print(counter_a())
print(counter_a())

counter_b = make_counter()
print(counter_b())
print(counter_b())
