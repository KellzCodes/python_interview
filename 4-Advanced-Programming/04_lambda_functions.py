# you can put a lambda in a variable and it will act as a function
func = lambda x, y, z=0: x + y + z
print(func(1, 2, 4))  # 7

# sort a list of tuples by their second element
lst = [(1, 2), (-2, -4), (3, 4), (0, 0)]
lst.sort(key=lambda x: x[1])
print(lst)  # [(-2, -4), (0, 0), (1, 2), (3, 4)]

# use a lambda to return another lambda
mul = lambda x: lambda y: x * y
result = mul(2)
print(result(4))  # 8

# use a lambda to return another lambda but use a chain call
sum = lambda x: lambda y: x + y
result = sum(4)(5)
print(result)  # 9

'''
Write the following lambda functions.

    - A lambda function that takes three integer or float parameters and returns their sum. You should store this lambda function 
      in the variable "add_values"
    - A lambda function that takes two string parameters and returns the maximum of their lengths. You should store this lambda 
      function in the variable "max_length"
    - A lambda function that takes two list parameters and returns a set containing the elements from both lists. You should store 
      this lambda function in the variable "create_set"
'''
add_values = lambda x, y, z: x + y + z
max_length = lambda x, y: max(len(x), len(y))
create_set = lambda x, y: set(x + y)