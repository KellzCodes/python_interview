# Sorted Squared Array

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

#### Sample Input

```
array = [1, 2, 3, 5, 6, 8, 9]
```

#### Sample Output

```
[1, 4, 9, 25, 36, 64, 81]
```

## Hints

#### Click on the arrows to see the hints

<details>
  <summary><b>Hint 1</b></summary>
While the integers in the input array are sorted in increasing order, their squares won't necessarily be as well, because of the possible presence of negative numbers.
</details>

<details>
  <summary><b>Hint 2</b></summary>
Traverse the array value by value, square each value, and insert the squares into an output array. Then, sort the output array before returning it. Is this the optimal solution?
</details>

<details>
  <summary><b>Hint 3</b></summary>
To reduce the time complexity of the algorithm mentioned in Hint #2, you need to avoid sorting the output array. To do this, as you square the values of the input array, try to directly insert them into their correct position in the output array.
</details>

<details>
  <summary><b>Hint 4</b></summary>
Use two pointers to keep track of the smallest and largest values in the input array. Compare the absolute values of these smallest and largest values, square the larger absolute value, and place the square at the end of the output array, filling it up from right to left. Move the pointers accordingly, and repeat this process until the output array is filled.
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
O(n) time | O(n) space - where n is the length of the input array
</details>

## Solution Walkthrough

This can be solved in linear time because the input array is sorted in ascending order. 

This solution will run in `O(N)` time where N is the number of integers in the array. `O(N)` space where N is the number of integers 

This solution will only work because the array is already sorted.

Let's initialize an empty output array that has a bunch of zeros. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/d064d079-9b7d-4ae8-9a91-09a10eba8bc2)

As we go further left into the negatives of our array and further right into the positives of our array, the squares of the values continue to get larger. 

Let's draw a number line here

![image](https://github.com/KellzCodes/python_interview/assets/19383145/f02751a6-0497-418a-bcc4-0ccb05e57900)

The further right we go from zero and the further left we go from zero, the larger the square values become. 

We can actually look at the absolute value of any of these values to determine which squares are going to be the largest. 

For example, if i'm comparing the integer -3 to and the integer 2 and trying to determine which is going to have a larger square, all I need to do is take the absolute value of these two values. 

I'll see that 3 is larger than two. That means that -3 is going to have a larger square than two. That is because $-3 * -3 = 9$. 

Let's look at the values at the beginning and end of our array

![image](https://github.com/KellzCodes/python_interview/assets/19383145/ade05c76-ede7-4131-b139-7d80bee719ab)

So now we can compare the values at the beginning and end of our array to determine which is larger. That will tell us which position we should be inserting these elements in the array. 

The largest positive value must be at the very end of our array and the largest negative value must be at the very beginning. These are the two values that are kinda gonna be competing for that spot at the very end of our output array to have the largest square. 

If we compare these two values and see the value that is the largest, we can simply take the square of that value and insert it at the end of the array, because we know no value will have a larger square than that. 

Then we can move over to the next element and continue along with the process. 

So you can start by creating two pointers: `start` and `end`

![image](https://github.com/KellzCodes/python_interview/assets/19383145/c5c36582-91ab-4e82-8519-e21fbcb1a268)

We know that these pointers will be at the smallest value and the largest value. We know that one of these two values will be at the end of our output array. The reason we know is because one is the largest positive value and one is the largest negative value. One will have the largest square out of all of the values in this input array. 

We are going to compare these values specifically by their absolute values. Whichever one has the largest absolute value, we'll take its square and insert it at the last position in our output array. 

So we are going to start building our output array from the very end. And the position we want to start at will be `i` which is marked on the diagram below.

![image](https://github.com/KellzCodes/python_interview/assets/19383145/7efaafa3-373c-489c-90e1-9ab850a23eae)

So we compared |-7| to |9|. 9 is larger so we squared it then placed the square at position `i`.

Then we move `i` to the left because we have filled the last position. We also move our `end` pointer to the number 8. We leave the `start` pointer at -7 and start the process again where we compare the `start` and `end` absolute values.

![image](https://github.com/KellzCodes/python_interview/assets/19383145/a894834f-d75a-4478-8796-65e867ab51a4)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/6ef387f1-d75c-4d2e-801f-c93fc01c0c6d)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/c6622b91-e1b1-4cc5-a5b4-37b6e665caaa)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/4bed4dff-b30d-4cd3-8aeb-0975cf5a70f8)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/a16f766a-0bbb-4a8e-a502-65d92bfb4e3d)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/6560874e-8761-42c7-96f1-a4ed530ca22c)

## Brute Force

Brute force solution will run in `O(nlog(n))` time because of sorting method. And `O(N)` space where N is the number of integers in the input array.

## Solution Files

The solutions can be found in [linear_solution.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Sorted-Squared-Array/linear_solution.py) and [brute_force_solution.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Sorted-Squared-Array/brute_force_solution.py).