# create a set
x = set() # empty set
y = {1, 2, 3} # non-empty set
z = {} # empty dictionary
print(type(x)) # <class 'set'>
print(type(y)) # <class 'set'>
print(type(z)) # <class 'dict'>

# print a set
x = {1, 2, 2, 1, 2, 1}
print(x) # {1, 2}

# add to a set
x = {1, 2, 2, 1, 2, 1}
x.add(3)
print(x) # {1, 2, 3}

# remove an element from a set
x = {1, 2, 2, 1, 2, 1, 3}
x.remove(3)
print(x) # {1, 2}

# remove all elements from a set
x = {1, 2, 2, 1, 2, 1, 3}
x.clear()
print(x) # set()

# print the length of a set
x = {1, 2, 2, 1, 2, 1, 3, "Hello", True, 0.2, (1, 2)}
print(len(x)) # 6

# find an item in a set
x = {1, 2, 2, 1, 2, 1, 3}
contains = 1 in x
print(contains) # True

# union (combination) of two sets
x = {1, 2}
y = {2, 3}
z = x.union(y)
print(z) # {1, 2, 3}

# union (combination) of two sets (alternative)
x = {1, 2}
y = {2, 3}
z = x | y
print(z) # {1, 2, 3}

# intersection of two sets (only keep the elements found in both sets)
x = {1, 2, 3}
y = {1, 2, 4}
z = x.intersection(y)
print(z) # {1, 2}

# intersection of two sets (alternative)
x = {1, 2, 3}
y = {1, 2, 4}
z = x & y
print(z) # {1, 2}

# difference of two sets (only keep the elements in the first set that is not found in the second set)
x = {1, 2, 3}
y = {1, 2, 4}
z = x.difference(y)
print(z) # {3}

# difference of two sets (alternative)
x = {1, 2, 3}
y = {1, 2, 4}
z = x - y
print(z) # {3}

# symmetric difference of two sets (only keep the elements that are not shared between the two sets)
x = {1, 2, 3}
y = {1, 2, 4}
z = x.symmetric_difference(y)
print(z) # {3, 4}

# symmetric difference of two sets (alternative)
x = {1, 2, 3}
y = {1, 2, 4}
z = x ^ y
print(z) # {3, 4}

# modify a set by adding all the elements from another set
x = {1, 2, 3}
y = {1, 2, 4}
x.update(y)
print(x) # {1, 2, 3, 4}

# modify a set with the difference of another set
x = {1, 2, 3}
y = {1, 2, 4}
x.difference_update(y)
print(x) # {3}

# modify a set with the symmetric difference of another set
x = {1, 2, 3}
y = {1, 2, 4}
x.symmetric_difference_update(y)
print(x) # {3, 4}

# check to see if a set is a subset of another set (are all the elements in one set contained in another set)
x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6, 7}
print(x.issubset(y)) # True

# check to see if a set is a subset of another set (alternative)
x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6, 7}
print(x <= y) # True

# check to see if a set is a superset of another set (does a set contain all the elements of another set)
x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6, 7}
print(y.issuperset(x)) # True

# check to see if a set is a superset of another set (alternative)
x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6, 7}
print(y >= x) # True

# check to see if a set is a proper superset of another set (both sets are not equal)
x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6, 7}
print(y > x) # True

# check to see if a set is a proper subset of another set (both sets are not equal)
x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6, 7}
print(x < y) # True

# convert list to a set
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set_x = set(x)
print(set_x) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# convert a string to a set
x = "helloworld"
set_x = set(x)
print(set_x) # {'r', 'o', 'w', 'l', 'd', 'e', 'h'}

# ask user to input a bunch of numbers but program stops when they enter a number they already used
numbers = set()
while True:
    num = int(input("Number: "))
    if num in numbers:
        break
    numbers.add(num)

'''
Write a program that continually asks the user to enter characters until the user enters a previously entered character
or more than one character at a time. After, the program should print the number of unique characters that were entered.

Use a set to accomplish this.
'''
characters = set()
while True:
    element = input("Enter a character: ")
    if element in characters or len(element) > 1:
        break
    characters.add(element)
print(f"Number of unique characters entered: {len(characters)}")