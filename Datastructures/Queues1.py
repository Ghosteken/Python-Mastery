import queue

# Creating a queue
my_queue = queue.Queue()

# Enqueuing elements
my_queue.put(10)
my_queue.put(20)
my_queue.put(30)

# Dequeuing elements
while not my_queue.empty():
    item = my_queue.get()
    print(item, end=' ')  # Output: 10 20 30
