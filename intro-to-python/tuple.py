
# 1. Creating Tuples
t = (1, 2, 3)
print("Tuple:", t)

# 2. Accessing Elements
print("Access element at index 0:", t[0])

# 3. Immutability (you will get an error from this you cannot change any element inside a tuple)
try:
    t[0] = 5
except TypeError as e:
    print("Error:", e)

# 4. Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# 5. Repetition
t_repeated = (1, 2) * 3
print("Repeated tuple:", t_repeated)

# 6. Length
print("Length of tuple:", len(t))

# 7. Membership Test
print("Is 2 in tuple?", 2 in t)

# 8. Slicing
print("Sliced tuple:", t[1:3])

# 9. Nested Tuples
nested_t = (1, (2, 3), 4)
print("Nested tuple:", nested_t[1])

# 10. Tuple Unpacking
a, b, c = t
print("Tuple Unpacking:", a, b, c)

# 11. Tuple Methods
print("Count of 2 in tuple:", t.count(2))
print("Index of 3 in tuple:", t.index(3))


# 13. Tuple Conversion
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print("Converted list to tuple:", tuple_data)
