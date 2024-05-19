# Strings

One of the fundamental data types in Computer Science, strings are stored in memory as arrays of integers, where each character in a given string is mapped to an integer via some character-encoding standard like **ASCII**.

Strings behave much like normal arrays, with the main distinction being that, in most programming languages (C++ is a notable exception), strings are **immutable**, meaning that they can't be edited after creation. This also means that simple operations like appending a character to a string are more expensive than they might appear.

## Operations on Characters

Every character in a string is going to be stored in memory using a fixed amount of bytes.

All of the operations that we are going to perform on a single character in a string are going to be O(1) time operations.

### traversing a string

`O(N)` time and `O(1)` space

### Copying a string

`O(N)` time and space

### Accessing a character in a string

`O(1)` time and space

### Inserting a value in a string

`O(N)` time and space

In Python, strings are immutable. You cannot alter them after you've created them. If you want to alter a string, you actually have to create a brand new string. You have to copy the string then create a new string with the new character.

The canonical example of an operation that's deceptively expensive due to string immutability is the following:

```
string = "this is a string"
newString = ""

for character in string:
    newString += character
```

The operation above has a time complexity of O(n<sup>2</sup>) where n is the length of string, because each addition of a character to `newString` creates an entirely new string and is itself an O(n) operation. Therefore, n O(n) operations are performed, leading to an O(n<sup>2</sup>) time-complexity operation overall.