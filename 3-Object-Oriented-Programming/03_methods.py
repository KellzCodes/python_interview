class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    # create a method
    def say_hello(self):
        print(f"Hello, {self.name}")

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


p1 = Person("Kelli")
p1.say_hello()  # Hello, Kelli
p1.set_age(21)
print(p1.age)  # 21
print(p1.get_age())  # 21


# create a counter class
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")


counter = Counter()
counter.increment()
counter.decrement()
counter.print_count()  # The current count is 0
counter.increment()
counter.increment()
counter.print_count()  # The current count is 2


# create a counter class with a method that locks the counter
class Counter2:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked

    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")


counter = Counter2()
counter.increment()
counter.print_count()
counter.toggle_lock()
counter.decrement()  # Exception: The counter is locked!

'''
Rectangle class:

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

Add the following to the Rectangle class:
    - "change_position(...)": this method should accept two parameters, one for the "x" position 
       and the other for the "y" position. It should set the corresponding instance attributes 
       such that they are equal to the arguments passed to the method
    - "get_position(...)": this method should return the position of the rectangle ass a tuble in the form 
      (x, y)
    - "get_area(...)": this method should return the area of the rectangle. It should calculate the are by 
       by using the appropriate instance attributes.

You do not need to make any instances of the class once you have added the methods. 
'''


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def change_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return (self.x, self.y)

    def get_area(self):
        return self.width * self.height


'''
Group Class

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

Add the following to the "Group" class:
    - "add(...)": accepts the name of a person as a parameter and adds them to the group
    - "delete(...)": accepts the name of a person as a parameter and deletes them from the group. If the name passed is not
       in the group, this method should raise an "Exception" (use the default exception class called "Exception".)
    - "get_members(...)": returns a sorted list with the names of students in the group. The list should be sorted in 
       ascending order (i.e. A-Z)

You do not need to make any instances of the class once you have added the methods. 
'''
class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group")

    def get_members(self):
        return sorted(self.members)

    '''
    Add an additional method to the "Group" class called "merge(...)". The "merge" method should accept as a parameter an 
    instance of another "Group" object. This method should merge the two groups together and return a new group that contains 
    all of the members from both groups. The newly created group may have any name.
    '''
    def merge(self, group):
        combined_members = self.members + group.members
        new_group = Group("Any name", combined_members)
        return new_group