from collections import Counter

# Creating a counter
my_list = [1, 2, 3, 4, 2, 3, 5, 2, 1]
my_counter = Counter(my_list)

# Counting occurrences
print(my_counter)       # Output: Counter({2: 3, 1: 2, 3: 2, 4: 1, 5: 1})

# Most common elements
print(my_counter.most_common(2))   # Output: [(2, 3), (1, 2)]
