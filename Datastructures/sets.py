# Creating a set
colors = {'red', 'blue', 'green'}

# Adding elements
colors.add('yellow')
print(colors)       # Output: {'red', 'blue', 'green', 'yellow'}

# Removing elements
colors.remove('blue')
print(colors)       # Output: {'red', 'green'}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)    # Output: {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
