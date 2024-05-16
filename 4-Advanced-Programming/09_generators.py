
# create a simple generator
def gen():
    yield 1
    yield 2
    yield 3

print(gen())  # <generator object gen at 0x0000016BAF504B40>
print(type(gen()))  # <class 'generator'>
itr = gen()
for i in itr:
    print(i)  # 1 2 3

# generate fibonacci sequence of numbers
def fib(n):
    last = 1
    second_last = 1
    current = 3

    while current <= n:
        num = last + second_last
        yield num

        second_last = last
        last = num
        current += 1

for val in fib(10):
    print(val)  # 2 3 5 8 13 21 34 55

'''
Write a generator named "new_range" that is initialized by passing three integer values, a start, stop, and step. 
Your generator should mimic the range function in functionality but always accept three integer values.

You may assume all three of these initialization values will always be integers and that the step will never be zero.
'''


# solution 1
def new_range(start, stop, step):
    current = start

    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step


# solution 2
def new_range2(start, stop, step):
    current = start
    while True:
        if step < 0 and current <= stop:
            break
        if step > 0 and current >= stop:
            break

        yield current
        current += step


# solution 3
def new_range3(start, stop, step):
    for i in range(start, stop, step):
        yield i