# create a function that returns an inner function
def outer(x):
    def inner(y):
        print(x + y)

    return inner


func = outer(5)
func(6)  # 11


# call an inner function from an outer function
def out(x):
    def inner(y):
        print(x * y)

    inner(5)


out(6)  # 30


# return two inner functions
def sum_3(x):
    def inner(y):
        def inner2(z):
            print(x + y + z)

        return inner2

    return inner


sum_3(5)(6)(7)  # 18


# build a list by returning an inner function
def collection():
    lst = []

    def inner(value):
        lst.append(value)
        return lst

    return inner


add_value = collection()
print(add_value(1))  # [1]
print(add_value(3))  # [1, 3]
print(add_value(4))  # [1, 3, 4]
print(add_value(2))  # [1, 3, 4, 2]


# use nonlocal keyword to help return an inner function that changes an immutable data type
def counter(start):
    count = start

    def increment(value):
        nonlocal count  # references the original count variable
        count += value
        return count

    return increment


count = counter(2)
print(count(1))  # 3


# run print statements to see which one prints first
def funcs():
    def inner():
        def inner2():
            nonlocal x
            x = 2
            print("Inner2: ", x)

        x = 3
        inner2()
        print("inner: ", x)

    x = 4
    inner()
    print("outer: ", x)


funcs()  # Inner2:  2  inner:  2  outer:  4

