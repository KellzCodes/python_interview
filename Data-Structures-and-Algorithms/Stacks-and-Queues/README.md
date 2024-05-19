# Stacks and Queues

## Stack

An array-like data structure whose elements follow the **LIFO** rule: Last In, First Out.

A stack is often compared to a stack of books on a table: the last book that's placed on the stack of books is the first one that's taken off the stack.

The following are a stack's standard operations and their corresponding time complexities:

- **Pushing an element onto the stack:** O(1)
- **Popping an element off the stack:** O(1)
- **Peeking at the element on the top of the stack:** O(1)
- **Searching for an element in the stack:** O(n)

A stack is typically implemented with a **dynamic array** or with a **singly linked list**.

## Queue

An array-like data structure whose elements follow the **FIFO** rule: First In, First Out.

A queue is often compared to a group of people standing in line to purchase items at a store: the first person to get in line is the first one to purchase items and to get out of the queue.

The following are a queue's standard operations and their corresponding time complexities:

- **Enqueuing an element into the queue:** O(1)
- **Dequeuing an element out of the queue:** O(1)
- **Peeking at the element at the front of the queue:** O(1)
- **Searching for an element in the queue:** O(n)

A queue is typically implemented with a **doubly linked list**.

### Inserting or deleting from stack / queue

`O(1)` space and time. 

This is because we are inserting or removing from the beginning or end of a linked list. 

### Searching for an element in a stack / queue

`O(N)` time and `O(1)` space

We have to traverse through N nodes which takes `O(N)` time. There is no additional space used. 

### Storing a stack / queue

`O(N)` space and `O(1)` time

Typically, a stack or queue is initialized as an empty stack and nodes are inserted. Insertions are `O(1)` time. Storing N nodes in a stack or queue will take `O(N)` space.

### Peeking in a stack or queue

`O(1)` space and time.

You are just looking at the first or last element. 