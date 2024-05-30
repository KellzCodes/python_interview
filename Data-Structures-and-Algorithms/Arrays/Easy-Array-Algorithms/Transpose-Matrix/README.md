# Transpose Matrix

You're given a 2D array of integers `matrix`. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

#### Sample Input #1 

```
matrix = [
    [1, 2]
]
```

#### Sample Output #1

```
[
    [1],
    [2]
]
```

#### Sample Input #2

```
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

#### Sample Output #2

```
[
    [1, 3, 5]
    [2, 4, 6]
]
```

#### Sample Input #3

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

#### Sample Output #3

```
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

## Hints

#### Click the arrow to see the hints

<details>
  <summary><b>Hint 1</b></summary> 
The row and column indices of each entry in the matrix should be flipped. For example, the value at `matrix[1][2]` will be at `matrix[2][1]` in the transpose of the matrix.
</details>

<details>
  <summary><b>Hint 2</b></summary>  
Each column in the matrix should become a row in the transpose of the matrix. Each row in the matrix should become a column in the transpose of the matrix.
</details>

<details>
  <summary><b>Hint 3</b></summary>  
Try iterating one column at a time, and with each column, create a row of the values to add to the transpose of the matrix.
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
O(w * h) time | O(w * h) space - where w is the width of the matrix and h is the height
</details>

## Solution Walkthrough

The solution code can be found in [transpose_matrix.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Transpose-Matrix/transpose_matrix.py)

The function `transposeMatrix(matrix)` takes a 2D list (matrix) as input and returns its transpose. The transpose of a matrix is obtained by swapping its rows and columns. Here's a detailed breakdown of the function:

1. Initialize the Transposed Matrix:
    ```
   transposed = []
   ```
   An empty list `transposed` is initialized to store the transposed matrix.


2. Iterate Over Columns of the Original Matrix:
    ```
   for col in range(len(matrix[0])):
   ```
   The outer loop iterates over each column index of the original matrix. `len(matrix[0])` gives the number of columns in the original matrix.


3. Create a New Row for the Transposed Matrix:
    ```
   new_row = []
   ```
   For each column in the original matrix, a new empty list `new_row` is initialized. This new row will represent a column in the original matrix.


4. Iterate Over Rows of the Original Matrix:

    ```
   for row in range(len(matrix)):
   ```
   The inner loop iterates over each row index of the original matrix. `len(matrix)` gives the number of rows in the original matrix.


5. Append the Element to the New Row:

    ```
   new_row.append(matrix[row][col])
   ```
   Within the inner loop, the element at position `[row][col]` in the original matrix is appended to `new_row`.


6. Append the New Row to the Transposed Matrix:

    ```
   transposed.append(new_row)
   ```
   After the inner loop completes (meaning all elements in the current column of the original matrix are added to `new_row`), `new_row` is appended to the transposed list.


7. Return the Transposed Matrix:

    ```
   return transposed
   ```
   Finally, the transposed matrix, which now contains the rows and columns swapped, is returned.

### Example

Let's see an example to understand how this works:

**Input Matrix:**

```
1 2 3
4 5 6
```

**Steps:**

1. Initialize `transposed` as `[]`.
2. For `col = 0`:
    - Initialize `new_row` as `[]`.
    - For `row = 0`, append `matrix[0][0]` (which is `1`) to `new_row`. `new_row` becomes `[1]`.
    - For `row = 1`, append `matrix[1][0]` (which is `4`) to `new_row`. `new_row` becomes `[1, 4]`.
    - Append `new_row` (`[1, 4]`) to `transposed`. `transposed` becomes `[[1, 4]]`.
3. For `col = 1`:
    - Initialize `new_row` as `[]`.
    - For `row = 0`, append `matrix[0][1]` (which is `2`) to `new_row`. `new_row` becomes `[2]`.
    - For `row = 1`, append `matrix[1][1]` (which is `5`) to `new_row`. `new_row` becomes `[2, 5]`.
    - Append `new_row` (`[2, 5]`) to `transposed`. `transposed` becomes `[[1, 4], [2, 5]]`.
4. For `col = 2`:
    - Initialize `new_row` as `[]`.
    - For `row = 0`, append `matrix[0][2]` (which is `3`) to `new_row`. `new_row` becomes `[3]`.
    - For `row = 1`, append `matrix[1][2]` (which is `6`) to `new_row`. `new_row` becomes `[3, 6]`.
    - Append `new_row` (`[3, 6]`) to `transposed`. `transposed` becomes `[[1, 4], [2, 5], [3, 6]]`.

**Output Transposed Matrix**

```
1 4
2 5
3 6
```

### Summary

The function `transposeMatrix` iterates over the columns of the original matrix and constructs the rows of the transposed matrix by iterating over the rows of the original matrix. This results in a new matrix where the rows and columns are swapped.
