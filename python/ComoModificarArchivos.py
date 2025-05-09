#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:12:25 2025

@author: david
"""
# leer archivo
with open('/home/david/Projects/Caperucita_roja.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())
        
#leer todas las lineas en una lista
'''with open('/home/david/Projects/Caperucita_roja.txt', 'r') as file:
    lines = file.readlines()
    print(lines)'''

#añadir texto sin modificar el texto ya existente
'''with open('/home/david/Projects/Caperucita_roja.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")
    print(file)'''

#Sobreescribir el texto
'''with open('/home/david/Projects/Caperucita_roja.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")'''