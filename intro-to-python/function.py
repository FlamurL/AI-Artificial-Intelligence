# 1. Defining a Function
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# 2. Function with Multiple Arguments
def add(a, b):
    return a + b
print("Sum:", add(3, 4))

# 3. Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())
print(greet("Bob"))

# 4. Keyword Arguments
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."
print(introduce(age=30, name="Charlie"))

# 5. Variable-Length Arguments (*args, **kwargs)
def sum_all(*args):
    return sum(args)
print("Sum of all:", sum_all(1, 2, 3, 4, 5))

def display_info(**kwargs):
    return kwargs
print("Information:", display_info(name="David", age=25))

# 6. Lambda Functions
multiply = lambda x, y: x * y
print("Multiplication using Lambda:", multiply(3, 4))

# 7. Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# 8. Returning Multiple Values
def min_max(values):
    return min(values), max(values)
print("Min and Max:", min_max([1, 2, 3, 4, 5]))

# 9. Function with Docstrings
def square(x):
    """
    This function returns the square of the number.
    """
    return x * x
print("Docstring of square function:", square.__doc__)

# 10. Function as First-Class Citizen (passing function as an argument)
def apply_function(func, value):
    return func(value)
print("Apply square function:", apply_function(square, 5))

# 11. Anonymous Function with map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# 12. Function with a return statement
def multiply_by_2(x):
    return x * 2
print("Multiply by 2:", multiply_by_2(10))
