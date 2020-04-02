#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:30:54 2018

@author: star
"""

"""
array size

We can use len function to determine the size of an array. Let’s look at a simple example for python array length.
"""

arr = ["One", 2, 'Three' ]

arr2d = [[1,2],[1,2,3,4]]

print(len(arr))
print(len(arr2d))
print(len(arr2d[0]))
print(len(arr2d[1]))

"""
Python array slice

Python provide special way to create an array from another array using slice notation. Let’s look at some python array slice examples.
"""

arr = [1,2,3,4,5,6,7]

#python array slice

arr1 = arr[0:3] #start to index 2
print(arr1)

arr1 = arr[2:] #index 2 to end of arr
print(arr1)

arr1 = arr[:3] #start to index 2
print(arr1)

arr1 = arr[:] #copy of whole arr
print(arr1)

arr1 = arr[1:6:2] # from index 1 to index 5 with step 2
print(arr1)

"""
Python array insert

We can insert an element in the array using insert() function.
"""
arr = [1,2,3,4,5,6,7]

arr.insert(3,10)

print(arr)


"""
Python array pop

We can call pop function on array to remove an element from the array at specified index.
"""
arr = [1,2,3,4,5,6,7]

arr.insert(3,10)
print(arr)

arr.pop(3)
print(arr)
