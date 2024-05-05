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

An **attribute is an **object** that belongs to either a class, or to an instance of that class. Attributes of an object can be referenced using the `.` notation: `print(person.name)`.

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