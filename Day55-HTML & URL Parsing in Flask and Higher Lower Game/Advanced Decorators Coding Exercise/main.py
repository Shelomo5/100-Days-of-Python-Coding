# decoraror logs the name of the function that was called, the arguments it was given and the returned output.
def logging_decorator(function):
    def wrapper(*args,**kwargs):
        # name of function and arguments printed
        print(f"You called {function.__name__}{args}")
        # result is the output of the function a_function
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

# adding decorator to function
@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(1, 2, 3)
