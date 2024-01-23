def check_key(dictionary, key_to_check):
    if key_to_check in dictionary:
        print(f"The key '{key_to_check}' exists in the dictionary with the value: {dictionary[key_to_check]}")
    else:
        print(f"The key '{key_to_check}' does not exist in the dictionary.")

user_input = input("Enter key-value pairs for the dictionary (format: key1:value1,key2:value2,...): ")
key_value_pairs = [pair.split(':') for pair in user_input.split(',')]

my_dict = dict((key, value) for key, value in key_value_pairs)

key_to_check = input("Enter a key to check if it exists in the dictionary: ")

check_key(my_dict, key_to_check)
