# Using set comprehension to create a new set based on existing list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_numbers = {x for x in numbers}
print(unique_numbers)   # Output: {1, 2, 3, 4}
