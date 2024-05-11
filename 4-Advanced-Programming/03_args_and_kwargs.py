# make a function you can pass any amount of parameters to
def sum_items(*args):
    print(sum(args))

sum_items(1, 2, 3)  # 6
sum_items(1, 2, 3, 4)  # 10

# make a function you can pass any amount of parameters to as well as key value pairs
def function(*args, **kwargs):
    print(args)
    print(kwargs)

function(1, 2, 3, a=2, b=9)  # (1, 2, 3)  {'a': 2, 'b': 9}

# make a regular function then pass an iterable as a parameter
def mult_items(a, b, c):
    return a * b * c

args = [1, 2, 3]
x = mult_items(*args) # one asterisk is for iterables that aren't dictionaries
print(x)  # 6

kwargs = {"a": 5, "b": 10, "c": 15}
x = mult_items(**kwargs) # two asterisks are for dictionaries
print(x)  # 750

# make a regular function and pass *args and **kwargs to it at the same time
def foo(p1, p2, a, b, c):
    print(p1, p2, a, b, c)
    return a + b + c + p1 + p2


args = [1, 2]
kwargs = {"a": 5, "b": 10, "c": 15}
x = foo(*args, **kwargs)
print(x)  # 1 2 5 10 15  33

# print all values in a list without printing the brackets
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*values)   # 1 2 3 4 5 6 7 8 9

# use both args and kwargs as both parameters and arguments
def test(p1, *args, **kwargs):
    print(p1, args, kwargs)

values = [1, 2, 3, 4, 5, 6]
kwargs = {"s": 1, "hello": 4, "k": True}
test(4, *values, **kwargs)  # 4 (1, 2, 3, 4, 5, 6) {'s': 1, 'hello': 4, 'k': True}

'''
Write a function named get_args_and_kwargs that accepts an unlimited number of positional and keyword arguments. 
The function should return True if there are at least 4 total arguments and if the keyword argument num exists, 
is a number, and is larger than 5. Otherwise it should return False

Your function should handle any error that may occur
'''


def get_args_and_kwargs(*args, **kwargs):
    num_of_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)  # will default to 0 if "num" key doesn't exist

    if not isinstance(num, int) and not isinstance(num, float):
        return False

    return num_of_args >= 4 and num > 5
