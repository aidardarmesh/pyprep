from decorators import timer, debug

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([num ** 2 for num in range(10_000)])

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy, {name}!"
    else:
        return f"Whoa, {name}! {age} already, growing up!"

make_greeting("Benjamin")
make_greeting("Juan", age=114)
