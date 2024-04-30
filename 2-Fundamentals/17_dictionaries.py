# print a value in a dictionary
x = {2: "hello", "1": 5}
print(x[2]) # hello

# Add values into a dictionary
x = {}
x["key"] = "value"
print(x) # {'key': 'value'}

# Add values into a dictionary (alternative)
x = dict()
x["key"] = "value"
print(x) # {'key': 'value'}

# Delete items from dictionary
x = {1: 1, 2: 2, 3: 3}
del x[1]
print(x) # {2: 2, 3: 3}

# Check to see if a key is in a dictionary
x = {1: 1, 2: 2, 3: 3}
contains = 1 in x
print(contains) # True

# print all the values in a dictionary
x = {1: 1, 2: 2, 3: 3}
values = x.values()
print(values) # dict_values([1, 2, 3])

# print the first value in a dictionary
x = {1: 1, 2: 2, 3: 3}
values = list(x.values())
print(values[0]) # 1

# print all the keys in a dictionary
x = {1: 1, 2: 2, 3: 3}
keys = x.keys()
print(keys) # dict_keys([1, 2, 3])

# print the first key in a dictionary
x = {1: 1, 2: 2, 3: 3}
keys = list(x.keys())
print(keys[0]) # 1

# print all the items in a dictionary
x = {1: 1, 2: 2, 3: 3}
items = x.items()
print(items) # dict_items([(1, 1), (2, 2), (3, 3)])

# print the first item a dictionary
x = {1: 1, 2: 2, 3: 3}
items = list(x.items())
print(items[0]) # (1, 1)

# print the length of a dictionary
x = {1: 1, 2: 2, 3: 3}
print(len(x)) # 3

# iterate through a dictionary using a for loop
x = {1: 1, 2: 2, 3: 3}
for key in x:
    value = x[key]
    print(key, value)
'''
Output for the above:
1 1
2 2
3 3
'''

# iterate through dictionary using for loop with access to both key and value
x = {1: 1, 2: 2, 3: 3}
for key, value in x.items():
    print(key, value)
'''
Output for the above:
1 1
2 2
3 3
'''

# get value of key and add 1 to it, but if the key does not exist, add it
x = {1: 1, 2: 2, 3: 3}
x[4] = x.get(4, 0) + 1
print(x) # {1: 1, 2: 2, 3: 3, 4: 1}

# get value of key and add 1 to it
x = {1: 1, 2: 2, 3: 3, 4: 1}
x[4] = x.get(4, 0) + 1
print(x) # {1: 1, 2: 2, 3: 3, 4: 2}

# loop through string and create a dictionary that contains the frequency of characters in the string
characters = {}
string = "hello world"
for char in string:
    characters[char] = characters.get(char, 0) + 1
print(characters) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# ask the user to enter a some values and count how many times they enter the values
counts = {}
while True:
    num = input("Number (enter q to quit): ")
    if num == "q":
        break
    num = int(num)
    counts[num] = counts.get(num, 0) + 1
print(counts)

'''
Write a program that asks the user to enter a string and prints the string's characters and their frequencies in any 
order and in the following format:

Enter a string: helloworld
h: 1
e: 1
l: 3
o: 2
w: 1
r: 1
d: 1
'''
counts = {}
string = input("Enter a string: ")
for char in string:
    counts[char] = counts.get(char, 0) + 1

for key, value in counts.items():
    print(f"{key}: {value}")