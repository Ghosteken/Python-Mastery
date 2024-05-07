from collections import OrderedDict

# Creating an ordered dictionary
my_ordered_dict = OrderedDict()

# Inserting elements
my_ordered_dict['apple'] = 50
my_ordered_dict['banana'] = 30
my_ordered_dict['orange'] = 25

# Iterating through the ordered dictionary
for fruit, quantity in my_ordered_dict.items():
    print(f"{fruit}: {quantity}")

# Output:
# apple: 50
# banana: 30
# orange: 25
