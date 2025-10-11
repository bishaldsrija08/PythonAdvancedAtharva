import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")

    return wrapper

@log_execution_time
def greet(a, b):
    print(a + b)

greet(5, 6)