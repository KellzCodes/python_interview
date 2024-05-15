# create an iter() object that iterates over a list
x = [1, 2, 3, 4]
x_iter = iter(x)
print(next(x_iter))  # 1
print(next(x_iter))  # 2
print(next(x_iter))  # 3

# create a while loop that moves the iter through the entire iterable catching an exception
x = [4, 5, 6, 7]
x_iter = iter(x)
while True:
    try:
        print(next(x_iter))  # 4 5 6 7
    except StopIteration:
        break


# create a custome iterator
class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __iter__(self):
        return NumberIterator(self.num1, self.num2, self.num3)


class NumberIterator:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        elif self.current == 2:
            return self.two
        elif self.current == 3:
            return self.three
        else:
            raise StopIteration


nums = Numbers(1, 2, 3)
itr = iter(nums)
for num in nums:
    print(num)  # 1 2 3


# create custom iterable
class Numbers2:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        self.current += 1

        if self.current == 1:
            return self.num1
        elif self.current == 2:
            return self.num2
        elif self.current == 3:
            return self.num3
        else:
            raise StopIteration


nums = Numbers2(1, 2, 3)
for val in nums:
    print(val)  # 1 2 3

'''
Write a class based iterator name "Range" that is initialized by passing three integer values, a start, stop, and step. 
Your iterator should mimic the "range" function in functionality but always accept three integer values.

You may assume all three of these initialization values will always be integers and that the step will never be zero.
'''


class Range:
    def __init__(self, start, stop, step):
        # Initialize the Range object with start, stop, and step values
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # Set the current position to start when the iteration begins
        self.current = self.start
        return self

    def __next__(self):
        # Check if the current value has passed the stop value (accounting for direction)
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration  # End iteration if stepping negatively beyond stop
        elif self.step > 0 and self.current >= self.stop:
            raise StopIteration  # End iteration if stepping positively beyond stop

        # Increment current position by step
        self.current += self.step

        # Return the value of current before the increment in this iteration
        return self.current - self.step

