#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:46:37 2024

@author: david
"""
#Ejercicio 1
num = [1,2,3,4,5]
num_2 = [x*2 for x in num]
print(num_2)
#Ejercicio 2
words = ["sol","mar","montaña","rio","estrella"]
words_2 = [palabra for palabra in words if len(palabra) > 3]
print(words_2)
#Ejercicio 3
claves = ["nombre","edad","ocupacion"]
valores = ["Juan", 30, "Ingeniero"]
diccionario = {claves[i]:valores[i] for i in range(len(claves))}
print(diccionario)
#Ejercicio 4
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix_2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix_2)
#Ejercicio 5
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print(nombres_madrid)
#Ejercicio 6
num = [1,2,3,4,5,6,7,8,9,10]
even = [x*2 if x % 2 == 0 else x for x in num]
print(even)