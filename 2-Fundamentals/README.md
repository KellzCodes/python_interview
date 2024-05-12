# Fundamentals

To start using Python you need to download it, which you can do [here](https://www.python.org/).

### Contents
- [Data Types](#data-types)
- [Comments](#comments)
- [Variables and Printing](#variables-and-printing)
- [Console Input](#console-input)
- [Arithmetic Operators](#arithmetic-operators)
- [Type Conversions](#type-conversions)
- [Conditions](#conditions)
- [Compound Conditions](#compound-conditions)
- [Conditionals](#conditionals)
- [Lists](#lists)
- [Strings](#strings)
- [Tuples](#tuples)
- [For Loops](#for-loops)
- [While Loops](#while-loops)
- [Slices](#slices)
- [Dictionary](#dictionary)
- [Sets](#sets)
- [Exceptions](#exceptions)
- [Functions](#functions)
- [Mutability](#mutability)
- [Scope](#scope)
- [Math](#math)
- [Sorting](#sorting)
- [Misc. Python Syntax](#misc-python-syntax)
- [Programming Fundamentals Assessments](#programming-fundamentals-assessments)

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

**Python String Module**

The **string module** is a built in module which has to be imported before using any of its contants and classes

Here are some constants defined in the string module:
```
import string

# string module constants
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)
print(string.punctuation)
```

Output:

```
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefABCDEF
 	

!"#$%&'()*+,-./:;?@[\]^_`{|}~
```

**RegEx**

In Python, RegEx is a tool for matching and handling strings.

Python provides a built-in module called `re`, which allows you to work with regular expressions. 

Regular expressions (RegEx) are patterns used to match and manipulate strings of text. THere are several special sequences in RegEx that can be used to match specific characters or patterns.

| Special Sequence | Meaning                                              | Example                                          |
|------------------|------------------------------------------------------|--------------------------------------------------|
| `\d`             | Matches any digit character (0-9)                    | `"123"` matches `"\d\d\d"`                       |
| `\D`             | Matches any non-digit character                      | `"hello"` matches `"\D\D\D\D\D"`                 |
| `\w`             | Matches any word character (a-z, A-Z, 0-9, and _)    | `"hello_world"` matches `"\w\w\w\w\w\w\w\w\w\w\w"`|
| `\W`             | Matches any non-word character                       | `"@#$%"` matches `"\W\W\W\W"`                    |
| `\s`             | Matches any whitespace character (space, tab, newline, etc.) | `"hello world"` matches `"\w\w\w\w\w\s\w\w\w\w\w"` |
| `\S`             | Matches any non-whitespace character                 | `"hello_world"` matches `"\S\S\S\S\S\S\S\S\S\S\S"`|
| `\b`             | Matches the boundary between a word character and a non-word character | `"cat"` matches `"\bcat\b"` in "The cat sat on the mat" |
| `\B`             | Matches any position that is not a word boundary     | `"cat"` matches `"\Bcat\B"` in "category" but not in "The cat sat on the mat" |


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

## Scope

A variable is only available from inside the region it is created. This is called **scope**.

**Local Scope**

A variable created inside a function belongs to the *local* scope of that function, and can only be used inside that function.

```
def myfunc():
  x = 300
  print(x)

myfunc() # this outputs to 300
```

**Function Inside Function**

As explained in the example above, the variable `x` is not available outside the function, but it is available for any function inside the function:

```
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() # this outputs to 300
```

**Global Scope**

A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

```
x = 300

def myfunc():
  print(x)

myfunc() # this outputs to 300

print(x) # this outputs to 300
```

**Naming Variables**

If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function).

The function will print the local x, and then the code will print the global x: 
```
x = 300

def myfunc():
  x = 200
  print(x) 

myfunc() # this outputs to 200

print(x) # this outputs to 300
```

**Block Scope**

In **block scope**, variables are only available within the blocks where they are declared, including any other blocks nested within that block. Also, variables can only be accessed by code executed after the variable is initially declared or given a value.

```
# Global block
x = int(input("Enter a number: "))
if x > 5:
    # block A
    y = int(input("Enter a number: "))
    if y > 10: 
        # block B
        z = 10
    else:
        # block C
        z = 5
elif x < 0:
    # block D
    a = -5
else:
    # block E
    b = 0
print("?")
```

**Global Keyword**

If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.

The `global` keyword makes the variable global.

```
def myfunc():
  global x
  x = 300

myfunc()

print(x) # this ouputs to 300
```

Also, use the `global` keyword if you want to make a change to a global variable inside a function.

```
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x) # this outputs to 200
```

The `global` keyword is typically considered bad practice and should be avoided. 

The reason for this is that the `global` keyword adds side-effects to a function and makes it dependent on something referenced outside the function scope. This means changes to the globally referenced object can change the behaviour of the function and be difficult to detect, especially if a bug or issue arises. 

In summary, the `global` keyword often introduces unnecessary complexity and can almost always be avoided.

**Nonlocal Keyword**

The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.

```
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) # this outputs to hello
```

## Math

**Standard Library**

The **standard library** of a language are the libraries that the language comes with by default. In Python, this includes modules like `os`, `math`, `threading`, and so many more. 

**math Module**

The **math** module is part of the Python **standard library**, and gives you many nice functions that you may need to use in real world programs. For instance, `math.sin(x)`, `math.cos(x)`, `math.tan(x)`, and `math.pi` are available from the `math` module.

**random Module**

The **random** module is part of the Python **standard library**, and provides many functions that you can use to generate random numbers or make random choices. `random.randint(start,stop)`, `random.randrange(start, stop, step)`, and `random.choice(iterable)` are a few commonly used functions from the `random` module.

Examples of what you can do with math and random can be found in [23_math.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/23_math.py).

## Sorting

Python lists have a built-in `.sort()` method that modifies the list in-place. There is also a `sorted()` built-in function that builds a new sorted list from an iterable.

Examples of what you can do with sorting can be found in [24_sorting.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/24_sorting.py).

## Misc. Python Syntax

Examples of miscellaneous Python syntax can be found in [25_misc_syntax.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/25_misc_syntax.py).

## Programming Fundamentals Assessments

### Random Number Guesser
Write a program that asks the user to enter two integers representing the start and end of a range. The program should then generate a random number within this range (inclusively) and ask the user to guess numbers until they guess the randomly generated number. Once the user guesses the random number, the program should tell them how many attempts it took them to guess it.

Your program needs to ensure that the range of numbers given is valid. For example, if the user enters a number for the end of the range that is less than the start of the range, your program needs to ask them to enter a valid number. Your program must also handle any other errors that might occur, like the user entering a string instead of an integer.

Note: You may assume the start of the range will never be negative (i.e. you don't need to handle negative values).

Your program must use the same prompts and outputs as shown in the sample output below:

**Sample Output 1**
```
Enter the start of the range: 1
Enter the end of the range: 5
Guess a number: 2
Guess a number: 3
You guessed the number in 2 attempts
```

**Sample Output 2**
```
Enter the start of the range: 5
Enter the end of the range: 4
Please enter a valid number.
Enter the end of the range: 7
Guess a number: 6
You guessed the number in 1 attempt
```

**Sample Output 3**
```
Enter the start of the range: hello
Please enter a valid number.
Enter the start of the range: 8
Enter the end of the range: 4
Please enter a valid number.
Enter the end of the range: 20
Guess a number: 6
Guess a number: 7
Guess a number: hello
Please enter a valid number.
Guess a number: 9
You guessed the number in 3 attempts
```

Solution 1 can be found in [random_number_guesser_1.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/random_number_guesser_1.py).

Solution 2 can be found in [random_number_guesser_2.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/random_number_guesser_2.py).

### Caesar Cypher

Write a function that accepts a string and returns the caesar cipher encoding of that string according to a secondary input parameter named `offset`.

The caesar cipher encoding of a string involves shifting each character in the string a set number of positions previous in the alphabet. For example, if you were performing a caesar cipher of the string `"kelli"` with `offset = 2`, you would get `icjjg`. `"k"` is shifted to positions to `"i"`, `"e"` is shifted two positions to `"c"`, `"l"` is shifted two positions to `"j"`, `"i"` is shifted two positions to `"g"`.

In the situation where the shift of a character results in it being a position before `"a"`, the positions wrap and the next character should be `"z"`. For example, the caesar cipher of `"ab"` with `offset = 2` would be `"yz"`.

`offset` will always be a positive integer that is no greater than `26` and the input string will only contain lowercase letters.

**Sample Input #1**
```
string = "hello"
offset = 3
```

**Sample Output #1**
```
"ebiil"
```

**Sample Input #2**
```
string = "apple"
offset = 5
```

**Sample Output #2**
```
"vkkgz"
```

Solution 1 can be found in [caesar_cypher_1.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/caesar_cypher_1.py).

Solution 2 can be found in [caesar_cypher_2.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/caesar_cypher_2.py).

### Sort Employees

Write a function that accepts a list of lists that contain the name, age, and salary of specific employees and also accepts a string representing the key to sort employees by. Your function should return a new list that contains the lists representing each employee sorted in ascending order by the given key.

The string parameter named `sort_by` will always be equal to one of the following values: `"name"`, `"age"`, or `"salary"`.

See the sample input and output below for a detailed example.

**Sample Input #1**
```
employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_by = "age"
```

**Sample Output #1**
```
[
  ['Sarah', 24, 75000], 
  ['Connor', 25, 110000], 
  ['Jason', 26, 55000], 
  ['Josie', 29, 100000], 
  ['John', 33, 65000]
]
```

**Sample Input #2**
```
employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_by = "salary"
```

**Sample Output #2**
```
[
  ['Jason', 26, 55000], 
  ['John', 33, 65000], 
  ['Sarah', 24, 75000], 
  ['Josie', 29, 100000], 
  ['Connor', 25, 110000]
]
```

**Sample Input #3**
```
employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_by = "name"
```

**Sample Output #3**
```
[
  ['Connor', 25, 110000], 
  ['Jason', 26, 55000], 
  ['John', 33, 65000], 
  ['Josie', 29, 100000], 
  ['Sarah', 24, 75000]
]
```

Solution 1 can be found in [sort_employees_1.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/sort_employees_1.py).

Solution 2 can be found in [sort_employees_2.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/sort_employees_2.py).

Solution 3 is an advanced solution not covered yet. It can be found in [sort_employees_3.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/sort_employees_3.py).

### Longest Unique Words

Write a function that accepts a list of strings that represent words and a positive integer `n`, representing the number of words to return. Your function should return a new list containing the `n` longest unique words from the input list. Words are unique if they only appear one time in the input list.

There will always be exactly `n` words to return and you may return the words in any order.

Note: all strings in the input list will not contain any special characters or spaces.

See the sample input and output below for a detailed example.

**Sample Input #1**
```
[
  "Longer",
  "Whatever",
  "Longer",
  "Ball",
  "Rock",
  "Rocky",
  "Rocky"
]
```

**Sample Output #1
```
[
  "Whatever",
  "Ball",
  "Rock"
]
```

Solution 1 can be found in [longest_unique_words_1.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/longest_unique_words_1.py).

Solution 2 can be found in [longest_unique_words_2.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/longest_unique_words_2.py).

Solution 3 can be found in [longest_unique_words_3.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/longest_unique_words_3.py).

### Pairs Sum To Target

Write a function that accepts two lists(`list1` and `list2`) of integers and a target integer named `target`. Your function should return all pairs of indices in the form `[x, y]` where `list1[x] + list2[y] == target`. In other words, return the pairs of indices where the sum of their values equals `target`.

`list1` and `list2` will always have the same number of elements and you may return the pairs in any order.

**Sample Input #1**
```
list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5
```

**Sample Output #1**
```
[
  [0, 0], # list1[0] = 1, list2[0] = 4, 1 + 4 = 5
  [3, 4], # list1[3] = 5, list2[4] = 0, 5 + 0 = 5
  [4, 2], # list1[4] = 9, list2[2] = -4, 9 + -4 = 5
  [4, 3], # list1[4] = 9, list2[3] = -4, 9 + -4 = 5
]
```

Solution 1 can be found in [pairs_sum_to_target_1.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/pairs_sum_to_target_1.py).

Solution 2 can be found in [pairs_sum_to_target_2.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/pairs_sum_to_target_2.py).

### Create Strings From Characters

Write a function that accepts a dictionary called `frequencies` and two strings named `string1` and `string2`. The `frequencies` dictionary contains character keys and integer values, the value associated with each character represents its frequency. Your function should return `0`, `1`, or `2` according to the cases below.
- Your function should return `2` if the frequency of characters in the dictionary is sufficient to create both `string1` and `string2` without reusing any characters.
- Your function should return `1` if the frequency of characters in the dictionary is sufficient to create either `string1` or `string2` without reusing any characters.
- Your function should return `0` if the frequency of characters in the dictionary is **not** sufficient to create either `string1` or `string2` without reusing any characters.

**Sample Input #1**
```
frequencies = {
    "h": 2,
    "e": 1,
    "l": 1,
    "r": 4,
    "a": 3,
    "o": 2, 
    "d": 2,
    "w": 1
}
string1 = "hello"
string2 = "world"
```

**Sample Output #1**
```
1 # the string "world" can be created but "hello" cannot be.
```

**Sample Input #2**
```
frequencies = {
    "h": 2,
    "e": 1,
    "l": 2,
    "r": 4,
    "a": 3,
    "o": 2, 
    "d": 1,
    "w": 1
}
string1 = "hello"
string2 = "world"
```

**Sample Output #2**
```
1 # The string "world" and "hello" can be created but they cannot both be created without resusing any characters.
  # This is because there is not enough "l"'s.
```

The solution can be found in [create_strings_from_characters.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/create_strings_from_characters.py).