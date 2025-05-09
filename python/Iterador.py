#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:14:33 2024

@author: david
"""

# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

text = "Hola mundo"
iter_text = iter(text)
for char in iter_text:
    print(char)
    
limit = 10

odd_itter = iter(range(1, limit+1,2))
for num in odd_itter:
    print(num)