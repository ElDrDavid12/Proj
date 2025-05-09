#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:08:19 2024

@author: david
"""
x = 5
if x > 5:
    print("X es mayor a 5")
elif x == 5:
    print("X es igual a 5")
else:
    print("X es menor que 5")
print("afuera")

x = 15
y = 20

if x > 10 and y > 25:
    print("X es mayor que 10 y Y es mayor que 15")
if x>10 or y>25:
    print("X es mayor que 10 o Y es Mayor que 25")
    
if not x>10:
    print("X no es mayor que 10")

is_member = True
age = 15

if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor que o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor que 15 años")
else:
    print("No eres miemrbo y NO TIENES ACCESo")