def convert_case(input_string):
    uppercase_string = input_string.upper()
    lowercase_string = input_string.lower()

    return uppercase_string, lowercase_string

# Get input from the user
user_input = input("Enter a string: ")


uppercase_result, lowercase_result = convert_case(user_input)


print("Original String:", user_input)
print("Uppercase String:", uppercase_result)
print("Lowercase String:", lowercase_result)
