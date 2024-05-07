# Using dictionary comprehension to create a new dictionary based on existing list
fruits = ['apple', 'banana', 'orange']

fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)    # Output: {'apple': 5, 'banana': 6, 'orange': 6}
