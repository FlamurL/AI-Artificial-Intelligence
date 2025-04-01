"""Write a Python program that takes a list of numbers (for example, a = [5, 10, 15, 20]) and creates a new list containing only the first and last elements of the original list.

Requirement:

For practice, put the code inside a function."""


def first_last(l):
    return [l[0]]+ [l[len(l)-1]]

a=[5, 10, 15, 20]

sol=first_last(a)
print(sol)