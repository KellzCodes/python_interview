# Advanced Programming

### Contents
- [Modules and Packages](#modules-and-packages)
- [Files](#files)
- [*args And **kwargs](#args-and-kwargs)
- [Lambda Functions](#lambda)
- [Map and Filter](#map-and-filter)
- [Function Closures](#function-closures)
- [Decorators](#decorators)
- [Iterators](#iterators)
- [Generators](#generators)
- [Compilers and Interpreters](#compilers-and-interpreters)
- [Threads and Processes](#threads-and-processes)
- [Python Global Interpreter Lock](#python-global-interpreter-lock)
- [Threads](#threads)
- [Asynchronous Programming](#asynchronous-programming)
- [Advanced Programming Assessments](#advanced-programming-assessments)

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

## Lambda

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

## Map and Filter

**Map** and **Filter** are paradigms of functional programming. They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.

Essentially, these two functions allow you to apply a function across a number of iterables, in one fell swoop. `map` and `filter` come built-in with Python (in the `__builtins__` module) and require no importing.

### Map

The map() function in python has the following syntax:

`map(func, *iterables)`

Where `func` is the function on which each element in `iterables` (as many as they are) would be applied on. Notice the asterisk(*) on `iterables`? It means there can be as many iterables as possible, in so `far` func has that exact number as required input arguments. Before we move on to an example, it's important that you note the following:

1. In Python 2, the `map()` function returns a list. In Python 3, however, the function returns a map object which is a generator object. To get the result as a list, the built-in `list()` function can be called on the map object. i.e. `list(map(func, *iterables))`
2. The number of arguments to `func` must be the number of iterables listed.

Say I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase. With `map()` functions, I simply do this:

```
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)  # Outputs to ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
```

### Filter

While `map()` passes each element in the iterable through a function and returns the result of all elements having passed through the function, `filter()`, first of all, requires the function to return boolean values (true or false) and then passes each element in the iterable through the function, "filtering" away those that are false. It has the following syntax:

`filter(func, iterable)`

The following points are to be noted regarding `filter()`:
1. Unlike `map()`, only one iterable is required.
2. The `func` argument is required to return a boolean type. If it doesn't, `filter` simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that `func` must only take one argument.
3. `filter` passes each element in the iterable through `func` and returns only the ones that evaluate to true.

The following is a list (`iterable`) of the scores of 10 students in a Chemistry exam. Let's filter out those who passed with scores more than 75...using `filter`.

```
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)  # Outputs to [90, 76, 88, 81]
```

Examples of what you can do with map and filter can be found in [05_map_and_filter.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/05_map_and_filter.py).

## Function Closures

A **Closure** in Python is a function object that remembers values in enclosing scopes even if they are not present in memory. 

It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.

```
# Python program to illustrate 
# closures 
def outerFunction(text): 

	def innerFunction(): 
		print(text) 

	# Note we are returning function
	# WITHOUT parenthesis
	return innerFunction 

if __name__ == '__main__': 
	myFunction = outerFunction('Hey!') 
	myFunction() 
```

Examples of function closures can be found in [06_function_closures.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/06_function_closures.py).

## Decorators

**Decorators** describe a special kind of function that is meant to **wrap** another function. The canonical example is to write a decorator that is meant to pring out the time it took for a given function to execute whenever it is called.

A particular `@` notation is used to indicate that a function should be wrapped by one or more **decorators**:

```
@timer
def run_simulation():

    ...
```

When using multiple decorators the modifications of the second decorator (one furthest to the function) will be applied to the modifications of the first decorator (one closest to the function).

```
@timer
@log_output
def func():
    ...
```

Decorator examples can be found in [07_decorators.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/07_decorators.py).

## Iterators

An **iterator** is a special kind of object that implements a single function: `next()`. Iterators historically were created through class definitions which had to implement the `__iter__()` method to create the iterator, in addition to the `__next__()` method. However, most modern programmers opt to use the **generator** syntax nowadays due to increased readability and conciseness.

An iterator raises the `StopIteration` exception when it runs out of elements. This exception is raised from the iterators `__next__` method.

Iterator examples can be found in [08_iterators.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/08_iterators.py).

## Generators

A **Generator** in Python is a function that returns an iterator using the Yield keyword.

A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the `yield` keyword rather than return. If the body of a def contains `yield`, the function automatically becomes a Python generator function. 

```
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value)  # outputs to 1 2 3
```

Generator examples can be found in [09_generators.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/09_generators.py).

## Compilers and Interpreters

### Compiler
A **compiler** is a program that takes in source code (the code that we, humans, write) and transforms it into code that a machine can interpret (bytecode) or execute (binary code).

### Interpreter
An **interpreter** is a program that is capable of translating code (typically bytecode) into machine code that can be ran and executed by the CPU (central processing unit). Python code is first compiled into bytecode, that bytecode is then passed to the interpreter where it is interpreted and executed.

### Source Code
The **source code** is the code that the programmers write and read.

### Bytecode
**Bytecode** is program code that has been compiled from source code into a lower level language that can be understood by an interpreter.

The first step that occurs when Python is ran is the following. The compiler translates Python source code into bytecode that is then read and executed by the interpreter.

Before the interpreter can execute any code it must first be translated into bytecode. The compiler translates Python source code into bytecode which is lower-level code that can be interpreted by the interpreter. The interpreter then executes bytecode in its execution environment.

## Threads and Processes

### Thread
A **thread** is a flow of execution of your program. By default, Python will run your program in a single thread, the **main thread**, which will execute your Python code line by line.

When trying to speed up certain programs using **concurrency**, many programs choose to run multiple threads at the same time. The `threading` package that comes pre-installed contains functions and classes that allow you to create new threads and coordinate them.

The most important elements of this library are: `Thread` and `Lock`.

### Process
A **process** is an application or program that is running on your computer. Processes are allocated their own memory space and always contain at least one thread, but may be split into multiple threads that are executing concurrently.

### Concurrency
**Concurrency** refers to the ability for parts of a program, application, or algorithm (i.e., multiple threads) to be executed simultaneously.

### Parallelism
**Parallelism** refers to several computations occurring at the same time. Parallel programs utilize multiple logical processing cores of your CPU to increase speed. This is different from a concurrent program that may only utilize a single logical CPU core.

### Modern Processors

Most modern day processors have more logical cores than they do physical cores due to a technology called hyperthreading (for intel CPU's) and clustered multithreading (for AMD CPU's). This allows each physical core to perform 2 operations at the same time, hence why a 4 core CPU with hyperthreading is said to have 8 logical cores. The number of logical cores determines how many operations can be performed in parallel.

All operations performed by the CPU are a part of a thread and only one operation per thread can be ran at anytime. Therefore, a processor with 8 logical cores can run 8 threads at a time, or more specifically work on 8 operations in 8 different threads simultaneously.

## Python Global Interpreter Lock

### Mutex

A **mutex** is a *mutually exclusive lock* that controls the access to a section of code. Mutexes are typically used in multi-threaded programs when a section of code should only be executed by one thread at a time. If one thread has acquired the mutex, all other threads must wait until that thread releases it before they can execute that locked section of code.

## Threads

### Thread

A **thread** is a flow of execution of your program. By default, Python will run your program in a single thread, the **main thread**, which will execute your Python code line by line.

When trying to speed up certain programs using **concurrency**, many programs choose to run multiple threads at the same time. The `threading` package that comes pre-installed contains functions and classes that allow you to create new threads and coordinate them.

The most important elements of this library are: `Thread` and `Lock`.

### Concurrency

**Concurrency** refers to the ability for parts of a program, application or algorithm (i.e., multiple threads) to be executed simultaneously.

### Mutex

A **mutex** is a *mutually exclusive lock* that controls the access to a section of code. Mutexes are typically used in multi-threaded programs when a section of code should only be executed by one thread at a time. If one thread has acquired the mutex, all other threads must wait until that thread releases it before they can execute that locked section of code.

Thread examples can be found in [13_threads.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/13_threads.py).

## Asynchronous Programming

Asynchronous programming refers to a form of multitasking that allows for faster execution of programs and tasks by dividing a single task into smaller chunks of code. This approach makes it easier for a program to process multiple requests at once, allowing the user to make more efficient use of their time and resources. It allows developers to create complex software applications with minimal effort.

In Python, asynchronous programming is based on the event-driven programming model. This involves using ‘callbacks’, or functions that are triggered as soon as an event occurs. These functions can be used to perform a wide variety of tasks, like making an HTTP request, sending a notification, or even executing some long-running code without blocking the main thread. 

Usually, asynchronous code in Python is directly related to an event loop that needs to be triggered. This loop runs continuously and checks for any new events that need to be processed. Once an event is detected and the loop is triggered, the async code will call the appropriate callback function. 

Asynchronous Programming examples can be found in [14_asynchronous_programming.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/14_asynchronous_programming.py).

# Advanced Programming Assessments

## Positive Even Squares

Write a function that accepts any number of positional arguments, all of which you may assume will be lists of integers. Your function should filter all of these lists such that they only contain even positive integers and combine all of the lists into one list of integers. Your function should then modify the combined list such that it contains the squares of all of the elements and return that list.

Use a combination of the `map`, `filter`, and `lambda` functions/keywords to modify the lists.

The solution can be found in [positive_even_squares.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/positive_even_squares.py).

## Integer Sum

Write a function named `integer_sum` that accepts any number of positional arguments, which are assumed to be integers. This function should return the sum of all of these integers.

To handle invalid input (arguments that are not integers) you must write the following decorators and use them to decorate the `integer_sum` function.

- `flatten_lists`: this decorator should flatten any `list` arguments for the decorated function by extracting their elements and passing them as individual arguments instead of the list. For example, if `[1, 2, True]` is an argument, then `1`, `2` and `True` should be extracted and passed as arguments instead of the `list` to the decorated function.
- `convert_strings_to_ints`: this decorator should convert any string arguments that are valid integers to integers and pass them to the decorated function. Any string that is not a valid integer should be removed as an argument to the decorated function.
- `filter_integers`: this decorator should remove any argument that is not an integer and call the decorated function with only integer arguments.

You may assume all arguments passed to `integer_sum` will be of type `float`, `int`, `str` or `list`.

The solution can be found in [integer_sum.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/integer_sum.py).

## Generate String

Write a generator that accepts a string and an integer called `frequency` and generates a sequence as follows:  
`string[0] * frequency + string[1] * frequency + ... + string[-2] * frequency + string[-1] * frequency`.  
Your generator should **not** store this string, it should generate the next element in the sequence each time its `next` method is called.

You should create this generator in both a functional and class-based way. Your functional generator should be named `generate_string` and your class-based generator (a.k.a. iterator) should be named `GenerateString`.

You may assume that `frequency >= 0`.

The solution can be found in [generate_string.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/generate_string.py).

## Thread Safe Counter

Write a `WordCounter` class that is meant to be able to count words in large texts, so that a user of that class can quickly calculate how many times a specific word occurs in a string. 

`WordCounter` should implement the following methods:

- `process_text(text)` should take in a string, `text`, and update the internal attributes of `WordCounter` in a thread-safe manner. You may assume naively that `text.split(" ")` is good enough to return the list of words in the passed `text`.
- `get_word_count(word)` should take in a string, `word`, and check how many times that word has been seen in all the texts that this `WordCounter` has processed. If this word has never been seen, you should return `0`.

**NOTE:** This class must be thread-safe; meaning that many threads should be able to use the `WordCounter` at the same time, and the calculations must remain accurate as if only a single thread was using the instance of `WordCounter`.

**NOTE:** You may not use the `Counter` class of the `collections` standard library.

The solutions can be found in [thread_safe_counter_1.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/thread_safe_counter_1.py) and [thread_safe_counter_2.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/thread_safe_counter_2.py).

## Asynchronous Fetcher

Write a `BatchFetcher` class that is meant to fetch lots of records from a database very quickly.

Your constructor takes in a `database` object that has an async method called `async_fetch`. This method takes a record identifier (or `record_id`) and returns whatever the database has in storage for that record.

`BatchFetcher` should implement the async method `fetch_records`, which takes in a list, `record_ids`, and should return the list of records corresponding to those `record_ids`.

The solutions can be found in [asynchronous_fetcher_1.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/asynchronous_fetcher_1.py) and [asynchronous_fetcher_2.py](https://github.com/KellzCodes/python_interview/blob/main/4-Advanced-Programming/asynchronous_fetcher_2.py).