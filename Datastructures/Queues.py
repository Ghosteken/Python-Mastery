from collections import deque

# Implementing a queue using a deque
queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)            # Output: deque([10, 20, 30])

# Dequeue elements
dequeued_item = queue.popleft()
print(dequeued_item)    # Output: 10
print(queue)            # Output: deque([20, 30])
