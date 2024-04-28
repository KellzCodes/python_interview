x = [1, 2, 3, True, 3.4, "Hello"]

# print the first element of the list
print(x[0]) # 1

# change the first element of the list
x[0] = 4
print(x) # [4, 2, 3, True, 3.4, 'Hello']

# add an element to the end of the list
x.append("last element")
x.append(2)
print(x) # [4, 2, 3, True, 3.4, 'Hello', 'last element', 2]

# print the length of a list
print(len(x)) # 8

# remove the last element of the list
x.pop()
print(x) # [4, 2, 3, True, 3.4, 'Hello', 'last element']
popped = x.pop()
print(popped) # last element
print(x) # [4, 2, 3, True, 3.4, 'Hello']

# count how many times an element occurs in a list
count = x.count(4)
print(count) # 1

# get the index in which the element first occurs
index = x.index(3)
print(index) # 2

# remove the first occurence of an element from a list
x.remove(4)
print(x) # [2, 3, True, 3.4, 'Hello']

# check to see if a list contains an element
list_contains_5 = 5 in x
print(list_contains_5) # False

# access element from the back of the list
y = [1, 2, 3, "world", "Hello"]
print(y[-1]) # Hello

# combine lists
a = [1, 2, 3]
b = [1, 2]
combined = a + b
print(combined) # [1, 2, 3, 1, 2]

# extend list
a.extend(b)
print(a) # [1, 2, 3, 1, 2]
#--------------------------------------
# nesting list
lst = [[5, 6, [100]], [2, 3], [1, 2, 3]]

# access middle element in last list in the list
print(lst[-1][1]) # 2

# access third element in first list of the list
print(lst[0][2]) # [100]

# access the first element of the third element in the first list of the list
print(lst[0][2][0]) # 100