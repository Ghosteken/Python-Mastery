def print_even_odd_positions(lst):
    even_positions = [item for index, item in enumerate(lst) if index % 2 == 0]
    odd_positions = [item for index, item in enumerate(lst) if index % 2 != 0]

    print("Items at even positions:", even_positions)
    print("Items at odd positions:", odd_positions)

# Get input from the user
user_input = input("Enter a list of items (comma-separated): ")
user_list = user_input.split(',')

# Call the function to print items at even and odd positions
print_even_odd_positions(user_list)
