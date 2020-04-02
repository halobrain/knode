#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:56:38 2018

@author: star
"""

Statements in Python typically end with a new line. Python does, however, allow
the use of the line continuation character (\) to denote that the line should
continue. For example:

total = first_one + \
second_two + \
third_three
print(total)

Statements contained within the [], {} or () brackets do not need to use the line
continuation character. For example:
days = ['Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday']
print(days)
