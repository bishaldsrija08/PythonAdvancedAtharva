# WAP to print 10 to 1 using recursion

def print_reverse(n): # 10 9
    # Base case
    if n==0:
        return # Return helps to exit from the function
    print(n, end= " ")
    # Recursive case
    print_reverse(n-1)

# Driver code
num = 10
print_reverse(num) # 10

# # WAP to print 1 to 10

def print_reverse(n): # 10 9
    # Base case
    if n>=11:
        return # Return helps to exit from the function
    print(n, end= " ")
    # Recursive case
    print_reverse(n+1)

# Driver code
num = 1
print_reverse(num) # 10