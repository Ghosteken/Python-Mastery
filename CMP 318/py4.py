# Method 1: Using reverse() method
def print_reverse_using_reverse(lst):
    reversed_list = lst.copy()
    reversed_list.reverse()
    print("Reversed List (using reverse() method):", reversed_list)

# Method 2: Using slicing
def print_reverse_using_slicing(lst):
    reversed_list = lst[::-1]
    print("Reversed List (using slicing):", reversed_list)

# Get input from the user
user_input = input("Enter a list of items (comma-separated): ")
user_list = user_input.split(',')

# Call the functions to print the list in reverse order
print_reverse_using_reverse(user_list)
print_reverse_using_slicing(user_list)
