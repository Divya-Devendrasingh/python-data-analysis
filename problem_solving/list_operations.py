# List Operations Practice

numbers = [1, 2, 3, 4, 5]

# 1. Filter even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# 2. Square all numbers
squares = [n * n for n in numbers]
print("Squares:", squares)

# 3. Label numbers as even/odd
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Labels:", labels)

# 4. Sum of even numbers
sum_even = sum([n for n in numbers if n % 2 == 0])
print("Sum of evens:", sum_even)

# 5. Find numbers greater than 3
greater_than_3 = [n for n in numbers if n > 3]
print("Greater than 3:", greater_than_3)
