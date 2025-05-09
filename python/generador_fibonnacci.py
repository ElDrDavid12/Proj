#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:41:11 2024

@author: david
"""

def fibonnacci(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b
        
for num in fibonnacci(10):
    print(num)