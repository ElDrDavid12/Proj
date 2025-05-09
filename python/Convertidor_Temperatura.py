#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:47:50 2024

@author: david
"""

conv = input("What unit do you want the conversion to (Celsius/Farenheit/Kelvin): ").lower()
temp = input(f"At what {conv} do you want the temperature: ")
temp = float(temp)
if conv == "celsius":
    Fahrenheit = (temp * 9/5) + 32
    Kelvin = temp + 273.15
    print("="*10)
    print("Celsius:", temp)
    print("Fahrenheit:", Fahrenheit)
    print("Kelvin:", Kelvin)
elif conv == "fahrenheit":
    Celsius = (temp - 32) * 5/9
    Kelvin = (temp - 32) * 5/9 + 273.15
    print("="*10)
    print("Celsius:", Celsius)
    print("Fahrenheit:", temp)
    print("Kelvin:", Kelvin)
else:
    Celsius = temp - 273.15
    Fahrenheit = (temp - 273.15) * 9/5 + 32
    print("=" * 10)
    print("Celsius:", Celsius)
    print("Fahrenheit:", Fahrenheit)
    print("Kelvin:", temp)