#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:56:07 2018

@author: star
"""

One of the first cautions programmers encounter when learning Python is the fact
that there are no braces to indicate blocks of code for class and function
definitions or flow control. Blocks of code are denoted by line indentation, which
is rigidly enforced.
The number of spaces in the indentation is variable, but all statements within the
block must be indented with same amount of spaces

Block 1:
if True:
	print "True"
else:
	print "False"

However, the second block in this example will generate an error:

Block 2:
if True:
print "Answer"
print "True"
else:
print "Answer"
print "False"
Thus, in Python all the continuous lines indented with similar number of spaces
would form a block.
Note: Use 4 spaces for indentation as a good programming practice.

"""
Python Indentation

Most of the programming languages like C, C++, Java use braces { } to define a block of code. Python uses indentation.

A code block (body of a function, loop etc.) starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.

Generally four whitespaces are used for indentation and is preferred over tabs. Here is an example.

"""

""" Indentation can be ignored in line continuation. But it's a good idea to always indent. It makes the code more readable. For example:"""

if True:
    print('Hello')
    a = 5



if True: print('Hello'); a = 5

""" both are valid and do the same thing. But the former style is clearer.

Incorrect indentation will result into IndentationError."""


