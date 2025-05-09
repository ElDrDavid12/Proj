#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:35:26 2025

@author: david
"""

import csv

#Leer un archivo
'''with open('/home/david/Downloads/csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)'''
        
#Mostrar la informacion por columnas
with open('/home/david/Downloads/csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")