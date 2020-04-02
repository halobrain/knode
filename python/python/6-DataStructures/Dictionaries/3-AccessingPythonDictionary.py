#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 03:39:04 2018

@author: star
"""

"""
Accessing Python Dictionary

Suppose, you’re not completely sure about dictionary keys or you want to access the dictionary dynamically, you can use loop. In our previous looping technique tutorial we discussed about how help Python For loop is to access elements. Now, the following code will show you how you can access Python Dictionary using loop.

"""

dictionary = {
    'name'  : 'Alex',
    'age'   : 23,
    'sex'   : 'male'
    }

#method1
print('Method1')

#fetch all the keys of that dictionary
key_list = dictionary.keys() #store the key list in key_list

#print to see the keys
print('list of keys')
print(key_list)

#pick key from the key_list
for key in key_list:
    #print the specific value for the key
    print('key = '+key+' value = '+str(dictionary[key]))

#method2
print('\nMethod2')

#pick key from directly from the dictionary
for key in dictionary:
    #print the specific value for the key
    print('key = '+key+' value = '+str(dictionary[key]))