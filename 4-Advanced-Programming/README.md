# Advanced Programming

## Modules and Packages

### Main Module

In Python, the `main` module is the one that is invoked or run directly. Python will automatically set the `__name__` variable of that module to the string `"__main__"`. All modules that are imported from that main package will have their own values for the `__name__` variable.

When writing your modules in Python, it is best practice to run some parts of the code conditionally based on that `__name__` variable:

```
if __name__ == "__main__":
    print("This code will only run if this is the main package!")
```

### Module
In Python, a module is simply any Python file (something ending in `.py`). Modules provide a way to split code into multiple files and make programs easier to understand. One Python module is able to import code from another Python module.

### Package
A Python package is simply a directory that contains a special file named `__init__.py`, and typically a collection of other Python modules. Packages provide a way to organize Python modules. When importing a Python package the code inside of the `__init__.py` file will run once.

