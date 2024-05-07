x = [[j for j in range(5)] for i in range(10)]
print(x)
#list1 = [[1,2,3,],[4,5,6]]
#words = 'here is a sentence'.split()

#count_words = [[word,len(word)] for word in words]
#print(count_words)

# Using list comprehension to create a new list based on existing list
numbers = [1, 2, 3, 4, 5]

squared_numbers = [x**2 for x in numbers]
print(squared_numbers)   # Output: [1, 4, 9, 16, 25]

# Using list comprehension with conditionals
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)      # Output: [2, 4]

