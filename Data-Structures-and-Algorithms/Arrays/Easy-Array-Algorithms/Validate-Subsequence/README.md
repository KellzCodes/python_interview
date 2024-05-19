# Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`, and so do the numbers `[2, 4]`. Note that a single number in an array and the array itself are both valid subsequences of the array.

#### Sample Input

```
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

#### Sample Output

```
True
```

## Hints

### Hint 1
You can solve this question by iterating through the main input array once.

### Hint 2
Iterate through the main array, and look for the first integer in the potential subsequence. If you find that integer, keep on iterating through the main array, but now look for the second integer in the potential subsequence. Continue this process until you either find every integer in the potential subsequence or you reach the end of the main array.

### Hint 3
To actually implement what Hint #2 describes, you'll have to declare a variable holding your position in the potential subsequence. At first, this position will be the 0th index in the sequence; as you find the sequence's integers in the main array, you'll increment the position variable until you reach the end of the sequence.

### Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the array

## Solution Walkthrough

We will likely have to traverse both arrays. The question is how?

Because the order of the elements of the sequence and subsequence matters....at the beginning we're really looking for the first element in the potential subsequence.

If we can't find the first element, it doesn't matter if we find the other elements. A subsequence cares about order.

So we're going to initialize a pointer underneath the first element of our subsequence. 

Let's traverse our main array until we find the first element our pointer is pointing to. 

So we're going to put another pointer under the first element in our main array. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/64f1806f-ed11-4cdb-90df-6b129f17906c)

We will iterate through the array until we find the first element from the subsequence. 

When you find the first element in the subsequence, look for the next element. 

So we're going to move the pointer to the next element in the subsequence. 

And we're going to move our pointer in our main array forward. We move forward because we already found the first element. So that means that any future elements we're looking for will be found after this element. 

Once you find all the elements in the subsequence, you can stop the algorithm. Even if there are more elements in the main array. 

The time complexity is `O(N)` time where N is the length of the main array

The space complexity is `O(1)` space because we are not storing anything extra. 
