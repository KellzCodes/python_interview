# super class
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")


# create an employee class that inherits from Person class
class Employee(Person):
    def __init__(self, first_name, last_name, salary):
        # override the initial constructor of the super class
        super().__init__(first_name, last_name)
        self.salary = salary

    def say_hello(self):
        # override a method from the super class (call a method from the super class)
        super().say_hello()
        print(f"My salary is {self.salary}")


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department


class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth


e = Employee("Kelli", "Davis", 50000)
e.say_hello()  # Hi my name is Kelli Davis My salary is 50000
m = Manager("Kelli", "Davis", 50000, "Sports")
m.say_hello()  # Hi my name is Kelli Davis My salary is 50000
o = Owner("Kimi", "Perry", 1000000)
o.say_hello()  # Hi my name is Kimi Perry

print(type(o))  # <class '__main__.Owner'>
print(isinstance(o, Person))  # True
print(isinstance(m, Person))  # True


# Multiple Inheritance
class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    pass


c = C()  # A
print(isinstance(c, A))  # True
print(isinstance(c, B))  # True


# Duck Typing
class Duck:
    def swim(self):
        print("swimming duck")

    def fly(self):
        print("flying duck")


class Whale:
    def swim(self):
        print("swimming whale")


animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim()
    animal.fly()  # code will run but crash when it gets to this line on Whale() because Whale() has no attribute called fly()

'''
Animal Inheritance

Create an "Animal", "Mammal", and "Reptile" class as defined below. Then create a "Monkey" and "Lizard" class that inherit 
from the proper base classes.
All Mammals and Reptiles are Animals; your inheritance should reflect this.
All Animals have an "age", "weight", and "height". All Mammals have a "sex" and most "Reptiles" have 4 legs but not all. 
Your classes should represent this.
All Monkeys have exactly 5 fingers and a "color". All Lizards have a "tail" and also have a "color". Your classes should 
represent this.
Think carefully about what type of attributes each of your classes should have.
'''
class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex

class Reptile(Animal):
    def __init__(self, age, weight, height, legs):
        super().__init__(age, weight, height)
        self.legs = legs

class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color

class Lizard(Reptile):
    tail = True

    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color