# Using lambda function to create an anonymous function
square = lambda x: x**2
print(square(5))   # Output: 25

# Using lambda function with map and filter
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)   # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)      # Output: [2, 4]
