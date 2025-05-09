#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:22:40 2024

@author: david
"""
add = lambda a,b: a + b
print(add(10,4))

multiply = lambda a,b: a * b
print(add(80,5))

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
#Pares
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)