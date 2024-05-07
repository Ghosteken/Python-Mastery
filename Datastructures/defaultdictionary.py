from collections import defaultdict

# Creating a defaultdict
my_default_dict = defaultdict(int)

# Adding values
my_default_dict['apple'] = 10
my_default_dict['banana'] = 5

# Accessing a non-existing key will return the default value (0 in this case)
print(my_default_dict['orange'])  # Output: 0

# Accessing an existing key will return its assigned value
print(my_default_dict['apple'])   # Output: 10
