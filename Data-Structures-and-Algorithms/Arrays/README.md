# Arrays

## Array

A linear collection of data values that are accessible at numbered indices, starting at index 0.

A static array is an implementation of an array that allocates a fixed amount of memory to be used for storing the array's values. Appending values to the array therefore involves copying the entire array and allocating new memory for it, accounting for the extra space needed for the newly appended value. This is a linear-time operation.

A dynamic array is an implementation of an array that preemptively allocates double the amount of memory needed to store the array's values. Appending values to the array is a constant-time operation until the allocated memory is filled up, at which point the array is copied and double the memory is once again allocated for it. This implementation leads to an amortized constant-time insertion-at-end operation.

A lot of popular programming languages like JavaScript and Python implement arrays as dynamic arrays.

## Memory

Below is a memory canvas that represents 35 slots of memory that will be used for example purposes

Each slot holds 1 byte which is 8 bits. 

Let's say we want to make a list that has 3 integers like [1, 2, 3]....

Our operating system would transform all 3 integers into their binary number format. For the purpose of this example, we will use 64 bit integers. 

Our operating system will go into the memory canvas and find a series of back to back memory slots that are free and have enough space to allocate or hold three integers.

If the integers are 64 bit integers, they each take 8 bytes or 8 memory slots.  So we need $8 * 3 = 24$ memory slots back to back that don't have anything in them. 

The number of memory slots, which is directly linked to the length of the array, is fixed. 

## Complexity

The following are an array's standard operations and their corresponding time complexities:

- **Accessing a value at a given index:** O(1)
- **Updating a value at a given index:** O(1)
- **Inserting a value at the beginning:** O(n)
- **Inserting a value in the middle:** O(n)
- **Inserting a value at the end:**
  - amortized O(1) when dealing with a **dynamic array**
  - O(n) when dealing with a **static array**
- **Removing a value at the beginning:** O(n)
- **Removing a value in the middle:** O(n)
- **Removing a value at the end:** O(1)
- **Copying the array:** O(n)

### Accessing a value at a given index

Accessing (or getting) an array index is a very basic operation that is performed almost instantly. 

Instant means that it runs in constant time and space which is denoted as `O(1)`.

It never changes regardless of how big your array is. 

When the operating system stored our array, it knew which memory address it started at. Similarly, it knew the array was a fixed width, 64-bit integer. Fixed with implies it never changes, which further implies it is a constant.

We know that every integer in this array has 8 memory slots allocated to it and where each integer begins in memory. So if the first integer starts at memory slot 3, the second integer starts at memory slot $3 + 8$ (which is 11), and the third integer starts at memory slot $3 + 16$ (which is 19).

When we are accessing an element in an array at a given index, our operating system is finding the memory address that starts the array, finding how many bytes or memory slots one element takes up, and then finds the index specified. 

### Updating a value at a given index

Updating (or setting) an array at an index runs in constant time and space: `O(1)`

Overwriting an element is an elementary operation. We do not use any extra memory because we are using the same memory we already had. 

### Initialize an array

Initializing the array will run in `O(N)` time and space.

First we specify the length $N$. Then the operating system found $N * 8$ memory slots that are free and back to back. This will run in `O(8N)` which is just `O(N)` for coding interviews. 

The array will have a size $N$. As $N$ increases, the time it takes to initialize array (the number of elementary operations) increases linearly with respect to $N$.

This will be `O(N)` space because you are taking $8 * N$ memory slots. 

### Traversing through an array

Traversing through an array will run in `O(N)` time and `O(1)` space. 

When you do a `for-loop` through an array, you are traversing through every element in the array. This means the operating system will traverse through $8 * N$ memory slots. So this will take `O(8N)` which is `O(N)` time.

Any built-in array methods that traverse through the array will be `O(N)` time, assuming you're not doing any auxillary operations. 

This is `O(1)` space because we are not using any extra space to traverse through the array.

### Copy an array

Copying an array will run in `O(N)` space and time. 

When you're copying an array, you're traversing the entire array and having the operating system find new space in memory. 

So you are traversing `O(N)` then allocating another $N$ memory blocks. So that is `O(N)` time and space. 

### Inserting a value in an array 

Inserting a value will run in `O(N)` time and `O(1)`space for static arrays. 

Inserting a value in a static array will cause a shift in other elements in the array. The problem is we haven not allocated anymore memory because the array is static and thus a fixed length. So there could be something stored in the memory slots right after the array. 

The option we have is to copy the array then tell the operating system to find the exact number of memory slots needed to store the new array plus the new element(s). Then the OS will free up all the space that was held by the original array. 

Copying is an `O(N)` time operation. Since we freed up all the space from the old array, this will be `O(1)` space.

### Inserting a value at the end of a dynamic array. 

Inserting a value at the end of a dynamic array will run in amortized `O(1)` time and space. 

Dynamic arrays will allow you to have faster insertion.

The dynamic array will allocate twice as much space as you asked for. So you can freely append or insert elements in a dynamic array

Once you exhaust the amount of space you've been allocated, only then does the insertion cause a copy of the array....then you get a new array with double the space you need. 

We keep doubling the array at $1 + 2 + 4 + 8 + N$. This means the doubling of the dynamic array runs at `O(2N)` which is just `O(N)`.

Every time you double the array, you get more and more `O(1)` insertions. This is enough to cancel out the `O(N)` operations.

To insert an element in the middle or the beginning of a dynamic array will take an `O(N)` operation because you will have to shift other elements. 

### Popping values out of the end of an array

Popping is `O(1)` space and time. 

Popping means removing a value at the end of an array. So you just free up the last memory slot. 

### Removing values from the beginning or middle of an array

Removing an element from the beginning or middle of an array is an `O(N)` operation because it causes a shift in the other elements.