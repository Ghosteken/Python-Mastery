from collections import ChainMap

# Creating dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Combining dictionaries using ChainMap
combined_dict = ChainMap(dict1, dict2)

# Accessing values in the combined dictionary
print(combined_dict['a'])  # Output: 1
print(combined_dict['c'])  # Output: 3
