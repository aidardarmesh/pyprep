import functools

# def decorator(saying):
#     print(saying)
#     def inner_fn(func):
#         @functools.wraps(func)
#         def wrapper_decorator(*args, **kwargs):
#             value = func(*args, **kwargs)
#             return value
#         return wrapper_decorator
#     return inner_fn

class Decorator:
    def __init__(self, saying):
        self.saying = saying

    def __call__(self, func):
        print(self.saying)

        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        return wrapper_decorator


Decorator("abc")


@Decorator("abc")
def say_whee():
    print("Whee!")


new_say_whee = Decorator("abc")(say_whee)()


import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down
