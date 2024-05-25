# Spiral Traverse

Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

#### Sample Input

```
array = [
    [1, 2, 3, 4], 
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
```

#### Sample Output

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Hints

**Hint 1**

You can think of the spiral that you have to traverse as a set of rectangle perimeters that progressively get smaller (i.e., that progressively move inwards in the two-dimensional array).

**Hint 2**

Going off of Hint #1, declare four variables: a starting row, a starting column, an ending row, and an ending column. These four variables represent the bounds of the first rectangle perimeter in the spiral that you have to traverse. Traverse that perimeter using those bounds, and then move the bounds inwards. End your algorithm once the starting row passes the ending row or the starting column passes the ending column.

**Hint 3**

You can solve this problem both iteratively and recursively following very similar logic.

**Optimal Space & Time Complexity**

O(n) time | O(n) space - where n is the total number of elements in the array.

## Solution Walkthrough

The recursive solution can be found in [spiral_traverse_recursive.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Spiral-Traverse/spiral_traverse_recursive.py).

The iterative solution can be found in [spiral_traverse_iterative.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Spiral-Traverse/spiral_traverse_iterative.py).

### Step 1: Define the Function

We'll start by defining our function spiralTraverse which takes a 2D array as an input parameter.

```
def spiralTraverse(array):
```

### Step 2: Initialize Variables

We need a list `result` to store the elements in spiral order. We'll also define variables to keep track of the boundaries of the current layer of the spiral: `startRow`, `endRow`, `startCol`, and `endCol`.

```
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1
```


### Step 3: Traverse the Array in Spiral Order

We'll use a while loop to traverse the array in spiral order. The loop will continue until `startRow` is greater than `endRow` or `startCol` is greater than `endCol`.

```
    while startRow <= endRow and startCol <= endCol:
```

### Step 4: Traverse the Top Row

We'll traverse the top row from left to right.

```
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
```

### Step 5: Traverse the Right Column

We'll traverse the right column from top to bottom.

```
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
```

### Step 6: Traverse the Bottom Row

We'll traverse the bottom row from right to left, if there are multiple rows remaining.

```
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])
```

### Step 7: Traverse the Left Column

We'll traverse the left column from bottom to top, if there are multiple columns remaining.

```
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])
```

### Step 8: Move Inward to the Next Layer

We'll move the boundaries inward to the next layer of the spiral.

```
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
```

### Step 9: Return the Result

After the loop completes, we return the `result` list.

```
    return result
```

### Explanation

1. **Initialize Variables**: We set up our result list and define the boundaries of the current spiral layer.
2. **Traverse Top Row**: We move from the left boundary to the right boundary of the top row.
3. **Traverse Right Column**: We move from the top boundary to the bottom boundary of the right column.
4. **Traverse Bottom Row**: We move from the right boundary to the left boundary of the bottom row, if there are multiple rows.
5. **Traverse Left Column**: We move from the bottom boundary to the top boundary of the left column, if there are multiple columns.
6. **Move Inward**: We adjust our boundaries to move inward to the next layer of the spiral.
7. **Return Result**: We return the list of elements collected in spiral order.
