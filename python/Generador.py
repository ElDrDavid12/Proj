#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:33:56 2024

@author: david
"""
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)