# Using zip to combine two lists into a dictionary
keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']

person_dict = dict(zip(keys, values))
print(person_dict)
