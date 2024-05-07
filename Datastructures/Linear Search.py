def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Example usage:
my_list = [10, 20, 30, 40, 50, 60]
target_element = 40
print(linear_search(my_list, target_element))  # Output: 3 (index of the target element)
