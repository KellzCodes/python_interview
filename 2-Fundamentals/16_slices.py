# print a slice of the first two elements in a list
my_list = [0, 1, 2, 3, 4, 5, 6]
new_list = my_list[0:2]
print(new_list) # [0, 1]

# print a slice of the first four elements in a list
my_list = [0, 1, 2, 3, 4, 5, 6]
new_list = my_list[:4]
print(new_list) # [0, 1, 2, 3]

# print a slice: start at index 1, end at index 6, step by 2
my_list = [0, 1, 2, 3, 4, 5, 6]
new_list = my_list[1:6:2]
print(new_list) # [1, 3, 5]

# print a slice: start at index 0, end at index 8, step by 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = my_list[:8:3]
print(new_list) # [1, 4, 7]

# Negative Index Slicing: start at index 8, end at index 0, step by -1
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = my_list[8:0:-1]
print(new_list) # [9, 8, 7, 6, 5, 4, 3, 2]

# print a slice: start at index -4, stop at index 0, step by -1
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = my_list[-4:0:-1]
print(new_list) # [9, 8, 7, 6, 5, 4, 3, 2]

# Copy an entire list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = my_list[:]
print(new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Reverse copy an entire list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_list = my_list[::-1]
print(new_list) # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Slice a string: print every other character
string = "hello world"
print(string[::2]) # hlowrd

# Slice a string: start at index 1, include the last index, step by 2
string = "hello world"
print(string[1::2]) # el ol

# Slice a string: start at index 1, stop at index 6, step by 2
string = "hello world"
print(string[1:6:2]) # el

# Slice a tuple: start at index 1, stop at index 6, step by 2
tup = 0, 1, 2, 3, 4, 5, 6, 7
print(tup[1:6:2]) # (1, 3, 5)