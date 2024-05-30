# Non-Constructible Change

Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you **cannot** create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given `coins = [1, 2, 5]`, the minimum amount of change that you can't create is `4`. If you're given no coins, the minimum amount of change that you can't create is `1`.

#### Sample Input

```
coins = [5, 7, 1, 1, 2, 3, 22]
```

#### Sample Output

```
20
```

## Hints

#### Click the arrows to see the hints

<details>
  <summary><b>Hint 1</b></summary>
One approach to solve this problem is to attempt to create every single amount of change, starting at 1 and going up until you eventually can't create an amount. While this approach works, there is a better one.
</details>

<details>
  <summary><b>Hint 2</b></summary>
Start by sorting the input array. Since you're trying to find the minimum amount of change that you can't create, it makes sense to consider the smallest coins first.
</details>

<details>
  <summary><b>Hint 3</b></summary>
To understand the trick to this problem, consider the following example: `coins = [1, 2, 4]`. With this set of coins, we can create `1, 2, 3, 4, 5, 6, 7` cents worth of change. Now, if we were to add a coin of value `9` to this set, we **would not** be able to create `8` cents. However, if we were to add a coin of value `7`, we **would** be able to create `8` cents, and we would also be able to create all values of change from `1` to `15`. Why is this the case?
</details>

<details>
  <summary><b>Hint 4</b></summary>
Create a variable to store the amount of change that you can currently create up to. Sort all of your coins, and loop through them in ascending order. At every iteration, compare the current coin to the amount of change that you can currently create up to. Here are the two scenarios that you'll encounter:
- The coin value is **greater** than the amount of change that you can currently create plus 1.
- The coin value is **smaller than or equal to** the amount of change that you can currently create plus 1.

In the first scenario, you simply return the current amount of change that you can create plus 1, because you can't create that amount of change. In the second scenario, you add the value of the coin to the amount of change that you can currently create up to, and you continue iterating through the coins. The reason for this is that, if you're in the second scenario, you can create all of the values of change that you can currently create plus the value of the coin that you just considered. If you're given coins `[1, 2]`, then you can make `1, 2, 3` cents. So if you add a coin of value `4`, then you can make `4 + 1` cents, `4 + 2` cents, and `4 + 3` cents. Thus, you can make up to `7` cents.
</details>

<details>
  <summary><b>Optimal Space & Time Complexity</b></summary>
O(nlogn) time | O(1) space - where n is the number of coins
</details>

## Concept Walkthrough

Let's look at an example array

![image](https://github.com/KellzCodes/python_interview/assets/19383145/c6603b69-3796-4361-8e17-319b2faba845)

Let's sort the input array first.

![image](https://github.com/KellzCodes/python_interview/assets/19383145/ca0553e1-757f-455c-8932-5594da4b7f94)

let's create a variable called `change = k`. This going to tell us how much change we can currently create. We can currently make `1 to k` change with the change we already have. So we can make all the values between 1 and k including 1 and k. 

So the idea is to loop through all the coins in ascending order then see how much change we can make with those coins. So we consider one new coin at a time and then compare that to the amount of change we could make previously. 

So let's set `change = 0` and start by iterating our sorted input array. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/bc5851a1-b3fb-41c4-a8da-0d304055b5d2)

At value 1, we can make one cent of change. So we can set `change = 1`. 

Note, if the first value in our sorted input list is not one, that means we can not make one cent worth of change. So we'd just return one because that is the minimum amount of change we cannot create. 

Let's go to the next value which is 1 again. This means we can now make 2 cents. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/a77cd0cd-9a1b-4964-9d42-4719e76d76ab)

The next value is 2. This means we can make 4 cents of change. Actually, this means we can make 1, 2, 3, and 4 cents of change. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/e6077a3e-a76a-4967-8c45-2ba119d0b9dd)

Let's move to the next coins. 

![image](https://github.com/KellzCodes/python_interview/assets/19383145/f8b258bc-8e73-458e-bcf0-1f68c1209265)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/3104945e-2981-4a8b-8c90-5e02603ed492)
![image](https://github.com/KellzCodes/python_interview/assets/19383145/722354d3-ae12-4403-b387-8795003e463f)

Let's move the pointer over once more. Now we are at 22. We can make 41 cents but can we make 20, 21, 22, etc? 

The answer is no. In fact, we cannot make 20 cents. This is because 22 is greater than the amount of change we have plus one. 

If you looked at all the previous coins, notice that when we were adding all of these up, we never had a coin that was greater than the amount of change we previously had plus one. 

## Solution

The solution code can be found in [non_constructible_change.py](https://github.com/KellzCodes/python_interview/blob/main/Data-Structures-and-Algorithms/Arrays/Easy-Array-Algorithms/Non-Constructible-Change/non_constructible_change.py)

The solution will run in `O(nlog(n))` time | `O(1)` space where n is the number of integers in the input array. 

If we have a set of coins and we'll call the set `u`. We are going to start with just one coin in the set: `u = {1}`. We have some `c` value which will stand for the change that we can create with these coins. It will be equal to whatever the second makes: `c = 1`. 

Imagine we have one individual coin called `V = 1` and we add it to the individual set. We can say that if `V` is greater than `c + 1` we cannot make `c + 1` change. 

The equation is $V > c + 1$. This means we cannot make `c + 1` change and we return `c + 1`

If $V <= c + 1$ that mean we can make from `c` plus `V`

So we want to have a set of coins and slowly add one more coin to it as we go through until we eventually reach the one coin that is greater than `change` plus one. If we reach that scenario, we just return `change` plus one. 

Remember, if the coin we add to `change` is less than `change` plus one, we can make all the values up to `change` plus the new coin. 

We will start by sorting the input array in ascending order. Then we loop through on coin at a time, keep track of how much `change` we can currently create, and then check for some coin that we add that is greater than our amount of `change` plus one. Once we find that, we just return the `change` plus one. 

If we were to make it to the very end of our list and never hit the condition where $V > c + 1$, that would mean we cannot make one more than the change we have at the end of the list
