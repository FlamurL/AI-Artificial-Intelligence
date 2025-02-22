"""
Write a function that, for a given list of tuples in the form [(‘a’, 1), (‘b’, 2), (‘c’, 3)], swaps the elements in the tuples so that the element at position 0 becomes the element at position 1, and vice versa. Use list comprehension.

Example input:
[(‘a’, 1), (‘b’, 2), (‘c’, 3)]

Example output:
[(1, ‘a’), (2, ‘b’), (3, ‘c’)]



"""
def swapElementsInsideTuple(list):
    return [(y,x) for (x,y) in list]

if __name__ == "__main__":
    li = [('a', 1), ('b', 2), ('c', 3)]
    print(swapElementsInsideTuple(li))
