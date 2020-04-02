#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
List 

"""

"""List
The list type is a container that holds a number of other objects, in a given order.
The list type implements the sequence protocol, and also allows you to add and
remove objects from the sequence.

Lists implement all of the common and mutable sequence operations.

Lists may be constructed in several ways:

    Using a pair of square brackets to denote the empty list: []
    Using square brackets, separating items with commas: [a], [a, b, c]
    Using a list comprehension: [x for x in iterable]
    Using the type constructor: list() or list(iterable)

 Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
 
"""

#To create a list, put a number of expressions in square brackets:
L=[]
print(L)

print(list('abc'))
print(list( (1, 2, 3) ) )

"""
You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None.
This is a design principle for all mutable data structures in Python.
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.index('banana'))

"""
Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where 
the last element added is the first element retrieved (“last-in, first-out”). 
To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, 
use pop() without an explicit index.
"""

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

"""
Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
"""
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")  
print(queue.popleft())
queue.popleft()
print(queue.popleft())
print(queue)


