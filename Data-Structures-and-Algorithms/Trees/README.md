# Trees

### Tree

A data structure that consists of nodes, each with some value and pointers to child-nodes, which recursively form **subtrees** in the tree.

The first node in a tree is referred to as the root of the tree, while the nodes at the bottom of a tree (the nodes with no child-nodes) are referred to as leaf nodes or simply leaves. The paths between the root of a tree and its leaves are called branches, and the height of a tree is the length of its longest branch. The depth of a tree node is its distance from its tree's root; this is also known as the node's level in the tree.

A tree is effectively a **graph** that's connected, directed, and acyclic, that has an explicit root node, and whose nodes all have a single parent (except for the root node, which effectively has no parent). Note that in most implementations of trees, tree nodes don't have a pointer to their parent, but they can if desired.

There are many types of trees and tree-like structures, including **binary trees**, **heaps**, and **tries**.

### Binary Tree

A tree whose nodes have up to **two** child-nodes.

The structure of a binary tree is such that many of its operations have a logarithmic time complexity, making the binary tree an incredibly attractive and commonly used data structure.

### K-ary Tree

A tree whose nodes have up to **k** child-nodes. A binary tree is a k-ary tree where **k == 2**.

### Perfect Binary Tree

A binary tree whose interior nodes all have two child-nodes and whose leaf nodes all have the same depth. Example:

```
    1
   / \
  2   3
 / \ / \
4  5 6  7
```

### Complete Binary Tree

A binary tree that's **almost perfect**; its interior nodes all have two child-nodes, but its leaf nodes don't necessarily all have the same depth. Furthermore, the nodes in the last level of a complete binary tree are as far left as possible. Example:

```
            1
           / \
          2   3
         / \ / \
        4  5 6  7
      /  \
     8    9
```

Conversely, the following binary tree *isn't* complete because the nodes in its las level aren't as far left as possible:

```
            1
           / \
          2   3
         / \ / \
        4  5 6  7
           /  \
          8    9
```

### Balanced Binary Tree

A binary tree whose nodes all have left and right **subtrees** whose **heights** differ by no more than 1.

A balanced binary tree is such that the logarithmic time complexity of its operations is maintained.

For example, inserting a node at the bottom of the following **imbalanced** binary tree's left subtree would clearly not be a logarithmic-time operation, since it would involve traversing through most of the tree's nodes:

```
            1
           / \
          2   3
         / 
        4  
       /
      8
     /
    10
```

The following is an example of a balanced binary tree:

```
            1
           / \
          2   3
         / \ / \
        4  5 6  7
       / \     /
      10  9   8
```

### Full Binary Tree

A **binary tree** whose nodes all have either two child-nodes or zero child nodes. Example:

```
            1
           / \
          2   3
             / \
            6   7
           / \     
          8   9   
```

### Storing a tree

`O(N)` space and time where N is the total number of nodes in the tree

### Traversing a tree

`O(N)` time where N is the total number of nodes in the tree. `O(1)` space.

### traversing a binary tree

If you're traversing a binary tree, and at every step of the way you're picking one of the two subtrees to go down.... you will have a time complexity of `O(logN)`