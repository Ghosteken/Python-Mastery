def binary_search(arr, target):
    low, high = 0,len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
               
            high = mid - 1
            
    return -1


sorted_list = [10, 20, 30, 40, 50, 60]
target_element = 40
print(binary_search(sorted_list, target_element))  


