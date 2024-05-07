import heapq

# Creating a max heap (using negative values to simulate max heap)
max_heap = [3, 1, 7, 4, 2, 6]
heapq.heapify(max_heap)
max_heap = [-x for x in max_heap]

# Extracting the maximum element
max_element = -heapq.heappop(max_heap)
print(max_element)  # Output: 7

# Adding elements to the max heap
heapq.heappush(max_heap, -5)
max_heap = [-x for x in max_heap]
print(max_heap)     # Output: [6, 4, 5, 3, 2]
