# Print my name 1000 times
for i in range(1000):
    print("My name is Bishal Rijal.")

# Whole number up to 10.
for i in range(0, 11, 1):
    print(i, end= " ")


# Even number up to 20
for i in range(2, 21, 2):
    print(i, end= " ")

# Odd number up to 20
for i in range(1, 21, 2):
    print(i, end= " ")


# Print : 10 9 8 7 6 5 4 3 2 1
for i in range(10, 0, -1):
    print(i, end= " ")

# Multiplication table of 7
for i in range(1, 11, 1):
    print(f"7x{i}={7*i}")


# Fibonacci series: 0 1 1 2 3 5 8 13 21 34 .....
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end = " ")
    c=a+b # c is the next term
    a=b # a takes the value of b
    b=c # b takes the value of c