# Move Element To End

You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

## Hints

<details>
  <summary><b>Hint 1</b></summary>
Don't overcomplicate this problem. How would you solve it by hand? Consider that approach, and try to translate it into code.
</details>

<details>
  <summary><b>Hint 2</b></summary>
In view of Hint #1, you can solve this problem without sorting the input array. Try setting two pointers at the start and end of the array, respectively, and progressively moving them inwards.
</details>

<details>
  <summary><b>Hint 3</b></summary>
Following Hint #2, set two pointers at the start and end of the array, respectively. Move the right pointer inwards so long as it points to the integer to move, and move the left pointer inwards so long as it doesn't point to the integer to move. When both pointers aren't moving, swap their values in place. Repeat this process until the pointers pass each other.
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
O(n) time | O(1) space - where n is the length of the array
</details>

## Solution Walkthrough

The solution code can be found in [move_element_to_end.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Medium-Array-Algorithms/Move-Element-To-End/move_element_to_end.py).

### Step 1: Define the Function

We'll start by defining our function moveElementToEnd which takes an array and the element to move as input parameters.

```
def moveElementToEnd(array, toMove):
```

### Step 2: Initialize Pointers

We'll use two pointers: `left` starting at the beginning of the array and `right` starting at the end of the array.

```
    left = 0
    right = len(array) - 1
```

### Step 3: Use the Two-pointer Technique

We'll use a while loop to traverse the array with our two pointers. The loop will continue while the `left` pointer is less than the `right` pointer.

```
    while left < right:
```

### Step 4: Move the Right Pointer

Inside the loop, we'll move the `right` pointer leftwards while it points to the element `toMove`. This ensures that when we find an element to move at the `left` pointer, we have a valid position at the `right` pointer to swap it with.

```
        while left < right and array[right] == toMove:
            right -= 1
```

### Step 5: Swap Elements

If the element at the `left` pointer is the element to move, we'll swap it with the element at the `right` pointer. After the swap, we move the `left` pointer to the right.

```
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        
        left += 1
```

### Step 6: Return the Modified Array

After the loop completes, we return the modified array.

```
    return array
```

### Explanation

1. **Initialize Pointers**: We start with `left` at the beginning and `right` at the end of the array.
2. **Move Right Pointer**: The inner `while` loop moves the `right` pointer leftwards until it points to an element that is not `toMove`.
3. **Swap Elements**: If `array[left]` is `toMove`, we swap it with `array[right]` and then move the `left` pointer to the right.
4. **Continue Loop**: The loop continues until the `left` pointer is no longer less than the `right` pointer.
5. **Return the Result**: We return the modified array with all instances of `toMove` moved to the end.
