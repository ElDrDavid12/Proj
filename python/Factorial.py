#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:18:14 2024

@author: david
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial_5 = factorial(30)
print(factorial_5)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = 4
print(fibonacci(number))