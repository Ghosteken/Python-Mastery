from collections import namedtuple

# Creating a namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances
person1 = Person('John', 30, 'New York')
person2 = Person('Alice', 25, 'London')

# Accessing fields using names
print(person1.name)  # Output: John
print(person2.city)  # Output: London
