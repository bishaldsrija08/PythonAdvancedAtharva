def fibo(n): # n=0, 1, 2, 3
    
    # Base case
    if n<=1:
        return n
    else:
        # Recursive call
        return fibo(n-1)+fibo(n-2) #

n=int(input("Enter the number of terms: "))
for i in range(n):
    # Driver code
    print(fibo(i), end= " ")