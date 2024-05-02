# import math module
import math

# import random module
import random

# absolute value
x = abs(-9)
print(x) # 9

# max function returns the biggest item
x = max(1, 2, 5)
print(x) # 5

x = max("a", "b")
print(x) # b

x = max((1, 2, 3))
print(x) # 3

# min function returns the smallest item

x = min([1, 2, -3])
print(x) # -3

# sum function returns the sum of iterable objects
x = sum([1, 2, 3])
print(x) # 6

# round function rounds a number to a given precision in decimal digits
x = round(3.45)
print(x) # 3

x = round(3.49453, 3)
print(x) # 3.495

# math.sin function returns the sine of a number (measured in radians)
x = math.sin(90)
print(x) # 0.8939966636005579

# math.cos function returns the cosine of a number (measured in radians)
x = math.cos(0)
print(x) # 1.0

# random.randint function returns random integer in range [a, b] including both numbers
random_number = random.randint(1, 10)
print(random_number)

# random.randrange function returns a random item from a range
random_range = random.randrange(1, 10, 2)
print(random_range)

# pick something random from a list
lst = ["hello", "hi", "ho", "he"]
random_string = random.choice(lst)
print(random_string)