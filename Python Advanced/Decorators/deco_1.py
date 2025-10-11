def repat_decorator(func):
    def wrapper():
        print("The function is called multiple times:")
        func()
        func()

    return wrapper


@repat_decorator
def greet():
    print("Hello!")

greet()

# The function is called multiple times:
# Hello!
# Hello!
# Hello!