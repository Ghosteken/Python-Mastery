# Creating a list
fruits = ['apple', 'banana', 'orange', 'grape']

# Accessing elements
print(fruits[0])    # Output: 'apple'
print(fruits[-1])   # Output: 'grape'

# Modifying elements
fruits[1] = 'kiwi'
print(fruits)       # Output: ['apple', 'kiwi', 'orange', 'grape']

# Adding elements
fruits.append('melon')
print(fruits)       # Output: ['apple', 'kiwi', 'orange', 'grape', 'melon']

# Removing elements
fruits.remove('orange')
print(fruits)       # Output: ['apple', 'kiwi', 'grape', 'melon']

# Slicing
print(fruits[1:3])  # Output: ['kiwi', 'grape']
