# Using string join to concatenate elements of a list into a single string
fruits = ['apple', 'banana', 'orange']

joined_string = ', '.join(fruits)
print(joined_string)   # Output: apple, banana, orange
# Using string join to concatenate elements of a list into a single string
fruits = ['apple', 'banana', 'orange']
print(joined_string)   # Output: apple, banana, orange
#words =str.split ('appleeee and banana and orange')
#sorted(words, key=len)

#print(words)
sl = [1,2,44,4,9,6,7,3]
sl.sort()
print(sl)

def iterTest(low, high):
    while low <= high:
        print(low)
        low = low+1
        
        
def recursiveTest(low, high):
    if low <= high:
        print(low)
        recursiveTest(low+1, high)        