def say_whee():
    print("Whee!")

def decorator(func):
    def wrapper():
        print("Something happened before argument that is function")
        func()
        print("Something happened after argument that is function")
    
    return wrapper

say_whee = decorator(say_whee)
