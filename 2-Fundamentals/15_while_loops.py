x = 0
while x < 5:
    x += 1
    print(x) # 12345

# have user input until an interger is entered
num = input("Enter an integer: ")
while not num.isdigit():
    num = input("Enter an integer: ")

# have user input until an interger is entered (alternative)
while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        break

# print numbers in a list then stop when the sum hits a particular number
lst = [2, 3, 3, 2, 2, 1]
result = 0
i = 0
while result < 9:
    num = lst[i]
    result += num
    i += 1
    print(num)

# determine if a number is in a list
lst = [2, 3, 3, -2, -2, -1]
i = 0
while i < len(lst):
    if lst[i] == -2:
        print("found it")
        break
    i += 1
else:
    print("didn't find it")

'''
Write a program that continually asks the user to enter a number until they enter the number 5, at which point the 
program should print how many numbers the user has entered. You may assume that the user will only enter a number.
'''

# solution 1
numbers = []
num = int(input("Enter a number: "))
while num != 5:
    num = int(input("Enter a number: "))
    numbers.append(num)
    if num == 5:
        numbers.append(num)
print(f"You entered {len(numbers)} numbers.")

# Solution 2
num_of_entries = 0
while True:
    number = int(input("Enter a number: "))
    num_of_entries += 1
    if number == 5:
        break
print(f"You entered {num_of_entries} numbers.")

'''
Write a program that continually asks the user to enter a word until they enter the word "q" or "quit", at which 
point the program should print the average length of all of the entered words, excluding the "q" or "quit". 

If the user doesn't enter any words (i.e., immediately enters "q" or "quit"), you program shouldn't print anything. 
'''

num_of_entries = 0
total_length = 0
while True:
    word = input("Enter a word: ")
    if word == "q" or word == "quit":
        break
    num_of_entries += 1
    total_length += len(word)

if num_of_entries > 0:
    print(total_length / num_of_entries)

'''
Use a while loop to print the squares of the numbers 1, 3, 6, 10, 15, and 21.
'''

lst = [1, 3, 6, 10, 15, 21]
i = 0
while i < len(lst):
    num = lst[i]
    print(num * num)
    i += 1