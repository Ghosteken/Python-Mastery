

# Open and read content from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# # Open and update content in a text file
# with open('example.txt', 'r') as file:
#     lines = file.readlines()

# # Update specific lines or content as needed
# # For example, update the first line
# lines[0] = 'This text file has been updated with Python.'

# # Write the updated content back to the file
# with open('updated_example.txt', 'w') as file:
#     file.writelines(lines)
