#  A decorator in Python is a design pattern that allows you to modify or extend the behavior of functions or methods without altering their actual code. It essentially wraps a function with another function, adding functionality before or after the original function's execution.

def hello_decorator(func):  # A decorator function

    def hello_wraapper(): # The wrapper function that adds extra functionality
        print("Before calling the function.")
        func()
        print("After calling the function.")

    return hello_wraapper # Returning the wrapper function


@hello_decorator
def hello():
    print("Hello, world!")


# hello_decorator(hello)() # Manually applying the decorator
