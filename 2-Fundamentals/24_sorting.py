# .sort() method sorts a data structure in place (modify a data structure) in ascending order
lst = [2, 4, 6, 9, 3, 1, 7, 5, 6, 0]
lst.sort()
print(lst) # [0, 1, 2, 3, 4, 5, 6, 6, 7, 9]

# sorted() function returns a new sorted data structure in ascending order
lst = [3,4,7,5,9,1,3]
print(sorted(lst)) # [1, 3, 3, 4, 5, 7, 9]

# modify and sort a list in descending order
lst = [3,4,7,5,9,1,3]
lst.sort(reverse=True)
print(lst) # [9, 7, 5, 4, 3, 3, 1]

# sort a new list in descending order
lst = [3,4,7,5,9,1,3]
print(sorted(lst, reverse=True)) # [9, 7, 5, 4, 3, 3, 1]

# when you sort a tuple it returns as a list (cannot use .sort() on a tuple)
lst = (3,4,7,5,9,1,3)
print(sorted(lst, reverse=True)) # [9, 7, 5, 4, 3, 3, 1]

# print a sorted tuple
lst = (3,4,7,5,9,1,3)
print(tuple(sorted(lst, reverse=True))) # (9, 7, 5, 4, 3, 3, 1)

# modify and sort a nested list (nested list will only sort by first element in each nested list)
lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
lst.sort()
print(lst) # [[-1, -2], [0, 0], [1, -2], [3, -4], [5, -6]]

# modify and sort a nested list by using a function as a key (sort by second index)
def sort_second_index(item):
    return item[1]

lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
lst.sort(reverse=True, key=sort_second_index)
print(lst) # [[0, 0], [-1, -2], [1, -2], [3, -4], [5, -6]]

# sort a nested list by the sum of each list
def sort_sum(item):
    return sum(item)

lst = [[1, -2], [3, -4], [5, -6], [-1, -2], [0, 0]]
new_list = sorted(lst, key=sort_sum)
print(new_list) # [[-1, -2], [1, -2], [3, -4], [5, -6], [0, 0]]