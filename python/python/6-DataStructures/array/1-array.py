#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 03:56:40 2018

@author: star
"""

"""
Python Array contains a sequence of data. Today we will learn about python array and different operations we can perform on array in python. I will assume that you have the basic idea of python variables and 
"""

"""
Python array elements are defined within the brace [] and they are comma separated. The following is an example of declaring python one dimensional array.
Array indexing starts from 0. So value of index 2 of variable arr is 3. 
"""

arr = [ 1, 2 ,3, 4, 5]
print (arr)
print (arr[2])
print (arr[4])

"""
In some other programming languages such as java, when we define an array we also need to define element type, so we are limited to store only that type of data in the array. For example, int brr[5]; is able to store integer data only. 
But python gives us the flexibility to have different type of data in the same array. It’s cool, right? Let’s see an example.
"""

student_marks = ['Akkas' , 45, 36.5]
marks = student_marks[1]+student_marks[2]
print(student_marks[0] + ' has got in total = %d + %f = %f ' % (student_marks[1], student_marks[2], marks ))

"""
In the above example you can see that, student_marks array have three type of data – string, int and float.
"""

"""
Python multidimensional array

Two dimensional array in python can be declared as follows. Similarly we can define three dimensional array or multidimensional array in python.
"""
arr2d = [ [1,3,5] ,[2,4,6] ]
print(arr2d[0]) # prints elements of row 0
print(arr2d[1]) # prints elements of row 1
print(arr2d[1][1]) # prints element of row = 1, column = 1


"""
Python array traversing using for loop

We can use for loop to traverse through elements of an array. Below is a simple example of for loop to traverse through an array.
"""
arrayElement = ["One", 2, 'Three' ]
for i in range(len(arrayElement)):
   print(arrayElement[i])
