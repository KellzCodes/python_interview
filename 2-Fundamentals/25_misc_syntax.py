# comprehension means to initialize a data structure in one line (doesn't work with tuples)
lst = [i for i in range(1, 11)]
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# dictionary comprehension
s = {j: i for i in range(1, 11) for j in range(5)}
print(s) # {0: 10, 1: 10, 2: 10, 3: 10, 4: 10}

# two variables initialized at the same time equal to the same value
x = y = 1
print(x, y) # 1 1

# unpacking means taking some iterable objects and unpacking it into individual values
x, y = 1, 2
print(x, y) # 1 2

# doc string is a multiline comment that describes what a function does
def foo():
    """
    this is the foo function
    """
    pass

help(foo) # this is the foo function