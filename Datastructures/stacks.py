# Implementing a stack using a list
stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)            # Output: [10, 20, 30]

# Pop elements from the stack
popped_item = stack.pop()
print(popped_item)      # Output: 30
print(stack)            # Output: [10, 20]
