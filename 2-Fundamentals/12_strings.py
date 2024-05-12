import re

s = "hello"

# print the character at the first index of the string
print(s[0]) # h

# print the length of the string
print(len(s)) # 5

# print how many of a certain character is in the string
print(s.count("l")) # 2

# print the first index of a certain character in the string
print(s.find("l")) # 2

# turn string into upper case
print(s.upper()) # HELLO

# turn string into lower case
t = "hElLo"
lower = t.lower()
print(lower) # hello

# capitalize the first letter in the string
a = "python"
print(a.capitalize()) # Python

# check to see if a string has a certain character
b = "fundamentals"
contains = "a" in b
print(contains) # True

# check to see if a string is a digit or not
c = "19"
is_digit = c.isdigit()
print(is_digit) # True
d = "19.4"
is_digit = d.isdigit()
print(is_digit) # False because 19.4 is a float

# Split a string into a list where each word is a list item
e = "hello my name is kelli"
words = e.split()
print(words) # ['hello', 'my', 'name', 'is', 'kelli']
f = "this, is, a, fun, time"
words = f.split(",")
print(words) # ['this', ' is', ' a', ' fun', ' time']

# replace all of certain character with a different character
g = "hello, my, name, is, kelli"
g2 = g.replace(",", "|")
print(g2)

# F strings
name = "Kelli"
h = f"Hello {name}!"
print(h) # Hello Kelli!
print(f"My dog is {10} years old") # My dog is 10 years old

# String multiplication
name = "davis"
print(name * 5) # davisdavisdavisdavisdavis

# Multiline String
string = '''hello my name is kelli 
and this is a multiline string
!'''
print(string)

# escape characters
name = "KDavis"
string = f"\"{name}\""
print(string) # "KDavis"

# convert a list into a string
list = ["k", "e", "l", "l", "i"]
string = "".join(list)
print(string) # kelli
string2 = ",".join(list)
print(string2) # k,e,l,l,i

# use the search() function to find patterns within a string
s1 = "Michael Jackson is the best!"
pattern = r"Jackson"
result = re.search(pattern, s1) # you have to import re to use search() function
if result:
    print("Match Found!")
else:
    print("Match not Found!")

# A simple example using the \d special sequence in a regular expression
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any 10 consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
else:
    print("No Match")

# A simple example using the \W special sequence in a regular expression pattern
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)  # findall() finds all occurrences of a specified pattern
print("Matches:", matches)  # Matches: [',', ' ', '!']

# use the findall() function to find all occurrences of "as" in a string
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
result = re.findall("as", s2)
print(result)  # ['as', 'as']

# regular expression's split() function splits a string into an array of substrings based on pattern
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
split_array = re.split("\s", s2)  # \s matches any whitespace character (space, tab, newline, etc.)
print(split_array)  # ['Michael', 'Jackson', 'was', 'a', 'singer', 'and', 'known', 'as', 'the', "'King", 'of', "Pop'"]

'''
the sub function of a regular expression is used to replace all occurrences of a pattern 
in a string with a specified replacement
'''
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
pattern = r"King of Pop"
replacement = "legend"
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
print(new_string)  # Michael Jackson was a singer and known as the 'legend'

# find the first index of the sub-string "snow"
g = """Mary had a little lamb, little lamb, Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went the lamb was sure to go
"""
print(g.find("snow"))

# split a string into a list
string = "I love coding in Python"
print(string.split())  # ['I', 'love', 'coding', 'in', 'Python']

# find whether a digit is present in a string using the \d and search() function
s3 = "House number- 1105"
result = re.search(r"\d", s3)
if result:
    print("Digit found:", result.group())
else:
    print("No Digit")

