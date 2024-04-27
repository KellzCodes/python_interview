# Introduction

To start using Python you need to download it, which you can do [here](https://www.python.org/)

### VSCode

VSCode stands for **Visual Studio Code** and is an application that can be used for development and programming purposes.
It is one of the most popular IDEs (integrated development environments) and is supported and maintained by Microsoft.
You can download it [here](https://code.visualstudio.com/download)

### Data Types
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

### Comments

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
  
### Variables and Printing
**Variable**
- A **variable** cam be thought of as a container that stores a value. As a programmer you can create your own variables that store different data types. The following is an example of a variable, `hello_world = "This variable holds a string"`
- In Python, variable names must:
  - Not start with a number.
  - Not contain any special characters other than underscores (_).
  - Not contain any spaces

**`print()` Function**

- The print() function prints the specified message to the screen, or other standard output device.
- The message can be a string, or any other object, the object will be converted into a string before written to the screen.

An example of variables and printing can be found in [4_variablesAndPrinting.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/4_variablesAndPrinting.py).

### Console Input

**Input**
- The input function is built directly into Python as a means to gather user input from the command line. 
- An important note is that it will always return a `str` object which will need to be converted to an `int` (for example) if you expect the user input to be an integer. 

```
user_name = input("What is your name? ")
print("Hello", user_name + "!")
```

An example of console input can be found at [5_console_input.py](https://github.com/KellzCodes/python_interview/blob/main/2-Fundamentals/5_console_input.py).
