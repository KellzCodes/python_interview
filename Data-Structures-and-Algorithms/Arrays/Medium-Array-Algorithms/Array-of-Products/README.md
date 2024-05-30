# Array Of Products

Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at `output[i]` is equal to the product of every number in the input array other than `input[i]`.

Note that you're expected to solve this problem without using division.

## Hints

#### Click the arrows to see each hint

<details>
  <summary><b>Hint 1</b></summary>
    Think about the most naive approach to solving this problem. How can we do exactly what the problem wants us to do without focusing at all on time and space complexity?
</details>

<details>
  <summary><b>Hint 2</b></summary>
    Understand how `output[i]` is being calculated. How can we calculate the product of every element other than the one at the current index? Can we do this with just one loop through the input array, or do we have to do multiple loops?
</details>

<details>
  <summary><b>Hint 3</b></summary>
    For each index in the input array, try calculating the product of every element to the left and the product of every element to the right. You can do this with two loops through the array: one from left to right and one from right to left. How can these products help us?
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
    O(n) time | O(n) space - where n is the length of the input array
</details>

# Solution Walkthrough

## Brute Force Solution

The brute force solution code can be found in [array_of_products_brute.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Array-of-Products/array_of_products_brute.py).

### Step 1: Define the Function

We'll start by defining our function `arrayOfProducts` which takes an array as an input parameter.

```
def arrayOfProducts(array):
```

### Step 2: Initialize the Products Array
We need an array products to store the result. Initially, we'll set each element to 1.

```
    products = [1 for _ in array]
```

### Step 3: Nested Loop to Calculate Products

We'll use two nested loops. The outer loop iterates through each element of the array, while the inner loop calculates the product of all elements except the current one.

```
    for i in range(len(array)):
        runningProduct = 1

        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]

        products[i] = runningProduct
```

#### Detailed Breakdown

1. **Outer Loop**:
- The outer loop runs from `i = 0` to `i = len(array) - 1`.

2. Inner Loop:
- The inner loop runs from `j = 0` to `j = len(array) - 1`.
- If `i` is not equal to `j`, we multiply `runningProduct` by `array[j]`.

3. Assign Product:
- After the inner loop completes, `runningProduct` contains the product of all elements except `array[i]`.
- We assign this value to `products[i]`.

### Step 4: Return the Result

After both loops complete, we return the `products` array.

```
    return products
```

### Time and Space Complexity

O(n^2) time | O(n) space - where n is the length of the input array


## Optimal Solution

The solution code can be found in [array_of_products.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Array-of-Products/array_of_products.py).

### Step 1: Define the Function

We'll start by defining our function `arrayOfProducts` which takes an array as an input parameter.

```
def arrayOfProducts(array):
```

### Step 2: Initialize the Products Array

We need an array `products` to store the result. Initially, we'll set each element to `1`.

```
    products = [1 for _ in array]
```

### Step 3: Calculate the Left Running Product

We'll use a variable `leftRunningProduct` to keep track of the product of all elements to the left of the current element. We'll iterate through the array from left to right, updating `products` and `leftRunningProduct` as we go.

```
    leftRunningProduct = 1
    
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]
```

### Step 4: Calculate the Right Running Product

Similarly, we'll use a variable `rightRunningProduct` to keep track of the product of all elements to the right of the current element. We'll iterate through the array from right to left, updating products and `rightRunningProduct` as we go.

```
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]
```

### Step 5: Return the Result

After the loops complete, we return the `products` array.

```
    return products
```

### Example Usage

Let's use the function to calculate the array of products for `[1, 2, 3, 4]`.

```
array = [1, 2, 3, 4]
print(arrayOfProducts(array))
```

When you run this code, it will print `[24, 12, 8, 6]` because:

- The product of all elements except `1` is `2 * 3 * 4 = 24`.
- The product of all elements except `2` is `1 * 3 * 4 = 12`.
- The product of all elements except `3` is `1 * 2 * 4 = 8`.
- The product of all elements except `4` is `1 * 2 * 3 = 6`.

