def sort_words_alphabetically(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    sorted_string = ' '.join(sorted_words)
    return sorted_string

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to sort the words alphabetically
result = sort_words_alphabetically(user_input)

# Display the result
print("Sorted String:", result)
