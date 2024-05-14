# Advanced Programming

## Modules and Packages

### Main Module

In Python, the `main` module is the one that is invoked or run directly. Python will automatically set the `__name__` variable of that module to the string `"__main__"`. All modules that are imported from that main package will have their own values for the `__name__` variable.

When writing your modules in Python, it is best practice to run some parts of the code conditionally based on that `__name__` variable:

```
if __name__ == "__main__":
    print("This code will only run if this is the main package!")
```

### Module
In Python, a module is simply any Python file (something ending in `.py`). Modules provide a way to split code into multiple files and make programs easier to understand. One Python module is able to import code from another Python module.

### Package
A Python package is simply a directory that contains a special file named `__init__.py`, and typically a collection of other Python modules. Packages provide a way to organize Python modules. When importing a Python package the code inside of the `__init__.py` file will run once.

## Files

File handling in Python is a powerful and versatile tool that can be used to perform a wide range of operations.

### Python File Open

Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function `open()` but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

```
f = open(filename, mode)
```

Where the following mode is supported:
- r: open an existing file for a read operation.
- w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
- a:  open an existing file for append operation. It won’t override existing data.
- r+:  To read and write data into the file. The previous data in the file will be overridden.
- w+: To write and read data. It will override existing data.
- a+: To append and read data from the file. It won’t override existing data.

Examples of what you can do with files can be found in [02_files.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/02_files.py).

## args And kwargs

### *args and **kwargs

Oftentimes, especially when writing decorators, you need to write a function that can accept any number of arguments (positional and keyword), and perform actions on these arguments no matter how many of them there are. By using `*args` and `**kwargs` as arguments to your function, you can ensure that the variable `args` and `kwargs` will contain all of the previously unused arguments that were passed into your function.

You must remember that `args` will be a tuple containing all positional arguments that were passed, and `kwargs` will be a dictionary containing all of the keyword arguments. For instance:

```
def add_all_args(*args):
    return sum(list(args))

print(add_all_args(1, 2, 3, 4, 5))  # 15
```

args and kwargs examples can be found in [03_args_and_kwargs.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/03_args_and_kwargs.py).

### Lambda

A **lambda** is an anonymous function that can be defined in-line without the use of the `def` keyword. THis is extremely useful when defining a custom sort ordering for a collection. Example:

```
# Here we have a list of tuples
# each representing a food and its price
lst = [
    ('cake', '30')
    ('orange', '3')
    ('pasta', '20')
]

# This lambda function lets us sort
# by the price of the items
lst.sort(key=lambda x: x[1])
```

In Python, `lambda` functions can have any number of arguments. Here is an example of a `lambda` function with multiple parameters: 

`lambda x, y: x + y + 5`

In Python, lambda functions can have optional parameters. Here is an example of a lambda with an optional parameter:

`lambda x, y=1: x + y + 5`

In Python, `lambda` functions can accept positional arguments. Here is an example of calling a `lambda` function using a keyword argument:

```
func = lambda x, y: x + y + 5
func(y=1, x=1)  # this will return 7
```

Examples of what you can do with lambda functions can be found in [04_lambda_functions.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/04_lambda_functions.py).