#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:04:48 2024

@author: david
"""

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aqui i es igual a:",i+1)
for i in range(10):
    print(i)
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruta in fruits:
    print(fruta )
    if fruta == "Naranja":
        print("Naranja encontrada")

x = 0
while x<5:
    print(x)
    x += 1
    
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i == 3:
        break
    print("Aqui i es igual a:",i)