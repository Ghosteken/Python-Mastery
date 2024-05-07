import queue

# Creating a stack
my_stack = queue.LifoQueue()

# Pushing elements onto the stack
my_stack.put(10)
my_stack.put(20)
my_stack.put(30)

# Popping elements from the stack
while not my_stack.empty():
    item = my_stack.get()
    print(item, end=' ')  # Output: 30 20 10
