# In Python, *args and **kwargs are special syntaxes used in function definitions to allow a function to accept a variable number of arguments.
def greet(funct):
    def wrapper(*args, **kwargs):
        print("Hello")
        funct(*args, **kwargs)
        print("Goodbye")

    return wrapper


@greet
def add(a, b):
    print(a + b)


add(5, 6)
