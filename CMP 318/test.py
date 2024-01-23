# Function to generate a list with square and cube of each number
def generate_square_and_cube_list(numbers):
    square = map(lambda x: x**2, numbers)
    cube = map(lambda x: x**3, numbers)

    result = list(zip(numbers, square, cube))
    return result

# Example usage
numbers_list = [1, 2, 3, 4, 5]

result_list = generate_square_and_cube_list(numbers_list)

# Display the result
print("Number\tSquare\tCube")
for item in result_list:
    print(f"{item[0]}\t{item[1]}\t{item[2]}")
