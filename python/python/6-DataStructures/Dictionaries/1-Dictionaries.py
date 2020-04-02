#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:22:35 2018

@author: star
"""

"""
A dictionary is mutable and is another container type that can store any number
of Python objects, including other container types. Dictionaries consist of pairs
(called items) of keys and their corresponding values.
Python dictionaries are also known as associative arrays or hash tables. The
general notation of a dictionary is as follows:
diction = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
The things on left side of “:” are keys and right side are values.

Note:
Keys of a particular dictionary are unique while values may not be.
The values of a dictionary can be of any type, but the keys must be of an
immutable data type such as strings, numbers, or tuples.



"""

d={1:'one',2:'two',3:'three',4:'four'}

print(d)

print(d.keys())

print(d.values())
