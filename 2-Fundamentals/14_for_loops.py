# print numbers from 0 to 9
for i in range(10):
    print(i) # 0123456789

# print numbers between 5 and 9
for i in range(5, 10):
    print(i) # 56789

# print numbers between 1 and 9 incrementing by 2
for i in range(1, 10, 2):
    print(i) # 13579

# print negative numbers counting backwards
for i in range(-1, -10, -2):
    print(i) # -1-3-5-7-9

# sum the numbers between 1 and 10
result = 0
for i in range(1, 11):
    result += i
print(result) # 55

# iterate through a list
list = [1, 2, 3, 4, 5, True, False]
for i in range(len(list)):
    print(list[i]) # 12345TrueFalse

# iterate through list by item
for element in list:
    print(element) # 12345TrueFalse

# iterate through a list with access to element and index
for i, element in enumerate(list):
    print(i, element)

'''
The above outputs to:
0 1
1 2
2 3
3 4
4 5
5 True
6 False
'''

# iterate through a tuple
tup = (2, 3, 4, "hello", "kelli", True)
for i in range(len(tup)):
    element = tup[i]
    print(element) # 234hellokelliTrue

# iterate through tuple with access to index and element
for i, element in enumerate(tup):
    print(i, element)


# iterate through tuple by item
for element in tup:
    print(element) # 234hellokelliTrue

# iterate through a string
s = "my string"
for i in range(len(s)):
    print(s[i]) # my string

# print the first 5 characters of a string
for i in range(5):
    print(s[i]) # my st

# print every other character of a string
for i in range(0, len(s), 2):
    print(s[i]) # m tig

# iterate through list and stop at a particular element
list = [1, 2, 3, 3, 4, 4, 2, 1, 2]
for num in list:
    if num == 4:
        break
    print(num) # 1233

# iterate through a list and skip a particular element
for num in list:
    if num == 4:
        continue
    print(num) # 1233212

# iterate through nested for loops
for i in range(5):
    for j in range(5):
        print(j) # 0123401234012340123401234

for i in range(3):
    for j in range(3):
        for w in range(2):
            print(i, j, w)

"""
Output for the above is:
0 0 0
0 0 1
0 1 0
0 1 1
0 2 0
0 2 1
1 0 0
1 0 1
1 1 0
1 1 1
1 2 0
1 2 1
2 0 0
2 0 1
2 1 0
2 1 1
2 2 0
2 2 1
"""

# using nested for loop with nested list
lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
for i in range(len(lst)):
    interior_lst = lst[i]
    for j in range(len(interior_lst)):
        print(interior_lst[j]) # 12345678

# for loop tells index of a particular character in a string
st = "hello world!"
for i, char in enumerate(st):
    if char == "w":
        print(i) # 6

# ask for input and put values in a list
numbers = []
for i in range(5):
    num = input("Enter a number: ")
    numbers.append(int(num))
print(numbers)

# add a placeholder in for loop that does nothing when run
for i in range(3):
    pass

# write a for loop that looks in tuple to see if a string exists
words = ("hello", "name", "this", "is", "word")
target = "name"
found = False
for word in words:
    if word == target:
        print("I found the word!")
        found = True
if not found:
    print("I didn't find the word!")

# write a for loop that looks in tuple to see if a string exists (alternative solution)
words = ("hello", "name", "this", "is", "word")
target = "kelli"
for word in words:
    if word == target:
        print("I found the word!")
        break
else:
    print("I didn't find the word!")

'''
Use a single for loop to iterate through two strings, and print all of their matching characters (i.e., the characters
that are at the same index and that are equal to each other) each on a separate line.
'''
string1 = "aabbcsdw"
string2 = "abbbcsdd"

for i in range(len(string1)):
    character1 = string1[i]
    character2 = string2[i]
    if character1 == character2:
        print(character1)

'''
Use a single for loop to iterate through the provided list, and print the elements that are both divisible by 2 and 
located at an odd index, each on a separate line.
'''
lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

for i, element in enumerate(lst):
    if element % 2 == 0 and i % 2 == 1:
        print(element)

'''
Use nested for loops to iterate through the provided list, which contains other lists, and print the respective sums of
the inner lists, each on a separate line.
'''
lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

for inner_list in lst:
    sum = 0
    for item in inner_list:
        sum += item
    print(sum)

'''
Use a single for loop to iterate through the provided list of numbers, and for each number, print the sum of the number
and the one directly to its right. In other words, print lst[i] + lst[i + 1]. Since the last number in the list has no 
number to the right of it, you should simply skip it.
'''
lst = [-2, 0, 4, 5, 1, 2]

for i in range(len(lst) - 1):
    current = lst[i]
    next = lst[i + 1]
    sum = current + next
    print(sum)