# Object-Oriented Programming

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

**Parent Class**

When a class `A` inherits from class `B`, we say that class `B` is a **parent class** of `A`.

**Polymorphism**

**Polymorphism** is a term originating from biology, where poly means many and morphism means forms (this is a simplification). In programming, polymorphism refers to the ability for an object to behave in different ways and exhibit different behavior based on the context it's used in.

**Method Overriding**

Method **overriding** is when a programmer re-defines a method on a class that was already defined in its **parent class(es)**.