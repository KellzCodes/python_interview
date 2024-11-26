# Exercise 1: CHeck if a number is even
# Write a function that uses bitwise AND operator to determine if a given integer is even
def is_even(num):
    """
    Checks if a number is even using bitwise AND.
    
    Args:
        num: The integer to check.
    
    Returns:
        True if the number is even, False otherwise
    """
    return (num & 1) == 0

print(is_even(4)) # True
print(is_even(7)) # False


# Exercise 2: Get the nth bit of a number
# Write a function that returns the value of the nth bit (starting from 0 as the least significant bit) of a given integer
def get_nth_bit(num, n):
  """
  Gets the value of the nth bit of a number.

  Args:
    num: The integer to check.
    n: The position of the bit (0-indexed)

  Returns:
    The value of the nth bit (0 or 1)
  """
  return (num >> n) & 1

print(get_nth_bit(10, 1)) # 1
print(get_nth_bit(10, 2)) # 0


# Exercise 3: Set the nth bit of a number
# Write a function that sets the nth bit of a number to 1.
def set_nth_bit(num, n):
  """
  Sets the nth bit of a number to 1.

  Args:
    num: The integer to modify.
    n: The position of the bit (0-indexed).

  Returns:
    The modified integer.
  """
  return num | (1 << n)

print(set_nth_bit(10, 0)) # 11
print(set_nth_bit(10, 2)) # 14


# Exercise 4: Flip all bits of a number
# Write a function that flips all the bits of a given integer
def flip_bits(num):
  """
  Flips all the bits of a number.

  Args:
    num: The integer to flip.

  Returns:
    The integer with all bits flipped.
  """
  return ~num
    
print(flip_bits(10)) # -11


# Exercise 5: Swap two numbers without a temporary variable
# Write a function that swaps two integers using bitwise XOR
def swap_numbers(x, y):
  """
  Swaps two numbers using XOR.

  Args:
    x: The first integer
    y: The second integer

  Returns:
    A tuple of swapped integers (y, x)
  """
  x = x ^ y
  y = x ^ y
  x = x ^ y
  return x, y

print(swap_numbers(5, 10)) # (10, 5)
