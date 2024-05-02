# Introduction

To start using Python you need to download it, which you can do [here](https://www.python.org/)

## VSCode

VSCode stands for **Visual Studio Code** and is an application that can be used for development and programming purposes.
It is one of the most popular IDEs (integrated development environments) and is supported and maintained by Microsoft.
You can download it [here](https://code.visualstudio.com/download)

## Data Types
- **Int**
  - In Python, the **int** data type can represent all integers, positive or negative. `..., -2, -1, 0, 1, 2, ...` are all ints in Python.
- **Float**
  - In Python, the **float** data type represents floating point numbers, positive or negative.
  - `-2.1, 0.2, 7.0, -90.234, 0.222321, 3.14` are all floats in Python. Even numbers like `2.0` that are whole numbers are considered floats because of the presence of the decimal point (the period).
- **String**
  - The **str** data type represents a sequence of characters. In Python, they start and end with `"`, `'`, `"""`, or `'''`. The following are examples of valid Python strings, `"hello", "2.0", 'str', """False""", '''true'''`.
- **Bool**
  - In Python, the **bool** data type represents one of two values: `True` or `False`
- ***`type()` Function***
  - The `type()` function returns the type of the specified object

## Comments

**Comments** are parts of the code that usually get ignored by the compiler or interpreter, and that are solely meant to explain or document a section of the program for future maintainers.
- `# Single line comment`
- ```
  '''
  This is a 
  multiline
  comment 
  '''
  ```
  
- ```
  """
  This is a
  multiline 
  comment
  """
  ```
  
## Variables and Printing
**Variable**
- A **variable** can be thought of as a container that stores a value. As a programmer you can create your own variables that store different data types. The following is an example of a variable, `hello_world = "This variable holds a string"`
- In Python, variable names must:
  - Not start with a number.
  - Not contain any special characters other than underscores (_).
  - Not contain any spaces

**`print()` Function**

- The print() function prints the specified message to the screen, or other standard output device.
- The message can be a string, or any other object, the object will be converted into a string before written to the screen.

An example of variables and printing can be found in [4_variablesAndPrinting.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/4_variablesAndPrinting.py).

## Console Input

- The input function is built directly into Python as a means to gather user input from the command line. 
- An important note is that it will always return a `str` object which will need to be converted to an `int` (for example) if you expect the user input to be an integer. 

```
user_name = input("What is your name? ")
print("Hello", user_name + "!")
```

An example of console input can be found at [5_console_input.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/5_console_input.py).

## Arithmetic Operators

**Operator**
- An **operator** is a symbol that indicates an operation to be performed. `+, -, /, *, **, //` are all operators.

**Operand**
- An **operand** is an object that an operator acts on. In the expression `2 + 3`, both `2` and `3` are operands while `+` is the operator. 

**Integer Division**
- **Integer Division** is division in which the fractional part (remainder) is discarded. In Python, integer division is performed by using the `//` operator. For example, the expression `11 // 3` evaluates to `3`.

**Modulus**
- The **modulus** (or modulo) is the remainder after dividing one number by another. In Python, modulus is performed by using the `%` operator. For example, the experession `10 % 3` evaluates to `1`.

**Concatenation**
- In Python, **concatenation** is the process of combining or adding strings together. Concatenation can be performed using the `+` operator. For example, the expression `"1" + "word"` evaluates to `"1word"`.

An example of arithmetic operators can be found in [6_arithmetic_operators.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/6_arithmetic_operators.py).

## Type Conversions

- The act of changing an object’s data type is known as **type conversion**. 
- The Python interpreter automatically performs Implicit Type Conversion. 
  - Python prevents Implicit Type Conversion from losing data.
- The user converts the data types of objects using specified functions in explicit type conversion, sometimes referred to as type casting. 
  - When type casting, data loss could happen if the object is forced to conform to a particular data type.

**Implicit Type Conversion**
```
x = 10

print("x is of type:",type(x))

y = 10.6
print("y is of type:",type(y))

z = x + y

print(z)
print("z is of type:",type(z))

```

Output:
```
x is of type: <class 'int'>
y is of type: <class 'float'>
20.6
z is of type: <class 'float'>
```

**Explicit Type Conversion**

```
# initializing string
s = "10010"

# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)

# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)
```

Output:

```
After converting to integer base 2 : 18
After converting to float : 10010.0
```

## Conditions

- A **condition** is any expression that evaluates to `True` or `False`. 
- The expression `2 == 2` evaluates to `True` and is considered a condition.

Python supports the usual logical conditions from mathematics:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

**ASCII**
- **ASCII** is the abbreviation for **American Standard Code for Information Interchange**.
- This code provides a standard character set for computers where each character on the keyboard is represented by a unique integer.
  - In Python, you can determine the ASCII code for a character by using the `ord()` function and determine the character represented by an integer with the `chr()` function. 
    - For example, `ord('a')` returns `97` and `chr(97)` returns `'a'`.


## Compound Conditions

**And / Or / Not**

- When you want to create larger conditions based on multiple smaller conditions, you will need to use the `and`, `or`, `not` keywords. Conditions that contain these keywords are called **compound conditions**

```
if x == 1 and y == 2:
  print("x is equal to 1 and y is equal to 2")
elif not (x == 2 or y == 2):
  print("neither x and y are equal to 2"
```

**De Morgan's Laws**
- **De Morgan's laws** state:
  - `not (x and y) == not x or not y`
  - `not (x or y) == not x and not y`
- You can use these laws to simplify complex conditions

**ORDER OF OPERATIONS**
1. parentheses
2. conditional/comparison operators
3. not
4. and 
5. or

## Conditionals

**if / elif / else**
- When you want to conditionally run a part of your program (depending on the value of a variable, for example) `if`, `elif`, and `else` statements are necessary:

```
if x == 1:
  print("If x is equal to 1, then this will be printed!")
elif x == 2
  print("If x is equal to 2, then this will be printed!")
else:
  print("If x isn't equal to 1 or 2, then this will be printed!")
```

## Lists

- In Python, a **list** is a data type that stores an ordered collection of elements.
- You can access individual elements in a list using their indices and add elements to a list by using the `.append(item)` method

Example:
```
lst = [1, 10, 4, True, "str"]
lst.append(2) # lst is now equal to [1, 10, 4, True, "str", 2]
print(lst[1]) # this outputs to 10
print(lst[-1] # this outputs to 2
```

**in**

- The `in` keyword in Python lets you check whether a value is contained in a collection (such as a `list`, `set`, `dict`. etc).

```
print("hello" in ["hello", "world"]) # True
```

- The `in` keyword can also be used to iterate of the items in a collection when using a `for` loop.

Examples of what you can do with lists are found in [11_lists.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/11_lists.py).


## Strings

**String**
- The **str** data type represents a sequence of characters. 
- In Python, they start and end with `"`, `'`, `"""`, `'''`.
- The following are examples of valid Python strings, `"hello", "2.0", 'str', """False""", '''true'''`.

**New Line Character - \n**
- The **new line character** is a `\n`.
- This character is invisible when printed but tells the computer to move the cursor to the next line. For example, `print("hello\nworld\n!")` outputs the following:

```
hello
world
!
```

Examples of what you can do with strings can be found in [12_strings.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/12_strings.py).

## Tuples

- A **tuple** is similar to a list in that it stores a collection of elements. 
- Like lists, you can access individual elements in a tuple using their indices, but you cannot modify or change these elements. 

Example:

```
tup = (1, 10, 4, True, "str")
print(tup[1]) # this outputs to 10
print(tup[-1]) # this outputs to "str"
tup[1] = 0 # this raises an exception
tup.append(1) # this raises an exception
```

Examples of what you can do with tuples can be found in [13_tuples.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/13_tuples.py).

## For Loops

**Range**
- The `range(start, stop, step)` function in Python creates an iterator that returns integers one by one from `start` (inclusive) to `stop` (exclusive), incrementing the last value by `step` every time.
- The `range` function is commonly used with `for` loops like so:

```
for i in range(1, 11, 2):
    print(i)
# this loop will output the following:
# 1
# 3
# 5
# 7
# 9
```

Examples of what you can do with for loops are found in [14_for_loops.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/14_for_loops.py).

## While Loops

With the `while` loop we can execute a set of statements as long as a condition is true.

Examples of what you can do with while loops are found in [15_while_loops.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/15_while_loops.py).

## Slices

Slicing is the process of accessing a sub-sequence of a sequence by specifying a starting and ending index. In Python, you perform slicing using the colon : operator. The syntax for slicing is as follows:

`sequence[start_index:end_index]`

For example:

```
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[1:3]) # output: ['banana', 'cherry']
```

The slice operator returns a new object that contains the result of the slice. It does not modify the existing object.

A slice can be used on a list, tuple, string, and typically any data type that stores a collection of items.

Examples of what you can do with slices can be found at [16_slices.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/16_slices.py).

## Dictionary

In Python, a **dictionary** (or **dict**) is a collection that associates immutable keys with values of any type. For example, the following code creates and accesses a dictionary that stores the age of each person according to their names:

```
ages = {
    "Kelli": 27,
    "Kimi": 30,
    "Camille": 7,
}
print("Kimi is", ages["Kimi"], "years old"
```

A dictionary is a good choice when you care about how many times items occur in a collection or if they exist in it at all. This is because determining if an item exists in a dict is much faster than doing so in a list, and you can map an item to its frequency in a dict.

If you're concerned with the order in which items are added to a collection and would like to modify these items, you should use a list. A dictionary doesn't maintain the order in which items are added to it, but a list does. A tuple also maintains the order of items but it's items cannot be modified. 

Examples of what you can do with dictionaries can be found in [17_dictionaries.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/17_dictionaries.py).

## Sets

Sets are collections of unique objects. In Python, you can create a new set with `my_set = set()`, add to it with `my_set.add(item)`, and remove items from it with `my_set.remove(item)`.

One important note about sets is that they are not ordered, so iterating through a set is not guaranteed to give you the same result every time.

If you only care if something exists, use a set.

## Exceptions

An **exception**, in Python, is **raised** when something unexpected happens during the execution of your program. For instance, if you try to convert the string `"hello"` into an **integer**, your program will raise a `ValueError`.

If you anticipate that a part of your code might, in some cases, raise an exception, you can surround that part of the code with a `try/except` block and prevent your program from completely crashing.

```
try:
    i = int("hello")
except Exception as e:
    print(f"Caught the exception: {e}")
```

A `try` block without an `except` or `finally` block is pretty useless, so an `except` or `finally` is indeed required.

You can have as many `except` blocks as you want, and you can do whatever you want in them.

However, you can only have one `finally` block, and it's not required if you have at least one `except` before it.

Python is an interpreted language, which means that all exceptions other than syntax errors occur at run-time, while the program is being executed.

For example, if you try executing `[0, 1, 2][3]` in Python, the code will indeed be executed, and the resulting `IndexError` will be raised at run-time.

If syntax errors are present, however, the interpreter will catch them before executing the program and inform you that it can't understand the code that you've written.

For example, if you try executing `[]]` in Python, the code won't be executed, and a `SyntaxError` will instead be raised.

Examples of what you can do with exceptions can be found in [19_exceptions.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/19_exceptions.py).

## Functions

**Argument & Parameter**

The terms **argument** and **parameter** are frequently used interchangeably. However, strictly speaking, **arguments** are values that are passed into a function, while **parameters** are values that are read by that function.

Examples of what you can do with functions can be found in [20_functions.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/20_functions.py).

## Mutability

**Immutable**

In Python, an **immutable** object is one that cannot be modified once created. The following are examples of immutable data types:
- `int`
- `float`
- `str`
- `bool`
- `tuple`

**Mutable**

In Python, a **mutable** object is one that can be modified once created. The following are examples of mutable data types:
- `list`
- `set`
- `dict`

Examples on mutability are found in [21_mutability.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/21_mutability.py).