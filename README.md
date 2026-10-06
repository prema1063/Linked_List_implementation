# Linked List Implementations

This repository contains basic implementations of Linked Lists and
data structures built using Linked Lists in Python.

## Implementations

### 1. Doubly Linked List

A basic Doubly Linked List implementation where each node contains
references to both the previous and next nodes.

Operations implemented:

- Insert at head
- Insert at tail
- Delete by value
- Search
- Display
- Track size

### 2. Stack Using Linked List

A Stack implementation using Linked List nodes.

Operations implemented:

- Push
- Pop
- Peek

The stack follows the LIFO (Last In, First Out) principle.

### 3. LRU Cache Using Linked List

An LRU (Least Recently Used) Cache implemented using:

- Doubly Linked List
- HashMap

The HashMap provides fast access to nodes, while the Doubly Linked
List maintains the order of recently used elements.

With a HashMap:
Key → Node → O(1) average

2. Doubly Linked List → Maintain usage order
An LRU Cache needs to know:
- Which item was recently used
- Which item was least recently used
The Doubly Linked List maintains that order.

When an item is accessed, you can remove it from its current position and move it to the front. When the cache is full, you remove the node at the tail. Your code does exactly this through remove_node() and add_to_head().   LRU_CACHE_using_Linked_list   LRU_CACHE_using_Linked_list
Why not use only one?
Only HashMap:
Fast lookup, but it doesn't give you the usage order you need for LRU eviction.
Only Linked List:
Can maintain usage order, but finding a key requires traversal → O(n).

So the combination is:
HashMap = Find the node quickly
Doubly Linked List = Move, reorder, and remove nodes quickly

Together, they give the LRU Cache O(1) average get() and put() operations.


Operations implemented:

- Get
- Put
- Add node
- Remove node
- Display cache

## Concepts Covered

- Nodes
- Head and Tail
- Previous and Next pointers
- Traversal
- Insertion
- Deletion
- Searching
- Stack using Linked List
- LRU Cache
- HashMap + Doubly Linked List

## Files

| File | Description |
|------|-------------|
| `Linked_List.py` | Basic Doubly Linked List |
| `stack_using_LL.py` | Stack implemented using Linked List |
| `LRU_CACHE_using_Linked_list.py` | LRU Cache using Linked List and HashMap |
