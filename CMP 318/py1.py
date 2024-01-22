def sort_words_alphabetically(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    sorted_string = ' '.join(sorted_words)
    return sorted_string

# Get input from the user
user_input = input("Enter a string: ")


result = sort_words_alphabetically(user_input)


print("Sorted String:", result)
