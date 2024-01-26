# Lambda function to filter even numbers in a list
filter_even = lambda x: x % 2 == 0

# Test the lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(filter_even, numbers))
print(f"Filtered even numbers: {filtered_numbers}")
