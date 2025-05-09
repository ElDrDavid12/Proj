#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:45:37 2025

@author: david
"""

import csv

file_path = '/home/david/Downloads/csv/products.csv'
updated_file_path = '/home/david/Downloads/csv/products_updated.csv'

with open('/home/david/Downloads/csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_price']
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribir los encabezados
        
        for row in csv_reader:
            row['total_price'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)