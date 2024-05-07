def bubbleSort(arr):
    n = len(arr)
    iterations = 0  

    for i in range(n - 1):
        swapped = False

        for j in range(0, n - i - 1):
            iterations += 1  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            
            break

    return iterations

arr = [15,90,43,12,6]
iterations = bubbleSort(arr)
print("Sorted array:", arr)
print("Number of iterations:", iterations)
