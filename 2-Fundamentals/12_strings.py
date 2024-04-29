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