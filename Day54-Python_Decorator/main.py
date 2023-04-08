import time

# calculates time it takes to execute the slow_function vs the fast_function
def speed_calc_decorator(function):
    def wrapper_function():
        # current time in seconds since January 1, 1970, 00:00:00
        before_time = time.time()
        function()
        after_time = time.time()
        # subtract time after function was run compared to what it was when we started function
        execute_time = (after_time - before_time)
        # gives you the name of the function
        function_name = function.__name__
        print(f"{function_name} run speed:{execute_time}s")
    return wrapper_function

# adding decorator to function
@speed_calc_decorator
# fast function because there's less 0's than the slow function
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

# execute functions
fast_function()
slow_function()

