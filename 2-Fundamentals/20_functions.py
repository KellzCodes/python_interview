# define a function with a parameter
def print_value(value):
    print(value)


# define a function without a parameter
def print_value2():
    print("hello")


# call a function with a parameter
print_value("hello")  # hello

# call a function without a parameter
print_value2()  # hello


# create a function with multiple parameters
def add_5(x, y):
    result = x + y + 5
    print(result)


add_5(5, 5)  # 15


# create a function that has a return value
def add_6(x, y, z):
    result = x + y + z + 6
    return result


x = 5
y = 7
z = 2
a = add_6(x, y, z)
print(a)  # 20


# create a function that returns a value based on a condition
def get_negative_sum(x, y, z):
    result = x + y + z
    if result < 0:
        return result
    return 1


x = -5
y = -7
z = -2
print(get_negative_sum(x, y, z))  # -14


# create a function with a default parameter
def new_range(start=0, stop=10):
    x = start
    while x < stop:
        print(x)
        x += 1


new_range()  # 0123456789
new_range(5)  # 56789
new_range(stop=5)  # 01234


# return multiple values from function
def return_values(x, y):
    return x + 1, y + 1


result = return_values(1, 2)
print(result)  # (2, 3)
x, y = return_values(1, 2)
print(x, y)  # 2 3


# create a function that takes in two strings: a base string and a string that we use to remove characters from base string
def remove_chars(base, chars):
    new_string = base
    for char in chars:
        new_string = new_string.replace(char, "")
    return new_string


result = remove_chars("hello world", "l")
print(result)  # heo word


# create a function that uses another function to return the sums of two lists
def sum_lists(list1, list2):
    list1_sum = sum_list(list1)
    list2_sum = sum_list(list2)
    return list1_sum, list2_sum


def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


sum1, sum2 = sum_lists([1, 2, 3, 4], [-1, -2, -3, -4])
print(sum1, sum2)  # 10 -10


# create a nested function of the above two functions
def sum_lists2(list1, list2):
    def sum_list2(lst):
        total = 0

        for num in lst:
            total += num
        return total

    list1_sum = sum_list2(list1)
    list2_sum = sum_list2(list2)
    return list1_sum, list2_sum


sum1, sum2 = sum_lists([1, 2, 3, 4], [-1, -2, -3, -4])
print(sum1, sum2)  # 10 -10

'''
Write a function name "add" that takes in two parameters x and y, both expected to be numbers. Your function should add 
the two numbers and return the result.
'''
def add(x, y):
    return x + y

print(add(1, 2)) # 3

'''
Write a function "find_all_odds(lst), which takes in a list of integers and returns a new list containing all of the odd 
numbers of the original list, in the order in which they appear.
You can assume that lst will only contain integers.
'''
def find_all_odds(lst):
    new_list = []
    for num in lst:
        if num % 2 == 1:
            new_list.append(num)
    return new_list

print(find_all_odds([1, 2, 3, 4, 5, 6, 5, 5, 3, 2])) # [1, 3, 5, 5, 5, 3]

'''
Write a function "string_lengths(strings)", which takes in a list of strings and returns a new list containing the 
lengths of the strings, in their relevant order. You can asuume that "strings" will only contain strings.
'''
def string_lengths(strings):
    new_list = []
    for string in strings:
        new_list.append(len(string))
    return new_list

strings = ["hello", "this", "is", "a", "beard", "orange", "blue"]
lengths = string_lengths(strings)
print(lengths) # [5, 4, 2, 1, 5, 6, 4]

'''
Write a function name "compare_lists" that accepts two optional parameters, lst1 and lst2. The function should return 
the number of unique common elements between the two lists. If either of the lists isn't passed as a parameter, it 
should be treated as an empty list.

You can assume that the input lists will only contain integers.
'''
def compare_lists(lst1=[], lst2=[]):
    x = set(lst1)
    y = set(lst2)
    return len(x & y)

print(compare_lists([1, 2, 3], [1, 1, 1])) # 1

'''
Write a function "trim_list(lst, elements_to_trim)", which takes in a list and returns a new version of the input list 
where the last elements_to_trim elements have been removed. You can assume that elements_to_trim will always be a 
positive integer that's smaller than the length of lst.
'''
def trim_list(lst, elements_to_trim):
    return lst[:len(lst) - elements_to_trim]

print(trim_list([1, 3, 34, "hi", "yes", True, 2.3], 3)) # [1, 3, 34, 'hi']

'''
Write a function "running_sums(numbers)", which takes in a list of integers and returns a new list of the same length as 
numbers, where the element at index i in the new list is equal to numbers[0] + numbers[1] + ... + numbers[i - 1] + numbers[i].
You can assume that numbers will only contain integers.
'''
def running_sums(numbers):
    sums = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)
    return sums

sums = running_sums([5, 4, 2, 1, 5, 6, 4])
print(sums) # [5, 9, 11, 12, 17, 23, 27]