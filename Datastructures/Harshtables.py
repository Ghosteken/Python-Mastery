# Creating a hash table
hash_table = {}

# Inserting elements
hash_table['apple'] = 50
hash_table['banana'] = 30
hash_table['orange'] = 25

# Accessing elements
print(hash_table['banana'])  # Output: 30

# Modifying elements
hash_table['apple'] = 40

# Checking if a key exists
if 'orange' in hash_table:
    print("Orange is present in the hash table.")
