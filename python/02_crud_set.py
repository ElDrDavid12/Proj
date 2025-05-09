#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:51:46 2024

@author: david
"""

set_countries = {'Ven', 'U.S', 'Arg', 'Ven'}

size = len(set_countries)
print(size)

print('Ven' in set_countries)
print('Rus' in set_countries)

# add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'rom', 'ecua', 'pe'})
print(set_countries)

# remove

set_countries.remove('Ven')
print(set_countries)

set_countries.remove('Arg')
set_countries.discard('Arg')
print(set_countries)
set_countries.add('Nazi')
print(set_countries)
set_countries.clear()
print(set_countries)
print(len(set_countries))