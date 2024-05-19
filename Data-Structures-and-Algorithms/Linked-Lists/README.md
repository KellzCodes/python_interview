# Linked Lists

A linked list is a fundamental data structure in computer science. It consists of nodes where each node contains data and a reference (link) to the next node in the sequence. This allows for dynamic memory allocation and efficient insertion and deletion operations compared to arrays.

## Types of Linked Lists

### Singly Linked List

A data structure that consists of nodes, each with some value and a pointer to the next node in the linked list. A linked list node's value and next node are typically stored in `value` and `next` properties, respectively.

The first node in a linked list is referred to as the head of the linked list, while the last node in a linked list, whose `next` property points to the `null` value, is known as the tail of the linked list.

Below is a visual representation of a singly linked list whose nodes hold integer values:

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> null
```

A singly linked list typically exposes its head to its user for easy access. While finding a node in a singly linked list involves traversing through all of the nodes leading up to the node in question (as opposed to instant access with an array), adding or removing nodes simply involves overwriting `next` pointers (assuming that you have access to the node right before the node that you're adding or removing).

### Doubly Linked List

Similar to a singly linked list, except that each node in a doubly linked list also has a pointer to the previous node in the linked list. The previous node is typically stored in a `prev` property.

Just as the `next` property of a doubly linked list's tail points to the `null` value, so too does the `prev` property of a doubly linked list's head.

Below is a visual representation of a doubly linked list whose nodes hold integer values:

```
null <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 -> null
```

While a doubly linked list typically exposes both its head and tail to its user, as opposed to just its head in the case of a singly linked list, it otherwise behaves very similarly to a singly linked list.

### Circular Linked List

A linked list that has no clear head or tail, because its "tail" points to its "head," effectively forming a closed circle.

A circular linked list can be either a singly circular linked list or a doubly circular linked list.

## Memory

Below is a memory canvas representing 25 memory slots and a linked list. This will be used for example purposes and does not represent actual memory in a system.

Unlike arrays, linked lists do not need contiguous (or back to back) memory slots. 

Linked lists are going to store elements in the list anywhere in memory. They are going to connect the elements using pointers. 

Pointers are this tool that allows you to have one memory slot, let's say memory slot 20, point to another memory slot just by storing the other memory slot's address. You can have memory slot 20 point to memory slot 10 which can pont to memory slot 1 which can point to memory slot 22 and so forth.

Let's look at how a linked list is stored in memory. We would create a structure likely called a "node". Each node in the linked list has both a value (such as 3 or 1) and a pointer to the next node in the linked list. So the first node that has value 3 would have a pointer that points to the next node in the linked list... the node with value 1. 

We would store this in memory by having two back to back memory slots for each node where one memory slot holds the value and the 2nd memory slot holds the pointer. Then the next node in the linked list could be anywhere in the memory canvas. 

So we can put node value 3 at memory slot 21 then have a pointer starting at memory slot 22 (value and pointer have to be back to back) then pointing to memory slot 5. Below, we are using arrows but in memory, the number 5 would be written in binary (101). At memory slot 5, we will store the value 1. Then have a pointer starting at memory slot 6 that points to memory slot 2. Memory slot 2 will store the value 4. Then have a pointer starting at memory slot 3 that points to memory slot 16. Memory slot 16 will store the value 2. Then have a pointer starting at memory slot 17 that points to `null` address.

In memory, there are certain memory addresses that kind of act like the null value or the non-value in coding. They are sort of like memory addresses where if you operating system ever reaches them, it kind of knows that it doesn't have to go anywhere else. Below, we can depict it as an orange 0.

## Complexity

The following are a singly linked list's standard operations and their corresponding time complexities:

- **Accessing the head:** O(1)
- **Accessing the tail:** O(n)
- **Accessing a middle node:** O(n)
- **Inserting / Removing the head:** O(1)
- **Inserting / Removing the tail:** O(n) to access + O(1)
- **Inserting / Removing a middle node:** O(n) to access + O(1)
- **Searching for a value:** O(n)

The following are a doubly linked list's standard operations and their corresponding time complexities:

- **Accessing the head:** O(1)
- **Accessing the tail:** O(1)
- **Accessing a middle node:** O(n)
- **Inserting / Removing the head:** O(1)
- **Inserting / Removing the tail:** O(1)
- **Inserting / Removing a middle node:** O(n) to access + O(1)
- **Searching for a value:** O(n)

### Accessing a middle node

Accessing a middle node runs in `O(N)` time and `O(1)` space.  

You have to start at the first node called the head then traverse the entire linked list until you find the index you are looking for. 

So this will take `O(index)` time. Because you're not storing any additional memory, this will take `O(1)` space. 

### Setting a middle node

Setting a middle node runs in `O(N)` time and `O(1)` space.

Once you find the value at the ith index which takes `O(index)` time, then you can set it instantly by swapping the value for another number. No extra space which would be `O(1)`

There actually isn't really a concept of setting a value in a linked list because that doen't really work. There aren't really indices in linked lists which is why when you implement the linked list you typically don't even have the concept of indices. They are not like arrays. 

### Initializing a linked list

Initializing a linked list runs in `O(N)` time and space. 

You've got a total of 2N memory slots for each node which is `O(2N)` space. Allocating those chunks of memory is going to take `O(N)` time. 

### Copying a linked list

Copying a linked list will run in `O(N)` time and space.

You would have to traverse through the entire linked list of N nodes which will take `O(N)` time. Then you are allocating 2N more memory slots for the copied linked list which will take `O(2N)` space. 

### Traversing a linked list

Traversing a linked list will run in `O(N)` time and `O(1)` space.

When you are traversing, you are not allocating new memory which is why it is `O(1)` space. You are going through all N nodes which takes `O(N)` time. 

### Inserting a node at the beginning

O(1)` time and space.

You create a new head node which will be stored in memory then have its pointer point to the old head. Then you set the head variable equal to the new head. 

This will take `O(1)` time because all we did was create one new node of two memory slots, just shifted a couple of pointers, and overwrote one memory address.  

### Inserting a node in the middle 

`O(N)` to access + `O(1)` time and `O(1)` space.

First we have to traverse through the linked list until we get to the node we want to insert to. This will be an `O(N)` time operation. Then create one new node and shift the pointers. Shifting pointers are `O(1)` time operations. 

If you already have a reference to the node you want to insert to, then it would take `O(1)` time. 

### Inserting a node at the tail

`O(N)` to access + `O(1)` time and `O(1)` space.

First we have to traverse through the linked list until we get to the end. This will be an `O(N)` time operation. Then create one new node and shift the pointers. Shifting pointers are `O(1)` time operations. 

If you already have a reference to the tail, then it would take `O(1)` time. 