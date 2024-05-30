# Longest Peak

Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers `[1, 4, 10, 2]` form a peak, but the integers `[4, 0, 10]` don't and neither do the integers `[1, 2, 2, 0]`. Similarly, the integers `[1, 2, 3]` don't form a peak because there aren't any strictly decreasing integers after the `[3]`.

#### Sample Input

```
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3] 
```

#### Sample Output

```
6  # 0, 10, 6, 5, -1, -3
```

## Hints

#### Click the arrows to see the hints

<details>
  <summary><b>Hint 1</b></summary>

You can solve this question by iterating through the array from left to right once.

</details>

<details>
  <summary><b>Hint 2</b></summary>

Iterate through the array from left to right, and treat every integer as the potential tip of a peak. To be the tip of a peak, an integer has to be strictly greater than its adjacent integers. What can you do when you find an actual tip?

</details>

<details>
  <summary><b>Hint 3</b></summary>

As you iterate through the array from left to right, whenever you find a tip of a peak, expand outwards from the tip until you no longer have a peak. Given what peaks look like and how many peaks can therefore fit in an array, realize that this process results in a linear-time algorithm. Make sure to keep track of the longest peak you find as you iterate through the array.

</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>

O(n) time | O(1) space - where n is the length of the input array

</details>

## Solution Walkthrough

The solution code can be found in [longest_peak.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Longest-Peak/longest_peak.py).

### Step 1: Define the Function

We'll start by defining our function `longestPeak` which takes an array as an input parameter.

```
def longestPeak(array):
```

### Step 2: Initialize Variables

We need a variable `longestPeakLength` to keep track of the longest peak length found so far. We'll also use a variable `i` to iterate through the array, starting from the second element.

```
    longestPeakLength = 0
    i = 1
```

### Step 3: Traverse the Array

We'll use a while loop to traverse the array. The loop will continue until `i` is less than the length of the array minus one (to ensure there are elements on both sides of the current element).

```
    while i < len(array) - 1:
```

### Step 4: Check for Peak

Inside the loop, we'll check if the current element is a peak. An element is a peak if it is greater than both its left and right neighbors.

```
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
```

### Step 5: Skip Non-Peak Elements

If the current element is not a peak, we increment `i` and continue to the next iteration.

```
        if not isPeak:
            i += 1
            continue
```

### Step 6: Expand to the Left

If the current element is a peak, we'll expand to the left to find the length of the peak. We use a variable `left` starting two positions to the left of `i` and move leftwards as long as the elements are increasing.

```
        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
```

### Step 7: Expand to the Right

Similarly, we'll expand to the right to find the length of the peak. We use a variable `right` starting two positions to the right of `i` and move rightwards as long as the elements are decreasing.

```
        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1
```

### Step 8: Calculate Peak Length

We calculate the length of the current peak by subtracting `left` from `right` and subtracting one. We update `longestPeakLength` if the current peak length is longer.

```
        currentPeakLength = right - left - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
```

### Step 9: Move to the Next Potential Peak

To avoid rechecking elements of the current peak, we set `i` to `right`.

```
        i = right
```

### Step 10: Return the Result

After the loop completes, we return the `longestPeakLength`.

```
    return longestPeakLength
```

### Explanation

1. **Initialize Variables**: We set up variables to keep track of the longest peak length and the current index.
2. **Traverse the Array**: We iterate through the array using a while loop.
3. **Check for Peak**: We check if the current element is a peak.
4. **Expand to the Left and Right**: If it is a peak, we expand left and right to find the length of the peak.
5. **Calculate and Update Peak Length**: We calculate the length of the current peak and update the longest peak length if necessary.
6. **Move to the Next Potential Peak**: We move the index to the end of the current peak to avoid rechecking elements.

