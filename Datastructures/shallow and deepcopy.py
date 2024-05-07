import copy

# Shallow copy of a list
original_list = [1, [2, 3], 4]
shallow_copy_list = copy.copy(original_list)

# Modifying the shallow copy
shallow_copy_list[1][0] = 'X'

# Both lists are affected since they share the same inner list
print(original_list)        # Output: [1, ['X', 3], 4]
print(shallow_copy_list)    # Output: [1, ['X', 3], 4]

# Deep copy of a list
original_list = [1, [2, 3], 4]
deep_copy_list = copy.deepcopy(original_list)

# Modifying the deep copy
deep_copy_list[1][0] = 'Y'

# Only the deep copy is affected; the original list remains unchanged
print(original_list)        # Output: [1, [2, 3], 4]
print(deep_copy_list)       # Output: [1, ['Y', 3], 4]
