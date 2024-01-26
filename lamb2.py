# Lambda function to square and cube numbers in a list
square_cube = lambda x: (x**2, x**3)

# Test the lambda function
numbers = [1, 2, 3, 4, 5]
result = list(map(square_cube, numbers))
print(f"Squared and cubed values of the numbers: {result}")
