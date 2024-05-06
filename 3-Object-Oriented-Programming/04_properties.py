
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

'''
BankAccount Class:

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name

Complete the "BankAccount" class by adding a private attribute named "balance" and implementing a getter and setter 
for it. For this question DO NOT USE THE "@property" decorator. 
If any of the listed constraints are broken, your method should not update the balance.
    - The "balance" must always be at least 0
    - The "balance" may not exceed 100,000
    - The "balance" must be a number
    - When the "balance" is retrieved, it is always rounded to the nearest dollar.
'''
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance >= 100000:
            return

        self._balance = balance


'''
BankAccount Class:

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name

Complete the "BankAccount" class by adding a private attribute named "balance" and implementing a getter and setter 
for it. For this question YOU SHOULD USE THE "@property" decorator. 
If any of the listed constraints are broken, your method should not update the balance.
    - The "balance" must always be at least 0
    - The "balance" may not exceed 100,000
    - The "balance" must be a number
    - When the "balance" is retrieved, it is always rounded to the nearest dollar.
'''
class BankAccount2:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance >= 100000:
            return

        self._balance = balance
