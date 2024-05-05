
# Python program to illustrate property() function
class Person:
    def __init__(self, name):
        self._name = name

    # getter function
    def get_name(self):
        print('Getting name...')
        return self._name

    # setter function
    def set_name(self, value):
        print('Setting name to:', value)
        self._name = value

    # deleter function
    def del_name(self):
        print('Deleting name...')
        del self._name

    # Set property() to use get_name, set_name and del_name methods
    name = property(get_name, set_name, del_name)

p = Person('David')
print(p.name)  # Getting name... David
p.name = 'Rocky'  # Setting name to: Rocky
del p.name  # Deleting name...


# Python program to illustrate @property decorator
class Person2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name...')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to:', value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name...')
        del self._name

p = Person2('David')
print(p.name)  # Getting name... David
p.name = 'Rocky'  # Setting name to: Rocky
del p.name  # Deleting name...
