# print an exception
try:
    int("Hello")
except:
    print("Exception!") # Exception!
print("Done") # Done

# Store a specific exception then print it
try:
    int("Hello")
except ValueError as e:
    print("Exception!", e) # Exception! invalid literal for int() with base 10: 'Hello'
print("Done") # Done

# handle multiple exceptions
try:
    2 / 0
except ValueError as e:
    print("Value Exception!", e) # this line of code doesn't print anything because of no Value Error
except ZeroDivisionError as e:
    print("Zero Division Exception!") # Zero Division Exception!
print("Done") # Done

# general exception
try:
    int("Hello")
except Exception as e:
    print("Exception!", e) # Exception! invalid literal for int() with base 10: 'Hello'
print("Done") # Done

# finally block
try:
    int("Hello")
except Exception as e:
    print("Exception!", e) # Exception! invalid literal for int() with base 10: 'Hello'
finally:
    print("done") # done

'''
# raise an exception
raise ValueError("This is an error") # ValueError: This is an error
'''

'''
# raise a custom exception
num = input("Enter a number: ")
if not num.isdigit():
    raise ValueError("This is not a valid number!")
'''

while True:
    num = input("Enter a number: ")
    try:
        num = float(num)
        break
    except ValueError as e:
        print("Not a valid float, try again!")

'''
Write a program that asks a user for two numbers: a numerator and a denominator. Your program should divide the
numerator by the denominator and handle any exceptions that might occur during the division. 

Specifically, your program should catch exceptions when either the numerator or denominator isn't a number and when 
the denominator is 0 (you can't divide by zero). All exceptions should be caught and handled, even when there are 
multiple.

If the division doesn't raise any exceptions, the program should print the result of the division. And regardless of 
outcome, the program should tell the user goodbye!
'''
numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")
try:
    numerator = float(numerator)
except ValueError:
    print("The numerator is not a number.")

try:
    denominator = float(denominator)
except ValueError:
    print("The denominator is not a number.")

try:
    result = numerator / denominator
    print(f"The result of this division is {result}.")
except TypeError:
    print("This division cannot be performed.")
except ZeroDivisionError:
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
finally:
    print("Goodbye!")
