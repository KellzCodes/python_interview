import time


# create a decorator
def decorator(func):
    def wrapper(x):
        print("Wrapper function called func", x)
        result = func()
        return result

    return wrapper


@decorator
def foo():
    print("foo")


foo(1)  # Wrapper function called func 1  foo


# create a decorator that can take any amount of arguments
def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Wrapper function called func!")
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator2
def foo(x, y, z=None):
    print(x, y, z)


foo(2, 3, z=4)  # Wrapper function called func!  2 3 4


# create a timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time = end_time - start_time
        print("Time taken to execute:", total_time)
        return result

    return wrapper


@timer
def loop():
    for _ in range(1000000):
        pass


@timer
def get_max(x, y, z):
    return max(x, y, z)


loop()  # Time taken to execute: 0.01902174949645996
print(get_max(1, 2, 3))  # Time taken to execute: 0.0  3


# work with multiple decorators
def pretty_printer(func):
    def wrapper(*args, **kwargs):
        print()
        result = func(*args, **kwargs)
        print()
        return result

    return wrapper


@timer
@pretty_printer
def print_numbers(num):
    for i in range(num):
        print(i)


print_numbers(5)  # 0 1 2 3 4  Time taken to execute: 0.0

'''
Write a decorator function named "add_one" that simply adds one to the return value of any function it decorates. 
Then use this function to decorate the "add_values" function. 

You may assume the arguments passed to "add_values" will always be integers.

def add_values(x, y):
    return x + y
'''

def add_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1
    return wrapper

@add_one
def add_values(x, y):
    return x + y

'''
Write a decorator name "print_return_value" that prints the return value of any function it decorates. 
Your decorator should work on any function, regardless of the number of parameters.
'''
def print_return_value(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

