from collections import OrderedDict

# Creating an ordered dictionary with sorting based on keys
unordered_dict = {'apple': 50, 'banana': 30, 'orange': 25}

sorted_dict = OrderedDict(sorted(unordered_dict.items()))

print(sorted_dict)  # Output: OrderedDict([('apple', 50), ('banana', 30), ('orange', 25)])
