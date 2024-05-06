class Car:
    # class attribute (only associated with class and not any instance of class)
    number_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # instance attribute
        self.number_of_cars = 1


# access class attribute
Car.number_of_cars += 3
c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")
print(Car.number_of_cars)  # 3 (class attribute)
print(c1.number_of_cars)  # 1 (instance attribute)


class Vehicle:
    # class attribute
    number_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # class attribute
        Vehicle.number_of_cars += 1

    # class method
    @classmethod
    def update_number_of_cars(cls, cars):
        cls.number_of_cars = cars


c1 = Vehicle("Ford", "Edge")
c2 = Vehicle("Mazda", "3")
print(c1.number_of_cars)  # 2
print(c2.number_of_cars)  # 2
print(Vehicle.number_of_cars)  # 2
Vehicle.update_number_of_cars(10)
print(c1.number_of_cars)  # 10
print(c2.number_of_cars)  # 10
print(Vehicle.number_of_cars)  # 10


# create circle class with all class methods
class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)


print(Circle.area(4))  # 50.24
print(Circle.perimeter(4))  # 25.12
print(Circle.get_area_and_perimeter(4))  # (50.24, 25.12)

'''
Create an "Employee" class where each employee has a "name", "age", and "salary". This class should 
contain two class attributes that store the average employee age and salary. These class attributes 
should be named "average_age" and "average_salary" and should be updated each time a new employee is 
created.

Note: you may add as many other additional attributes as you like.
'''
class Employee:
    average_age = 0
    average_salary = 0
    num_of_employees = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        total_age = Employee.average_age * Employee.num_of_employees
        total_salary = Employee.average_salary * Employee.num_of_employees
        Employee.average_age = (total_age + age) / (Employee.num_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.num_of_employees + 1)
        Employee.num_of_employees += 1


'''
Create a "Temperature" class whose instances all contain a "kelvin" attribute. This class should also contain two class
attributes named "min_temperature" and "max_temperature" which can be modified by calling the respective class methods 
named "update_min_temperature" and "update_max_temperature".

"min_temperature" must always be less than "max_temperature" and each instances "kelvin" attribute must be between 
"min_temperature" and "max_temperature", inclusively. Any instantiation or method call that breaks the outlined 
constraints should raise an "Exception".

Note: "min_temperature" should be initialized as 0 and "max_temperature should be initialized as "1000"
'''
class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        if kelvin > self.max_temperature or kelvin < self.min_temperature:
            raise Exception("Invalid temperature.")
        else:
            self.kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")
        else:
            cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")
        else:
            cls.max_temperature = kelvin
