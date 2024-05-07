# Using map function to apply a function to each element of a list
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))
print(squared_numbers)   # Output: [1, 4, 9, 16, 25]
