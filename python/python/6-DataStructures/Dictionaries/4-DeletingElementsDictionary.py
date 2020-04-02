#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 03:40:08 2018

@author: star
"""


"""
Deletion of elements in python dictionary is quite easy. You can just use del keyword. 
It will delete single element from Python Dictionary. But if you want to delete all elements from the dictionary. 
You can use clear() function. Deletion of elements from Python Dictionary is shown in the following code:
    
"""

dictionary = {
    'name'  : 'Alex',
    'age'   : 23,
    'sex'   : 'male'
    }

#print initial dictionary
print(dictionary)

#delete a single element
del dictionary['name']
print('After deleting name')
print(dictionary)


'''
you cannot the element which is not int the dictionary. so the below statement
will raise error

del dictionary['name']
'''


#delete all elements from the list
dictionary.clear()
print(dictionary) #this will show an empty dictionary

#delete the entire variable
del dictionary
print(dictionary) #this will produce error