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

**Input**
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

**Condition**
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

