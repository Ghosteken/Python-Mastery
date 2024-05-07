# Using filter function to filter elements from a list based on a condition
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(is_even, numbers))
print(even_numbers)      # Output: [2, 4]
