# print numbers from n to 1 using recursion
def series(n):
    # base case
    if n==0:
        return
    print(n, end=" ")
    # recursive cases
    return series(n-1)
n = 10
series(n)