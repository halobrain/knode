#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 23:45:45 2018

@author: star
"""

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)