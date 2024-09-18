"""
Singleton design pattern allows to create only one object
and prevent cloning it to manage global state of program.
"""

class Logger():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print(f"Creating the {cls} object")
            cls._instance = super().__new__(cls)
        return cls._instance

log1 = Logger()
log2 = Logger()
print(log1 is log2)
