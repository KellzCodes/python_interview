# Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

## Hints

### Hint 1
Using three for loops to calculate the sums of all possible triplets in the array would generate an algorithm that runs in O(n^3) time, where n is the length of the input array. Can you come up with something faster using only two for loops?

### Hint 2
Try sorting the array and traversing it once. At each number, place a left pointer on the number immediately to the right of your current number and a right pointer on the final number in the array. Check if the current number, the left number, and the right number sum up to the target sum. How can you proceed from there, remembering the fact that you sorted the array?

### Hint 3
Since the array is now sorted (see Hint #2), you know that moving the left pointer mentioned in Hint #2 one place to the right will lead to a greater left number and thus a greater sum. Similarly, you know that moving the right pointer one place to the left will lead to a smaller right number and thus a smaller sum. This means that, depending on the size of each triplet's (current number, left number, right number) sum relative to the target sum, you should either move the left pointer, the right pointer, or both to obtain a potentially valid triplet.

### Optimal Space & Time Complexity
O(n^2) time | O(n) space - where n is the length of the input array

## Solution Walkthrough

The solution can be found in [three_number_sum.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Three-Number-Sum/three_number_sum.py).

### Step 1: Sort the Array

```
    array.sort()
```

- Sorting the array helps in using the two-pointer technique to efficiently find the triplets.

### Step 2: Initialize the Result List

```
    triplets = []
```

- This list will store all the triplets that sum up to the `targetSum`.

### Step 3: Iterate Through the Array

```
    for i in range(len(array) - 2):
```

- The main loop runs from the start of the array to the third last element (since we need at least three elements to form a triplet).

### Step 4: Initialize Two Pointers

```
        left = i + 1
        right = len(array) - 1
```

- For each element at index `i`, we initialize two pointers:
  - `left` starts just after `i`.
  - `right` starts at the end of the array.

### Step 5: Check for Triplets

```
        while left < right:
```

- The `while` loop runs as long as the `left` pointer is before the `right` pointer.

#### Calculate the Current Sum

```
            currentSum = array[i] + array[left] + array[right]
```

- Compute the sum of the elements at indices `i`, `left`, and `right`.

### Step 6: Compare the Current Sum with the Target Sum

```
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
```

- If `currentSum` equals `targetSum`:
  - Add the triplet to the `triplets` list.
  - Move the `left` pointer to the right and the `right` pointer to the left to look for new pairs.
- If `currentSum` is less than `targetSum`:
  - Increment the `left` pointer to increase the sum.
- If `currentSum` is greater than `targetSum`:
  - Decrement the `right` pointer to decrease the sum.

### Step 7: Return the Result List

```
    return triplets
```

- Finally, return the list of all found triplets.

### Example Walkthrough

Consider the array `[1, 2, 3, 4, 5, 6]` and the target sum `10`:

1. **Sort the Array**: `[1, 2, 3, 4, 5, 6]`
2. **Iterate through the Array**:
- For `i = 0` (`array[i] = 1`):
  - `left = 1`, `right = 5`
  - `currentSum = 1 + 2 + 6 = 9` (less than 10, move `left` to 2)
  - `currentSum = 1 + 3 + 6 = 10` (equal to 10, add `[1, 3, 6]` to `triplets`)
  - Move `left` to 3, `right` to 4
  - `currentSum = 1 + 4 + 5 = 10` (equal to 10, add `[1, 4, 5]` to `triplets`)
  - For `i = 1` (`array[i] = 2`):
    - `left = 2`, `right = 5`
    - `currentSum = 2 + 3 + 6 = 11` (greater than 10, move `right` to 4)
    - `currentSum = 2 + 3 + 5 = 10` (equal to 10, add `[2, 3, 5]` to `triplets`)
- For `i = 2` (`array[i] = 3`):
    - `left = 3`, `right = 5`
    - `currentSum = 3 + 4 + 6 = 13` (greater than 10, move `right` to 4)
    - `currentSum = 3 + 4 + 5 = 12` (greater than 10, move `right` to 3)

Output: [[1, 3, 6], [1, 4, 5], [2, 3, 5]]