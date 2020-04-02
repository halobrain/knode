#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:29:49 2018

@author: star
"""

"""
Rules for writing identifiers

    Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). Names like myClass, var_1 and print_this_to_screen, all are valid example.
    An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
    Keywords cannot be used as identifiers. 
    
"""
global = 1


""" We cannot use special symbols like !, @, #, $, % etc. in our identifier. """
a@ = 0

"""Identifier can be of any length."""

"""
Things to care about

Python is a case-sensitive language. This means, Variable and variable are not the same. Always name identifiers that make sense.

While, c = 10 is valid. Writing count = 10 would make more sense and it would be easier to figure out what it does even when you look at your code after a long gap.

Multiple words can be separated using an underscore, this_is_a_long_variable.

We can also use camel-case style of writing, i.e., capitalize every first letter of the word except the initial word without any spaces. For example: camelCaseExample

"""