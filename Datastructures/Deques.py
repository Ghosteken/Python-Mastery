from collections import deque

# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])

# Appending elements
my_deque.append(6)
my_deque.appendleft(0)
print(my_deque)     # Output: deque([0, 1, 2, 3, 4, 5, 6])

# Popping elements
my_deque.pop()
my_deque.popleft()
print(my_deque)     # Output: deque([1, 2, 3, 4, 5])
