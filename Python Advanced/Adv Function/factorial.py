# 5! = 5x4x3x2x1 = 120
# 10! = 10x9x8x7x6x5x4x3x2x1 = 3628800
# 0! = 1 or 1! = 1
def factorial(n): # n= 5, 4
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # 5 * factorial(4) # 4 * factorial(3) # 3 * factorial(2) # 2 * factorial(1)


print(factorial(10))
