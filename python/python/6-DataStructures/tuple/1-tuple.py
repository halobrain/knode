#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:01:46 2018

@author: star
"""

"""
Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

class tuple([iterable])

    Tuples may be constructed in a number of ways:

        Using a pair of parentheses to denote the empty tuple: ()
        Using a trailing comma for a singleton tuple: a, or (a,)
        Separating items with commas: a, b, c or (a, b, c)
        Using the tuple() built-in: tuple() or tuple(iterable)

Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples)

"""

t = 12345, 54321, 'hello!'
print(t)
t[0] = 88888 # Tuples are immutable , we will get error

v = ([1, 2, 3], [3, 2, 1]) # but they can contain mutable objects:
print(v)

x, y, z = t1
print(t1)