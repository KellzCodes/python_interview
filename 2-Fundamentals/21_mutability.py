# "is" keyword tells you if two objects are the same

# "is" keyword on mutable objects
x = []
y = []
print(x is y) # False

'''
whenever you have two variables pointing to the same object, and that object is mutable, 
anything you do on one of those variables is going to affect the other.
'''
x = []
y = x
x.append(1)
print(x is y) # True

# is keyword on immutable objects
a = 1
b = a
print(a is b) # True

'''
whenever you have two variables pointing to the same object, and that object is immutable,
whatever you do on one of those variables is not going to affect the other
'''
a += 1
print(a is b) # False

# "id" keyword points to a variable's address in RAM
a = 1
b = 2
print(id(a), id(b)) # 140704048691640 140704048691672

# pass a list to a function and modify the list outside of the function
def func(lst, x):
    lst.append(x)
    print(lst)

a = []
func(a, 2) # [2]
print(a) # [2]

# create two dictionary objects by making one equal to the other
d = {}
d["k"] = "v"
a = d
a["a"] = "b"
print(d, a) # {'k': 'v', 'a': 'b'} {'k': 'v', 'a': 'b'}
print(d is a) # True

# create two set objects by making one equal to the other
s1 = set()
s2 = s1
s1.add(1)
s2.add(2)
print(s1 is s2) # True

# make a copy of a list without the copy being able to change the original list
a = [1, 2, 3]
b = a[:]
a.append(4)
print(a is b) # False

# make a copy of a set without the copy being able to change the original set
s1 = {1, 2, 3}
s2 = s1.copy()
s1.add(4)
print(s1, s2) # {1, 2, 3, 4} {1, 2, 3}

# make a copy of a dictionary without the copy being able to change the original dictionary
s1 = {"k": "v"}
s2 = s1.copy()
s1[1] = 2
print(s1, s2) # {'k': 'v', 1: 2} {'k': 'v'}

# change a nested list
lst = [[1, 2, 3], [3, 4, 5]]
lst[0].append(4)
lst[1].append(4)
print(lst) # [[1, 2, 3, 4], [3, 4, 5, 4]]

# change a list while it is inside a dictionary
lst = [1, 2, 3]
d = {1: lst}
lst.append(4)
print(d) # {1: [1, 2, 3, 4]}

# change a mutable object while it is inside a dictionary
x = 2
d = {1: x}
x = 3
print(d) # {1: 2}

# store a mutable data type inside an immutable data type
a = [1, 2]
b = [3, 4]
tup = (a, b)
a.append(1)
print(tup) # ([1, 2, 1], [3, 4])

# make a shallow copy of a nested mutable data type storing mutable data type
'''
The slice makes a copy of the outer list but not the nested list. a, b, and c are referencing the same nested list
'''
a = [[1, 2, 3]]
b = a[:]
c = a[0]
c.append(4)
print(a, b) # [[1, 2, 3, 4]] [[1, 2, 3, 4]]
print(a is b) # False
a.append(1)
print(a, b) # [[1, 2, 3, 4], 1] [[1, 2, 3, 4]]

'''
Write a function named "replace" that takes in three parameters: "lst" (a list of strings), "target" (a string), 
and "swap_value" (another string).

Your function should replace all instances of "target" in "lst" with "swap_value", and it shouldn't return anything;
in other words, your function should mutate the input list.
'''
def replace(lst, target, swap_value):
    for i, word in enumerate(lst):
        if word == target:
            lst[i] = swap_value

lst = ["kelli", "is", "great", "is", "is", "yes", "no", "blue", "no"]
replace(lst, "is", "the")
print(lst) # ['kelli', 'the', 'great', 'the', 'the', 'yes', 'no', 'blue', 'no']