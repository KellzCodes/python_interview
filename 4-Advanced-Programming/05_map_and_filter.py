import math

# generate a list that contains the squares of all the elements of a list
lst = [1, 2, 3, 4, 5, 6, 7]
new_lst = list(map(lambda x: x**2, lst))
print(new_lst)  # [1, 4, 9, 16, 25, 36, 49]

# generate a list that contains the square root of the elements in a list
lst = [49, 64, 81, 100, 121, 144]
new_lst = list(map(lambda x: math.sqrt(x), lst))
print(new_lst)  # [7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

# generate the sum of nested lists
lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
new_lst = list(map(lambda x: sum(x), lst))
print(new_lst) # [6, 15, 6, 7]

# filter a nested list for items with a sum greater than 6
lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
new_lst = list(filter(lambda x: sum(x) > 6, lst))
print(new_lst)  # [[4, 5, 6], [3, 4]]

# filter a nested list for items with a length greater than 2
lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
new_lst = list(filter(lambda x: len(x) > 2, lst))
print(new_lst)  # [[1, 2, 3], [4, 5, 6], [1, 2, 3]]

# use map and filter to find the sums of nested lists that are even numbers
lst = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [3, 4]]
new_lst = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), lst))
print(list(new_lst))  # [6, 6]

'''
Use the map and filter to create an iterable object that contains the even squares of all elements in a list. 
Once you've created theis iterable, print out all of its values on separate lines. 

You should use lambda's for an functions you create.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = map(lambda x: x**2, lst)
new_lst = filter(lambda y: y % 2 == 0, squares)
for element in new_lst:
    print(element)