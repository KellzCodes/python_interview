class Student:
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    # create an instance method that calculates average grades
    def average(self):
        return sum(self.grades) / len(self.grades)

    # create a class method that curves the average grades
    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        average = cls.get_average_from_grades(grades)
        return min(average + cls.grade_bump, 100)

    # create a static method that calculates average grades
    @staticmethod
    def get_average_from_grades(grades):
        return sum(grades) / len(grades)


s1 = Student("Kelli", [80, 75, 65, 100])
s2 = Student("Bill", [60, 50, 65, 60])

average = s1.get_average_from_grades(s1.grades)
print(average)  # 80.0
average2 = s2.get_average_from_grades(s2.grades[:2])
print(average2)  # 55.0
average3 = Student.get_average_from_grades(s1.grades + s2.grades)
print(average3)  # 69.375

'''
Create a "Physics" class that contains no constructor method and three static methods as outlined below.
    - "calculate_net_force(mass, acceleration)" which returns the product of the passed "mass" and "acceleration".
    - "calculate_acceleration(mass, net_force)" which returns the quotient of the passed "net_force" and "mass".
    - "calculate_mass(net_force, acceleration)" which returns the quotient of the passed "net_force" and "acceleration".

Your static methods should handle any errors cleanly and return the value 0.0 if any error occurs or invalid input is passed. 
For purpose of this question, invalid input is any negative value.
'''
class Physics:

    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass < 0 or acceleration < 0:
            return 0.0
        return mass * acceleration

    @staticmethod
    def calculate_acceleration(mass, net_force):
        if mass <= 0 or net_force < 0:
            return 0.0
        return net_force / mass

    @staticmethod
    def calculate_mass(net_force, acceleration):
        if net_force < 0 or acceleration <= 0:
            return 0.0
        return net_force / acceleration