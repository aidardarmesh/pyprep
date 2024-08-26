from decorators import timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([num ** 2 for num in range(10_000)])

waste_some_time(1)
waste_some_time(999)
