#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:13:26 2018

@author: star
"""

"""
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set()

"""
a = set('abracadabra')
b = set('alacazam')

print(a)      # unique letters in a

print(a-b)  # letters in a but not in b

print(a | b)    # letters in either a or b

print(a & b)    # letters in both a and b

print(a ^ b)    # letters in a or b but not both

"""
A set is a dictionary with no values. It has only unique keys. Its syntax is similar
to that for a dictionary. But we omit the values,and can use complex,powerful set
logic.
"""
"""
General syntax for set creation is as follows:
set1={'a','b','c'}
We can also create a set using set() function by providing parameters as list.
Example:
set1=set([1,2])
Note : Use set() operator for creating empty set ,variable with empty {} will be
considered as a dictionary.
"""

