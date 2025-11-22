def calculate_sth(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Cannot divide by zero"
    return result

print(calculate_sth(40,0))