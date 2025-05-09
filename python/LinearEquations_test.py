#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:25:28 2024

@author: david
"""


import matplotlib.pyplot as plt

# Datos
x = []
y = []

function = lambda x: (9/-10) * x - 3
for i in range(1, 10):
    x.append(function(i))
    y.append(function(i))
# Crear el plot
plt.plot(x, y)
plt.title('Gráfico de ejemplo "Linear Equations"')
plt.xlabel('X')
plt.ylabel('Y')
plt.show(x, y)