# Function
# A function is a block of code that performs a specific task.


# function with no parameters and no return values
def greet():  # Function definition
    print("Hello, welcome to the function tutorial!")
greet()  # Function call


# function with parameters and no return values
def sum(a, b):  # Function definition with parameters
    print("The sum is:", a + b)
sum(5, 10)  # Function call with arguments


# function with parameters and return values
def multiply(x, y):
    return x * y  # Function definition with return value

result = multiply(4, 5)  # Function call with arguments
print("The product is:", result)