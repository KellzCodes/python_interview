x = (1, 2, 3)

# print an element from a tuple
print(x[1]) # 2

# print the length of a tuple
print(len(x)) # 3

# count how many times an element appears in a tuple
count = x.count(1)
print(count) # 1

# get the index of the first occurence of an element
index = x.index(3)
print(index) # 2

# check to see if an element is in a tuple
contains = 2 in x
print(contains) # True

# print a nested tuple
x = (1, 2, 3, (1, 2), True, [])
print(x) # (1, 2, 3, (1, 2), True, [])

# Access nested tuple
print(x[3]) # (1, 2)

# Access the first element in a nested tuple
print(x[3][0]) # 1

# add multiple tuples together
x = (1, 2)
y = (3, 4)
combined = x + y
print(combined) # (1, 2, 3, 4)

# multiply tuples
combined = x * 2
print(combined) # (1, 2, 1, 2)

# create a tuple without parenthesis
x = 1, 2, 3, 4
print(x) # (1, 2, 3, 4)