def sort_words_alphabetically(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=lambda x: x.lower())
    sorted_string = ' '.join(sorted_words)
    return sorted_string

user_input = input("Enter a string: ")

result = sort_words_alphabetically(user_input)

print("Sorted String:", result)
