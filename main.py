from decorators import timer, debug, slow_down

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

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

