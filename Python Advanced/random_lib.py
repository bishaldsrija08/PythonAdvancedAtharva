import random

a = ["apple", "banana", "cherry", "date"]
print(random.choice(a))  # Randomly selects and prints an element from the list 'a'


# Generate a random float number

number = random.random()*10000000
print(int(number))  # Prints a random float number between 0.0 and 1.0


print(random.randint(-1000000, -1))  # Prints a random integer between 1 and 100000 (inclusive)


name = "abcdefghijklmnopqrstuvwxyz"

print(random.choice(name))

