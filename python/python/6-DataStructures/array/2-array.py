#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:18:04 2018

@author: star
"""
"""
Traversing 2D-array using for loop

The following code print the elements row wise then the next part prints each element of the given array.
"""

arrayElement2D = [ ["Four", 5, 'Six' ] , [ 'Good',  'Food' , 'Wood'] ]
for i in range(len(arrayElement2D)):
   print(arrayElement2D[i])

for i in range(len(arrayElement2D)):
   for j in range(len(arrayElement2D[i])):
       print(arrayElement2D[i][j])
       
       
# Python array append

arrayElement = ["One", 2, 'Three' ]
arrayElement.append('Four')
arrayElement.append('Five')
for i in range(len(arrayElement)):
   print(arrayElement[i])

# You can also append an array to another array. The following code shows how you can do this.
   # Now our one dimensional array arrayElement turns into a multidimensional array. 

arrayElement = ["One", 2, 'Three' ]
newArray = [ 'Four' , 'Five']
arrayElement.append(newArray);
print(arrayElement)
