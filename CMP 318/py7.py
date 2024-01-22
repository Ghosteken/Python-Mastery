def create_square_dictionary(n):
    square_dict = {key: key ** 2 for key in range(1, n + 1)}
    return square_dict

# Get input from the user for the value of n
n = int(input("Enter a value for n: "))


result_dict = create_square_dictionary(n)


print("Dictionary of keys from 1 to", n, "with values as the square of keys:")
print(result_dict)
