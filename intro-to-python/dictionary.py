#dictionaries are like hashTables in java, maps in cpp

# 1. Creating a Dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", d)

# 2. Accessing Elements
print("Access value for key 'a':", d['a'])

# 3. Adding/Updating Elements
d['d'] = 4
d['a'] = 10
print("Updated Dictionary:", d)

# 4. Removing Elements
del d['b']
print("Dictionary after removing key 'b':", d)

# 5. Checking Key Existence
print("Is key 'c' in dictionary?", 'c' in d)

# 6. Dictionary Methods
print("Keys in dictionary:", d.keys())
print("Values in dictionary:", d.values())
print("Items in dictionary:", d.items())

# 7. Dictionary Comprehensions
squared = {key: value**2 for key, value in d.items()}
print("Dictionary comprehension (squared values):", squared)

# 8. Nested Dictionaries
nested_dict = {'a': {'x': 10, 'y': 20}, 'b': {'x': 30, 'y': 40}}
print("Access value in nested dictionary (nested_dict['a']['x']):", nested_dict['a']['x'])

# 9. Merging Dictionaries
d2 = {'e': 5, 'f': 6}
merged_dict = {**d, **d2}
print("Merged Dictionary:", merged_dict)

# 10. Default Dictionary with get() method
print("Value for key 'z' (non-existing):", d.get('z', 'Not Found'))

# 11. Dictionary from List of Tuples
tuples_list = [('x', 1), ('y', 2), ('z', 3)]
dict_from_tuples = dict(tuples_list)
print("Dictionary from list of tuples:", dict_from_tuples)

# 12. Iterating through a Dictionary
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

# 13. Copying a Dictionary
copied_dict = d.copy()
print("Copied Dictionary:", copied_dict)
