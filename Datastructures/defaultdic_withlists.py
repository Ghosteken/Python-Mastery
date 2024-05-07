from collections import defaultdict

# Creating a defaultdict with a list as the default value
my_dict = defaultdict(list)

# Adding values to the list using keys
my_dict['fruits'].append('apple')
my_dict['fruits'].append('banana')
my_dict['fruits'].append('orange')

my_dict['vegetables'].append('carrot')
my_dict['vegetables'].append('spinach')

print(my_dict)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana', 'orange'], 'vegetables': ['carrot', 'spinach']})
