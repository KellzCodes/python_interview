import math
# Create an interface (all methods have to be implemented)
class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError("You must implement compile_code().")

    def execute_code(self):
        raise NotImplementedError("You must implement execute_code().")


class GoCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Go code")

    def execute_code(self):
        print("Execute Go code")


class JavaCode(RunCodeInterface):
    def compile_code(self):
        print("Compile Java code")

    def execute_code(self):
        print("Execute Java code")


# create a function that requires input of a specific type
def run_code(code: RunCodeInterface):
    code.compile_code()
    code.execute_code()


go = GoCode()
run_code(go)  # Compile Java code  Execute Go code
java = JavaCode()
run_code(java)  # Compile Java code  Execute Go code

'''
Shape Interface

import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


# Write your code here.
class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

Complete the "Square" and "Circle" class such that they properly implement the "Shape" interface.
The perimeter of a circle is its circumference which is given by the formula "2 * pi * radius". 
To obtain pi you can use math.pi from python's math module.
The area of a circle is given by the formula "pi * (radius ** 2)"
'''


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length

    def get_perimeter(self):
        return 4 * self.side_length


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius