# Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

## Hints

### Hint 1
You can solve this question by iterating through the input array from left to right once.

### Hint 2
Try iterating through the input array from left to right, in search of two adjacent integers that can indicate whether the array is trending upward or downward. Once you've found the tentative trend of the array, at each element thereafter, compare the element to the previous one; if this comparison breaks the previously identified trend, the array isn't monotonic.

### Hint 3
Alternatively, you can start by assuming that the array is both entirely non-decreasing and entirely non-increasing. As you iterate through each element, perform a check to see if you can invalidate one or both of your assumptions.

### Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the array

## Solution Walkthrough

The solution code can be found in [monotonic_array.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Monotonic-Array/monotonic_array.py).

### Step 1: Define the Function

We'll start by defining our function `isMonotonic` which takes an array as an input parameter.

```
def isMonotonic(array):
```

### Step 2: Initialize Flags

We need two flags: `isNonDecreasing` and `isNonIncreasing`. Initially, we set both to `True`. These flags will help us determine the nature of the array.

### Step 3: Iterate Through the Array

We'll use a for loop to iterate through the array starting from the second element. We'll compare each element with the previous one to update our flags accordingly.

```
    for i in range(1, len(array)):
```

### Step 4: Update Flags Based on Comparisons

Inside the loop, we compare the current element with the previous one. If the current element is smaller, we set `isNonDecreasing` to `False`. If the current element is `larger`, we set `isNonIncreasing` to `False`.

```
        if array[i] < array[i - 1]:
            isNonDecreasing = False

        if array[i] > array[i - 1]:
            isNonIncreasing = False
```

### Step 5: Return the Result

After the loop completes, we return `True` if the array is either non-decreasing or non-increasing. This means either of the flags should still be `True`.

```
    return isNonDecreasing or isNonIncreasing
```

### Explanation

1. **Initialize Flags**: We start by assuming the array is both non-decreasing and non-increasing.
2. **Iterate Through the Array**: We compare each element with the previous one.
3. **Update Flags**: Based on the comparisons, we update our flags.
4. **Return the Result**: We check if the array is either non-decreasing or non-increasing by returning the logical OR of our flags.

























