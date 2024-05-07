# Creating a dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print(person['name'])    # Output: 'John'
print(person.get('age')) # Output: 30

# Modifying elements
person['age'] = 31
print(person)            # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding elements
person['occupation'] = 'Engineer'
print(person)            # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

# Removing elements
del person['city']
print(person)            # Output: {'name': 'John', 'age': 31, 'occupation': 'Engineer'}
