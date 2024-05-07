import heapq

# Creating a min heap
min_heap = [3, 1, 7, 4, 2, 6]

heapq.heapify(min_heap)

# Extracting the minimum element
min_element = heapq.heappop(min_heap)
print(min_element)  # Output: 1

# Adding elements to the heap
heapq.heappush(min_heap, 5)
print(min_heap)     # Output: [2, 4, 5, 7, 3, 6]
