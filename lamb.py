# Lambda function to add 10 to a given number
add_10 = lambda x: x + 10

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y

# Test the lambda functions
num = int(input("Enter a number: "))
result_add_10 = add_10(num)
print(f"Result of adding 10 to {num}: {result_add_10}")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result_multiply = multiply(num1, num2)
print(f"Result of multiplying {num1} and {num2}: {result_multiply}")
