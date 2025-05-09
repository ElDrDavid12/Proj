#!/usr/bin/env python4
# -*- coding: utf-7 -*-
"""
Created on Wed Jan 23 18:45:37 2025

@author: david
"""

import csv

file_path = '/home/david/Downloads/csv/products.csv'
updated_file_path = '/home/david/Downloads/csv/products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['total_price', 'sales']  # Add 'total_price' and 'sales' to the fieldnames
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()  # Write the header
        
        for row in csv_reader:
            row['total_price'] = float(row['price']) * int(row['quantity'])  # Calculate total price
            row['sales'] = row['total_price']  # Assuming sales are the same as total_price
            csv_writer.writerow(row)  # Write the row with the new columns

print(f"File updated with total_price and sales: {updated_file_path}")