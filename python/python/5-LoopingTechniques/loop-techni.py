#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:40:12 2018

@author: star
"""
"""

Compound statements

Compound statements contain (groups of) other statements; they affect or control the execution of those other statements in some way. In general, compound statements span multiple lines, although in simple incarnations a whole compound statement may be contained in one line.




The if, while and for statements implement traditional control flow constructs. try specifies exception handlers and/or cleanup code for a group of statements, while the with statement allows the execution of initialization and finalization code around a block of code. Function and class definitions are also syntactically compound statements.

A compound statement consists of one or more ‘clauses.’ A clause consists of a header and a ‘suite.’ 
The clause headers of a particular compound statement are all at the same indentation level. 
Each clause header begins with a uniquely identifying keyword and ends with a colon. 
A suite is a group of statements controlled by a clause. 
A suite can be one or more semicolon-separated simple statements on the same line as the header, following the header’s colon,
 or it can be one or more indented statements on subsequent lines. 
 
 Only the latter form of a suite can contain nested compound statements; the following is illegal, 
 mostly because it wouldn’t be clear to which if clause a following else clause would belong:
    

if test1: if test2: print(x)

Also note that the semicolon binds tighter than the colon in this context, so that in the following example, either all or none of the print() calls are executed:

if x < y < z: print(x); print(y); print(z)

Summarizing:

compound_stmt ::=  if_stmt
                   | while_stmt
                   | for_stmt
                   | try_stmt
                   | with_stmt
                   | funcdef
                   | classdef
                   | async_with_stmt
                   | async_for_stmt
                   | async_funcdef
suite         ::=  stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
statement     ::=  stmt_list NEWLINE | compound_stmt
stmt_list     ::=  simple_stmt (";" simple_stmt)* [";"]

Note that statements always end in a NEWLINE possibly followed by a DEDENT. Also note that optional continuation clauses always begin with a keyword that cannot start a statement, thus there are no ambiguities (the ‘dangling else‘ problem is solved in Python by requiring nested if statements to be indented).

The formatting of the grammar rules in the following sections places each clause on a separate line for clarity.





























"""