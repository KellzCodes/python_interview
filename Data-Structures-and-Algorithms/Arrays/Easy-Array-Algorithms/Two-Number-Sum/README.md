# Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

#### Sample Input

```
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

#### Sample Output
```
[-1, 11] // the numbers could be in reverse order
```

## Hints

#### Click the arrows to see the hints

<details>
  <summary><b>Hint 1</b></summary>
Try using two for loops to sum all possible pairs of numbers in the input array. What are the time and space implications of this approach?
</details>

<details>
  <summary><b>Hint 2</b></summary>
Realize that for every number X in the input array, you are essentially trying to find a corresponding number Y such that X + Y = targetSum. With two variables in this equation known to you, it shouldn't be hard to solve for Y.
</details>

<details>
  <summary><b>Hint 3</b></summary>
Try storing every number in a hash table, solving the equation mentioned in Hint #2 for every number, and checking if the Y that you find is stored in the hash table. What are the time and space implications of this approach?
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
O(n) time | O(n) space - where n is the length of the input array
</details>

## Solution 1 Walkthrough

Using two for loops can give a solution but it would cost `O(N²)` time.

The better way of solving this is to use a hash table. It's going to cause extra space but it might make our algorithm faster. 

We can traverse our array and store every number we see in a hash table. This will allow us to then access these numbers in constant time through the hash table.

Python dictionary is a hash table.

At each number we traverse, we are going to check if the number needed to sum up to the target value is stored in the hash table. 

In our example, `target sum = 10` and `current num = x`

We want to find `y`such that `x + y = 10`. In other words, we can isolate `y` so that `y = 10 - x`

![image](https://github.com/KellzCodes/python_interview/assets/19383145/58a13f05-030a-4996-aacf-32ddd7bb9dce)

If `y` is in our hash table, then we just return `x` and `y`. Accessing the hash table can be done in `O(1)` time. 

Otherwise we keep traversing the array and we just make sure to store `x` in the hash table. 

Below is an illustration of traversing through the array. We solve for `y` and store the `x` values in the hash table as `True`

![image](https://github.com/KellzCodes/python_interview/assets/19383145/de1033a5-2515-43b8-87b5-4a3b535c580c)

Solution 1 can be found in [hash_solution.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Two-Number-Sum/hash_solution.py).

## Solution 2 Walkthrough

This solution is not the most optimal because it runs in `O(log(n))` time and `O(1)` space

First you sort the array in ascending order. 

Then you set two pointers: left and right. The left pointer will point to the beginning of the array. The right pointer will point to the end of the array. 

We add the value of the left and right pointers. If they are equal to the target sum then we return an array with both values.

If the sum of the pointers are smaller than the target sum, we move the left pointer to the right to a bigger number (remember the array is sorted)

If the sum of the pointers are bigger than the target sum, we move the right pointer to the left to a smaller number.

This solution is `O(nlog(n))` because of the sorting.

![image](https://github.com/KellzCodes/python_interview/assets/19383145/c51ff1d9-44f8-43e8-8efe-24089079078c)

Solution 2 can be found in [pointer_solution.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Two-Number-Sum/pointer_solution.py).