# Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

## Hints

### Hint 1
Instead of generating all possible pairs of numbers, try somehow only looking at pairs that you know could actually have the smallest difference. How can you accomplish this?

### Hint 2
Would it help if the two arrays were sorted? If the arrays were sorted and you were looking at a given pair of numbers, could you efficiently find the next pair of numbers to look at? What are the runtime implications of sorting the arrays?

### Hint 3
Start by sorting both arrays, as per Hint #2. Put a pointer at the beginning of both arrays and evaluate the absolute difference of the pointer-numbers. If the difference is equal to zero, then you've found the closest pair; otherwise, increment the pointer of the smaller of the two numbers to find a potentially better pair. Continue until you get a pair with a difference of zero or until one of the pointers gets out of range of its array.

### Optimal Space & Time Complexity
O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first input array and m is the length of the second input array.

## Solution Walkthrough

The solution code can be found in [smallest_difference.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Smallest-Difference/smallest_difference.py).

### Step 1: Define the Function

We'll start by defining our function `smallestDifference` which takes two arrays as input parameters.

### Step 2: Sort Both Arrays

To efficiently find the smallest difference, we first need to sort both arrays in ascending order. Sorting helps us use the two-pointer technique, which will minimize the difference by moving through the arrays in a structured way.

```
    arrayOne.sort()
    arrayTwo.sort()
```

### Step 3: Initialize Variables

We need some variables to keep track of the smallest difference, the current difference, and the pair of numbers with the smallest difference. We'll also use two indices (`idxOne` and `idxTwo`) to traverse through both arrays.

```
    smallest = float('inf')  # This will store the smallest difference we find
    current = float('inf')   # This will store the current difference between two numbers
    smallestPair = []        # This will store the pair with the smallest difference
    idxOne = 0               # Index for arrayOne
    idxTwo = 0               # Index for arrayTwo
```

### Step 4: Use the Two-pointer Technique

We'll use a while loop to traverse both arrays using our two pointers (`idxOne` and `idxTwo`). The loop will continue until we reach the end of either array.

```
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
```

### Step 5: Get the Current Numbers

Inside the loop, we'll get the current numbers from both arrays using our indices.

```
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
```

### Step 6: Calculate the Difference

Next, we'll compare the two numbers and calculate the difference based on their relative sizes. If the first number is smaller, we'll move the pointer in the first array forward. If the second number is smaller, we'll move the pointer in the second array forward. If the numbers are equal, we've found the smallest possible difference (zero), and we can return this pair immediately.

```
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1  # Move the pointer in the first array
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1  # Move the pointer in the second array
        else:
            return [firstNum, secondNum]  # The difference is zero, return the pair
```

### Step 7: Update the Smallest Difference

If the current difference is smaller than our smallest recorded difference, we'll update `smallest` and store the current pair as `smallestPair`.

```
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
```

### Step 8: Return the Result

After the loop completes (one of the arrays is fully traversed), we'll return the pair with the smallest difference.
