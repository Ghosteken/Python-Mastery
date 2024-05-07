def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
