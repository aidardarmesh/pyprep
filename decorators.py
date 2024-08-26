def decorator(func):
    def wrapper():
        print("Something happened before argument that is function")
        func()
        print("Something happened after argument that is function")
    
    return wrapper

@decorator
def say_whee():
    print("Whee!")
