# Object-Oriented Programming

### Contents
- [Creating Classes](#creating-classes)
- [Methods](#methods)
- [Properties](#properties)
- [Class Methods and Attributes](#class-methods-and-attributes)
- [Static Methods](#static-methods)
- [Inheritance](#inheritance)
- [Abstract Classes](#abstract-classes)
- [Interfaces](#interfaces)
- [Operator Overloading](#operator-overloading)
- [Programming Assessments](#programming-assessments)

Programming languages are often classified based on their syntax, features, and execution models. This course introduces you to the idea of programming paradigms and gives you an in-depth look into one of the most popular ways to think about and organize your programs.

**Object** 

`object` is the class that all other classes inherit from, even if it wasn't declared explicitly by the programmer. Almost everything in Python is an object, including `function`s, `list`s, `int`s, and all other instances of built in data types. An object's type is defined by the cass that was used to instantiate it. For example, the assignment `x = 1` creates a new object with type `int` containing with value `1`.

**Class**

In programming, a `class` can be thought of as a template or a blueprint for the creation of objects. The type of an object is the class that was used to create it. Classes define the attributes and methods (i.e. the behavior) of objects that are instantiated using them.

In Python, the term **instantiation** refers to the creation of an object based on a class.

In Python, the type of object is the class used to instantiate it.

For example, if an object is instantiated from a user defined class called `Animal`, then that object's type is `Animal`.

In object-oriented programming, an objects behavior is defined by the attributes and methods it possesses. Objects of different types behave differently based on the logic defined in the class that was used to instantiate them.

In object-oriented programming, a method is simply a function that is defined inside a class and typically acts on an instance of that class. Methods that accept the `self` parameter are instance methods and can access the attributes and methods of the instance they are called on. Methods are typically called using the `.` (dot) notation.

For example, `"str".count("s")`, `[1, 2, 1].sort()` and `"str".upper()` are all examples of methods. The method comes after the `.` (dot) and the instance that they act on is to the left of the `.` (dot).

## Creating Classes

**Attribute**

An **attribute** is an **object** that belongs to either a class, or to an instance of that class. Attributes of an object can be referenced using the `.` notation: `print(person.name)`.

**Class attributes** are attributes that are shared by all instances of that class, while **instance attributes** may have a different value for each and every instance that was created.

In Python object-oriented programming an attribute is any data/objects associated with a class or an instance of a class. Attributes are not always defined inside the class constructor and can be added to an instance after its creation.

**Constructor**

The **constructor** of a class is a function defined within the class definition that will be called when a new instance is created. In Python, the **constructor** is implemented with the `__init__` method.

Typically, the **constructor** is responsible for initializing any instance variables, and essentially prepares the instance for use by the rest of the program.

`self` is always the first parameter in a class constructor. The `self` parameter refers to the instance of the class in which the method or constructor is being called on.

The first parameter in the class constructor (a.k.a the `__init__` method) is implicitly passed during the instantiation of a object and is mandatory. Note that the name `self` is a recommended convention in Python but not the mandatory name for this first parameter.

**Instance**

An **instance** of a class is an object created from that class's "blueprint". For example, `Person("Kelli")` will return an **instance** of the `Person` class.

**Encapsulation**

Encapsulation, in **Object-Oriented Programming**, refers to how a programmer might prevent outside access to the details of a class in order to simiplify the way the class might be used, or to make it harder to misuse the functionality that is exposed through certain methods or properties.

According to PEP-8 (the style guide for Python) the proper casing for class names is **PascalCase**. Note that this is also commonly referred to as **CapitalCamelCase**.

Examples of what you can do with classes can be found in [02_creating_classes.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/02_creating_classes.py).

## Methods

A **method** is a function defined inside a **class** definition. There are three important kinds of methods: **instance methods**, **class methods**, and **static methods**.

Examples of what you can do with methods can be found in [03_methods.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/03_methods.py).

## Properties

In Python, all attributes of an object are public. This means they can be accessed from outside the class they are defined in.

In Python, since there is no access modifiers (private, public or protected keywords) to denote an attribute as private you prefix it with a `_`. The attribute can still be accessed and modified like all other attributes but the `_` prefix denotes that it should not be, this is a Python convention.

In object-oriented programming, getters are used to return the value of attributes while setters are used to set the value of attributes. Both allow you to hide complexity by providing a single method that can be used to validate data before assigning it to an attribute (setter) or mutate data (e.g. rounding a number) before returning it (getter). Setters may also constrain an attribute value by only allowing you to set it to something considered valid by the class (e.g. you can't set a negative salary for an employee).

In Python, there is a built-in function for declaring the properties of the program class, which is known as the `property()` function. Python `property()` built-in function and `@property` decorator is provided to easily implement the getters and setters methods in Object-Oriented Programming.

Examples of what you can do with properties can be found in [04_properties.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/04_properties.py).

## Class Methods And Attributes

**Class Attribute**

An **attribute** is an **object** that belongs either to a class, or to an instance of that class. Attributes of an object can be referenced using the `.` notation: `print(person.name)`.

A **class attribute** is an attribute that is associated with a class but not with an instance of a class. Class attributes can be modified and accessed by using the class name directly or by using an instance of the class. Typically class attributes are defined at the top of the class, inside the class body.

**Class Method**

A **class method** is a method that has a mandatory `cls` parameter and can only access class attributes and other class methods. It does not act on an instance of a class, but on the class itself. Class methods are denoted with the `@classmethod` decorator.

Examples of what you can do with class methods and attributes can be found in [05_class_methods_and_attributes.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/05_class_methods_and_attributes.py).

## Static Methods

A **static method** is defined within a class but should not reference anything relevant to that class specifically, except for other static methods. 

For the most part, static methods should only be used for **pure** functions, which do not use temporary variables outside of their own scope and exclusively transform a set of inputs into some outputs. For instance, a method that converts a distance from kilometers to miles should most like be **static**. Static methods are denoted using the `@staticmethod` decorator.

Examples of what you can do with static methods can be found in [06_static_methods.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/06_static_methods.py).

## Inheritance

**Child Class**

When a class `A` inherits from class `B`, we say that class `A` is a **child class** of `B`.

Child class, subclass and derived class are all synonymous for a class that inherits from another class.

**Parent Class**

When a class `A` inherits from class `B`, we say that class `B` is a **parent class** of `A`.

Parent class, superclass and base class are all synonymous for a class that is inherited from.

**Polymorphism**

**Polymorphism** is a term originating from biology, where poly means many and morphism means forms (this is a simplification). In programming, polymorphism refers to the ability for an object to behave in different ways and exhibit different behavior based on the context it's used in.

**Method Overriding**

Method **overriding** is when a programmer re-defines a method on a class that was already defined in its **parent class(es)**.

Inheritance examples are found in [07_inheritance.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/07_inheritance.py).

## Abstract Classes

An **abstract method** is a method that is defined in an interface or abstract class and does not provide an implementation. Abstract methods are designed to be overridden by base or subclasses that extend the class or implement the interface they're defined in.

An **abstract class** is a class that contains at least one abstract method and is not meant to be instantiated. Abstract classes are meant to act as the parent or base class in an inheritance hierarchy. Typically abstract classes implement some functionality that can be used commonly by all child or subclasses.

All method types are allowed in an abstract class. Abstract classes usually contain some concrete methods (ones that provide an implementation) while also defining abstract methods that must be implemented by child classes that inherits from it.

In many other programming languages it is enforced that a subclass of an abstract class must implement any abstract methods it contains. However, in Python this behavior is not enforced and although it is conventional for subclasses of an abstract class to do so it is not required.

Abstract class examples are found in [08_abstract_classes.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/08_abstract_classes.py).

## Interfaces

In Python, there is no formal definition for an **interface**, but we can still represent one by creating a class that only defines abstract methods. An interface is designed to be used as an abstract data type that enforces that classes that implement it define specific methods and behavior.

Interfaces, like abstract classes, should not be instantiated. There are meant to act as an abstract data type that classes will implement.

Unlike abstract classes the only methods allowed in an interface are abstract. An interface does not provide any concrete methods or behavior.

Interface examples can be found in [09_interfaces.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/09_interfaces.py).

## Operator Overloading

**Dunder Methods** are methods that are prefixed and suffixed by two underscores. The most important to know is the `__init__` dunder method, which is sometimes called the `constructor` of the class, and defines how a new instance is initialized after being created.

Implementing those methods will sometimes change how certain operators will behave (like `+` with `__add__` and `==` with `__eq__`). Other examples include `__len__`, `__str__`, `__repr__` and many more.

Operator Overloading examples can be found in [10_operator_overloading.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/10_operator_overloading.py).

# Programming Assessments

## Inventory Class

Write an `Inventory` class, as defined below, that handles the management of inventory for a company. All instances of this class should be initialized by passing an integer value named `max_capacity` that indicates the maximum number of items that can be stored in inventory. Your `Inventory` class will need to store items that are represented by a `name`, `price`, and `quantity`.

Your class should implement the following methods.
- `add_item(name, price, quantity)`: This method should add an item to inventory and return `True` if it was successfully added. If adding an item results in the inventory being over capacity, your method should return `False` and omit adding this item to the inventory. Additionally, if an item with the passed `name` already exists in inventory, this method should return `False` to indicate the item could not be added.
- `delete_item(name)`: This method should delete an item and return `True` if the item was successfully deleted. If there is no item with the passed `name`, this method should return `False`.
- `get_most_stocked_item()`: This method should return the name of the item that has the highest quantity in the inventory, and return `None` if there are no items in the inventory. You may assume there will always be exactly one item with the largest quantity, except for the case where the inventory is empty.
- `get_items_in_price_range(min_price, max_price)`: This method should return a list of the names of items that have a price within the specified range (inclusively).

Note: you may assume all input/arguments to your class will be valid and the correct types. For example, the `max_capacity` will always be greater thatn or equal to `0` and a valid integer.

The solution can be found in [Inventory.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/Inventory.py).

## Student Class

Write a `Student` class, as defined below, that keeps track of all created students.

Your class should implement the following methods, class variables and properties:

- An instance attribute called `name`.
- A property called `grade` that returns the grade of that student. Trying to set the grade should raise a `ValueError` if the new grade is not a number between `0` and `100`.
- A static method called `calculate_average_grade(students)` that accepts a list of `Student` objects and returns the average grade for those students. If there are no students in the list, it should return `-1`.
- A class variable called `all_students` that stores all of the student objects that have been created in a list.
- A class method named `get_average_grade()` which returns the average grade of all created students.
- A class method named `get_best_student()` which returns the student object with the best grade out of all the currently created students. If there are no students created this method should return `None`. You may assume there will always be one student with the best grade, except in the case where there are no students created.

The solution can be found in [Student.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/Student.py).

## Geometry Inheritance

Create 4 classes: `Polygon`, `Triangle`, `Rectangle` and `Square`. The `Triangle` and `Rectangle` class should be subclasses of `Polygon`, and `Square` should be a subclass of `Rectangle`.

Your `Polygon` class should raise a `NotImplementedError` when the `get_area()` and `get_sides()` methods are called. However, it should correctly return the perimeter of the polygon when `get_perimeter()` is called. Treat the `Polygon` class as an abstract class.

Your `Triangle` class should have a constructor that takes in 3 arguments, which will be the lengths of the 3 sides of the triangle. You may assume the sides passed to the constructor will always form a valid triangle.

Your `Rectangle` class should have a constructor that takes in 2 arguments, which will be the width and height of the `Rectangle`.

Your `Square` class should have a constructor that takes in 1 argument, which will be the length of each side of the `Square`.

Your `Triangle` and `Rectangle` classes should both implement the following methods:
- `get_sides()`: This method returns a list containing the lengths of the sides of the shape.
- `get_area()`: This method returns the area of the polygon.

Your `Square` class should only have an implementation for its constructor, and rely on the `Rectangle` superclass for implementations of `get_sides()` and `get_area()`.

Note: To calculate the area of a triangle given three side lengths (`x`, `y`, and `z`) you can use the following formula. First calculate the semi perimeter `s` using: `s = (x + y + z) / 2`. Then calculate the area `A` using: `A = math.sqrt(s * (s - x) * (s - y) * (s - z))`.

The solution can be found in [Geometry_Inheritance.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/Geometry_Inheritance.py).

## Deck Class

Create a `Deck` class that represents a deck of `52` playing cards. The `Deck` should maintain which cards are currently in the deck and never contain duplicated cards. Cards should be represented by a string containing their value (`2` - `10`, `J`, `Q`, `K`, `A`) followed by their suit (`D`, `H`, `C`, `S`). For example, the jack of clubs would be represented by `"JC"` and the three of hearts would be represented by `"3H"`.

Your `Deck` class should implement the following methods:
- `shuffle()`: This method shuffles the cards randomly, in place. You may use the `random.shuffle()` method to help you do this.
- `deal(n)`: This method removes and returns the last `n` cards from the deck in a list. If the deck does not contain enough cards it returns all the cards in the deck.
- `sort_by_suit()`: This method sorts the cards by suit, placing all the hearts first, diamonds second, clubs third and spades last. The order within each suit (i.e., the card values) does not matter. This method should sort the cards in place, it does not return anything.
- `contains(card)`: This method returns `True` if the given card exists in the deck and `False` otherwise.
- `copy()`: This method returns a new `Deck` object that is a copy of the current deck. Any modifications made to the new `Deck` object should not affect the `Deck` object that was copied.
- `get_cards()`: This method returns all the cards in the deck in a list. Any modifications to the returned list should not change the `Deck` object.
- `__len__()`: This method returns the number of the cards in the `Deck`.

Your deck should always start with exactly 52 cards that are distributed across 4 suits and 13 values where there are no duplicate cards.

Solution 1 can be found in [Deck1.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/Deck1.py).

Solution 2 can be found in [Deck2.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/Deck2.py).

## FileSystem Implementation

In this question, you need to implement a very simplistic `FileSystem` class that mimics the way that your own computer's `FileSystem` works. A `FileSystem` starts empty with only a root node which will always be a directory.

A `FileSystem` is a tree-like structure composed of nodes, each of which is either a `File` or `Directory`.

Files are simplest and only have `name` and `contents` as attributes; which correspond to the name of the file and its contents, respectively. Files also have a `write` method, which sets the contents of that file to the argument passed in. Additionally, files override the `__len__` dunder method which returns the number of characters in the contents of that file.

Directories have a `name` and a `children` attribute. `children` is a dictionary that stores the name of its children nodes as keys, and the nodes themselves as the values of that dictionary. Directories also have the `add` and `delete` methods which are used to add or delete nodes from its `children` dictionary.

For your convenience, the `__str__` methods of each class have been overridden so that you may debug your FileSystem more easily.

Your task is to implement the following methods on the `FileSystem` class:
- `create_directory(path)`: This method should create a `Directory` inside the `FileSystem` at the location specified. For instance, `create_directory("/dir1")` should create a directory as a child of the root of the filesystem called `"dir1"`. Running `create_directory("/dir1/dir2")` should create another directory, `dir2`, inside the one that was just created. If the path is malformed or the operation is impossible, it should raise a `ValueError`.
- `create_file(path, contents)`: This method should create a new file at the desired path, with the contents passed in. If the operation is impossible, it should raise a `ValueError`.
- `read_file(path)`: This method should return the contents of the file at the path parameter. If no such file exists, it should raise a `ValueError`.
- `delete_directory_or_file(path)`: This method should delete the node located at `path`. It should work on files and directories alike, and should raise a `ValueError` if that file does not exist.
- `size()`: This method should return the number of characters across all files in your filesystem.
- `_find_bottom_node(node_names)`: This is a private helper method of the `FileSystem` class that takes in a list of node names and should traverse the filesystem downwards until the last node in the list. For instance, calling this with `["a", "b", "c"]` should first look for a node `a` inside the root node of the filesystem, then for a node `b` inside node `a`, and then return the node `c` which should be a child of node `b`.

Note: for all methods that accept a `path` parameter you will need to first validate that path and then parse it. The `path` will be a string, and from that string you'll need to do one of the following:
- Obtain the directory object used to create a new directory or file inside of.
- Obtain the directory object used to delete a directory or file.
- Obtain the file object to read the contents of.

This is non-trivial because you may need to distinguish between the name of the new node create and the path where this node should be created.

See Below for the base code:

```
class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        # Write your code here.
        pass

    def create_file(self, path, contents):
        # Write your code here.
        pass

    def read_file(self, path):
        # Write your code here.
        pass

    def delete_directory_or_file(self, path):
        # Write your code here.
        pass

    def size(self):
        # Write your code here.
        pass

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        # Write your code here.
        pass


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

```

Solution 1 can be found in [FileSystem_Implementation1.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/FileSystem_Implementation1.py).

Solution 2 can be found in [FileSystem_Implementation2.py](https://github.com/KellzCodes/python_interview/blob/main/3-Object-Oriented-Programming/FileSystem_Implementation2.py).