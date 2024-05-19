# Data Structures and Algorithms

## What are data structures?

Data Structures are a way of organizing data so that it can be accessed more efficiently depending upon the situation. Data Structures are fundamentals of any programming language around which a program is built. Python helps to learn the fundamental of these data structures in a simpler way as compared to other programming languages.

## Complexity Analysis

### Complexity Analysis

The process of determining how efficient an algorithm is. Complexity analysis usually involves finding both the **time complexity** and the **space complexity** of an algorithm.

Complexity analysis is effectively used to determine how "good" an algorithm is and whether it's "better" than another one.

### Time Complexity

A measure of how fast an algorithm runs, time complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using **Big O** notation.

### Space Complexity

A measure of how much auxiliary memory an algorithm takes up, space complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using **Big O** notation.

## Memory

### Bit

Short for **binary digit**, a bit is a fundamental unit of information in Computer Science that represents a state with one of two values, typically 0 and 1.

Any data stored in a computer is, at the most basic level, represented in bits.

### Byte

A group of eight bits. For example, `01101000` is a byte.

A single byte can represent up to 256 data values (2^8).

Since a **binary number** is a number expressed with only two symbols, like 0 and 1, a byte can effectively represent all of the numbers between 0 and 255, inclusive, in binary format.

The following bytes represent the numbers 1, 2, 3, and 4 in binary format.

```
1: 00000001
2: 00000010
3: 00000011
4: 00000100
```


### Fixed-Width Integer

An integer represented by a fixed amount of bits. For example, a **32-bit integer** is an integer represented by 32 bits (4 bytes), and a **64-bit integer** is an integer represented by 64 bits (8 bytes).

The following is the 32-bit representation of the number 1, with clearly separated bytes:

```
00000000 00000000 00000000 00000001
```


The following is the 64-bit representation of the number 10, with clearly separated bytes:

```
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00001010
```


Regardless of how large an integer is, its fixed-width-integer representation is, by definition, made up of a constant number of bits.

It follows that, regardless of how large an integer is, an operation performed on its fixed-width-integer representation consists of a constant number of bit manipulations, since the integer is made up of a fixed number of bits.

### Memory

Broadly speaking, memory is the foundational layer of computing, where all data is stored.

In the context of coding interviews, it's important to note the following points:

- Data stored in memory is stored in bytes and, by extension, bits.
- Bytes in memory can "point" to other bytes in memory, so as to store references to other data.
- The amount of memory that a machine has is bounded, making it valuable to limit how much memory an algorithm takes up.
- Accessing a byte or a fixed number of bytes (like 4 bytes or 8 bytes in the case of **32-bit** and **64-bit integers**) is an elementary operation, which can be loosely treated as a single unit of operational work.

## Big O Notation

### Time Complexity

A measure of how fast an algorithm runs, time complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using **Big O** notation.

### Space Complexity

A measure of how much auxiliary memory an algorithm takes up, space complexity is a central concept in the field of algorithms and in coding interviews.

It's expressed using **Big O** notation.

### Big O Notation

The notation used to describe the **time complexity** and **space complexity** of algorithms.

Variables used in Big O notation denote the sizes of inputs to algorithms. For example, **O(n)** might be the time complexity of an algorithm that traverses through an array of length **n**; similarly, **O(n + m)** might be the time complexity of an algorithm that traverses through an array of length **n** and through a string of length **m**.

The following are examples of common complexities and their Big O notations, ordered from fastest to slowest:

- **Constant:** O(1)
- **Logarithmic:** O(log(n))
- **Linear:** O(n)
- **Log-linear:** O(n log(n))
- **Quadratic:** O(n^2)
- **Cubic:** O(n^3)
- **Exponential:** O(2^n)
- **Factorial:** O(n!)

Note that in the context of coding interviews, Big O notation is usually understood to describe the worst-case complexity of an algorithm, even though the **worst-case** complexity might differ from the **average-case** complexity.

For example, some sorting algorithms have different time complexities depending on the layout of elements in their input array. In rare cases, their time complexity will be much worse than in more common cases. Similarly, an algorithm that takes in a string and performs special operations on uppercase characters might have a different time complexity when run on an input string of only uppercase characters vs. on an input string with just a few uppercase characters.

Thus, when describing the time complexity of an algorithm, it can sometimes be helpful to specify whether the time complexity refers to the average case or to the worst case (e.g., "this algorithm runs in O(n log(n)) time on average and in O(n^2) time in the worst case").

## Logarithm

A mathematical concept that's widely used in Computer Science and that's defined by the following equation:

**log<sub>b</sub>(x) = y** if and only if **b<sup>y</sup> = x**

In the context of coding interviews, the logarithm is used to describe the complexity analysis of algorithms, and its usage always implies a logarithm of base **2**. In other words, the logarithm used in the context of coding interviews is defined by the following equation:

**log(n) = y** if and only if **2<sup>y</sup> = n**

In plain English, if an algorithm has a logarithmic time complexity (O(log(n))), where n is the size of the input, then whenever the algorithm's input doubles in size (i.e., whenever n doubles), the number of operations needed to complete the algorithm only increases by one unit. Conversely, an algorithm with a linear time complexity would see its number of operations double if its input size doubled.

As an example, a linear-time-complexity algorithm with an input of size 1,000 might take roughly 1,000 operations to complete, whereas a logarithmic-time-complexity algorithm with the same input would take roughly 10 operations to complete, since **2<sup>10</sup> ≈ 1,000**.

## What is an algorithm?

The word Algorithm means ”A set of finite rules or instructions to be followed in calculations or other problem-solving operations”.

Or

”A procedure for solving a mathematical problem in a finite number of steps that frequently involves recursive operations”.

Therefore, Algorithm refers to a sequence of finite steps to solve a particular problem.

## Use of the Algorithms

Algorithms play a crucial role in various fields and have many applications. Some of the key areas where algorithms are used include:

1. **Computer Science:** Algorithms form the basis of computer programming and are used to solve problems ranging from simple sorting and searching to complex tasks such as artificial intelligence and machine learning.
2. **Mathematics:** Algorithms are used to solve mathematical problems, such as finding the optimal solution to a system of linear equations or finding the shortest path in a graph.
3. **Operations Research:** Algorithms are used to optimize and make decisions in fields such as transportation, logistics, and resource allocation.
4. **Artificial Intelligence:** Algorithms are the foundation of artificial intelligence and machine learning, and are used to develop intelligent systems that can perform tasks such as image recognition, natural language processing, and decision-making.
5. **Data Science:** Algorithms are used to analyze, process, and extract insights from large amounts of data in fields such as marketing, finance, and healthcare.

These are just a few examples of the many applications of algorithms. The use of algorithms is continually expanding as new technologies and fields emerge, making it a vital component of modern society.

## What is the need for algorithms?

1. Algorithms are necessary for solving complex problems efficiently and effectively.
2. They help to automate processes and make them more reliable, faster, and easier to perform.
3. Algorithms also enable computers to perform tasks that would be difficult or impossible for humans to do manually.
4. They are used in various fields such as mathematics, computer science, engineering, finance, and many others to optimize processes, analyze data, make predictions, and provide solutions to problems.

## What are the Characteristics of an Algorithm?

As one would not follow any written instructions to cook the recipe, but only the standard one. Similarly, not all written instructions for programming are an algorithm. For some instructions to be an algorithm, it must have the following characteristics:

- **Clear and Unambiguous:** The algorithm should be unambiguous. Each of its steps should be clear in all aspects and must lead to only one meaning.
- **Well-Defined Inputs:** If an algorithm says to take inputs, it should be well-defined inputs. It may or may not take input.
- **Well-Defined Outputs:** The algorithm must clearly define what output will be yielded and it should be well-defined as well. It should produce at least 1 output.
- **Finite-ness:** The algorithm must be finite, i.e. it should terminate after a finite time.
- **Feasible:** The algorithm must be simple, generic, and practical, such that it can be executed with the available resources. It must not contain some future technology or anything.
- **Language Independent:** The Algorithm designed must be language-independent, i.e. it must be just plain instructions that can be implemented in any language, and yet the output will be the same, as expected.
- **Input:** An algorithm has zero or more inputs. Each that contains a fundamental operator must accept zero or more inputs.
- **Output:** An algorithm produces at least one output. Every instruction that contains a fundamental operator must accept zero or more inputs.
- **Definiteness:** All instructions in an algorithm must be unambiguous, precise, and easy to interpret. By referring to any of the instructions in an algorithm one can clearly understand what is to be done. Every fundamental operator in instruction must be defined without any ambiguity.
- **Finiteness:** An algorithm must terminate after a finite number of steps in all test cases. Every instruction which contains a fundamental operator must be terminated within a finite amount of time. Infinite loops or recursive functions without base conditions do not possess finiteness.
- **Effectiveness:** An algorithm must be developed by using very basic, simple, and feasible operations so that one can trace it out by using just paper and pencil.

## Properties of Algorithm:

- It should terminate after a finite time.
- It should produce at least one output.
- It should take zero or more input.
- It should be deterministic means giving the same output for the same input case.
- Every step in the algorithm must be effective i.e. every step should do some work.

## Types of Algorithms

There are several types of algorithms available. Some important algorithms are:

1. **Brute Force Algorithm:**

   It is the simplest approach to a problem. A brute force algorithm is the first approach that comes to mind when we see a problem.

2. **Recursive Algorithm:**

   A recursive algorithm is based on [recursion](http://www.geeksforgeeks.org/recursion/). In this case, a problem is broken into several sub-parts and called the same function again and again.

3. **Backtracking Algorithm:**

   The backtracking algorithm builds the solution by searching among all possible solutions. Using this algorithm, we keep on building the solution following the failure point, build on the next solution, and continue this process till we find the solution or all possible solutions are looked after.

4. **Searching Algorithm:**

   Searching algorithms are the ones that are used for searching elements or groups of elements from a particular data structure. They can be of different types based on their approach or the data structure in which the element should be found.

5. **Sorting Algorithm:**

   Sorting is arranging a group of data in a particular manner according to the requirement. The algorithms which help in performing this function are called sorting algorithms. Generally, sorting algorithms are used to sort groups of data in an increasing or decreasing manner.

6. **Hashing Algorithm:**

   Hashing algorithms work similarly to the searching algorithm. But they contain an index with a key ID. In hashing, a key is assigned to specific data.

7. **Divide and Conquer Algorithm:**

   This algorithm breaks a problem into sub-problems, solves a single sub-problem, and merges the solutions to get the final solution. It consists of the following three steps:
   - Divide
   - Solve
   - Combine

8. **Greedy Algorithm:**

   In this type of algorithm, the solution is built part by part. The solution for the next part is built based on the immediate benefit of the next part. The one solution that gives the most benefit will be chosen as the solution for the next part.

9. **Dynamic Programming Algorithm:**

   This algorithm uses the concept of using the already found solution to avoid repetitive calculation of the same part of the problem. It divides the problem into smaller overlapping subproblems and solves them.

10. **Randomized Algorithm:**

    In the randomized algorithm, we use a random number so it gives immediate benefit. The random number helps in deciding the expected outcome.

To learn more about the types of algorithms refer to the article about [Types of Algorithms](https://www.geeksforgeeks.org/most-important-type-of-algorithms/).
