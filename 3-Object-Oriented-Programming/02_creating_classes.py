# create a class
class Person:
    pass

p1 = Person()
print(p1) # <__main__.Person object at 0x0000027858DF9970>
print(type(p1)) # <class '__main__.Person'>

class Person2:
    # create a dunder (double underscore) method
    def __init__(self):
        print("ran")

p1 = Person2() # ran
print(p1) # <__main__.Person2 object at 0x0000019CE3A69B50>

class Person3:
    # pass a parameter to dunder method
    def __init__(self, x):
        print(x)

p1 = Person3(2) # 2
p2 = Person3(3) # 3

# create an attribute
class Person4:
    def __init__(self, name):
        self.name = name

p1 = Person4("Kelli")
p2 = Person4("Bill")
print(p1.name) # Kelli
print(p2.name) # Bill

# multiple attributes
class Person5:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person5("Kelli", 21)
p2 = Person5("Bill", 40)
print(p1.name, p1.age) # Kelli 21
print(p2.name, p2.age) # Bill 40

# create new attribute outside of class
p1.new = "random"
print(p1.new) # random

# change an existing attribute outside of class
p1.name = "random"
print(p1.name) # random

# create a fruit class that has name and calories
class Fruit:
    def __init__(self, name, calories):
        selt.name = name
        self.calories = calories

# create a new instance of fruit class: apple with 100 calories
a = Fruit("Apple", 100)
# create a new attribute outside of fruit class
a.color = "Red"

'''
Create a ContactInformation class that is instatiated by passing a "first_name", "last_name", "email", 
and "phone_number". This class should store all of the passed values as instance attributes and have 
an additional attribute "country" that is set by default to "None".

After creating the class, instantiate two instances of it. The first instance should be stored in the 
variable "person1" and the next in "person2".
'''

class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None

person1 = ContactInformation("Kelli", "Davis", "kdavis@example.com", "555-555-5555")
person2 = ContactInformation("Bill", "Nye", "thescienceguy@example.com", "555-555-5555")