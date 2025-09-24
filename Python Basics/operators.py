# What operator are?
# Operators are special symbols in Python that carry out arithmetic or logical computation.

# Arithmetic Operators => + - * / % // **

a = 10
b = 3

print("Addition=", a + b)
print("Subtraction=", a - b)
print("Multiplication=", a * b)
print("Division=", a / b)
print("Modulus=", a % b) # It gives remainder (Modulus %)
print("Floor Division=", a // b) # It gives quotient (Floor Division //)
print("Exponentiation=", a ** b)

# Comparison Operators => == != > < >= <=

print(5>4)
print(5<4)
print(5==4)
print(5!=4) # Not equal to
print(5>=4)
print(5<=4)

# Logical Operators => and or not
print("And Operator")
print((5>4) and (4<3)) # and operator returns True if both the conditions are True

print("OR Operator")
print((5>4) or (4<3)) # or operator returns True if at least one condition is True

print("Not Operator")
print(not(5>4)) # not operator reverses the result, returns False if the result is True