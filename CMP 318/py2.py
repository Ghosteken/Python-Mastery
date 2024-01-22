def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = {vowel: 0 for vowel in vowels}

    for char in input_string:
        if char in vowels:
            vowel_count[char] += 1

    return vowel_count

# Get input from the user
user_input = input("Enter a string of words: ")


vowel_counts = count_vowels(user_input)


print("Vowel Counts:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
