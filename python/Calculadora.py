#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:35:48 2024

@author: david
"""

# Funciones para las operaciones matemáticas
def add(a, b):
    return a + b  # Suma de dos números

def substract(a, b):
    return a - b  # Resta de dos números

def multiply(a, b):
    return a * b  # Multiplicación de dos números

def divide(a, b):
    return a / b  # División de dos números

# Función principal para ejecutar la calculadora
def calculator():
    while True:
        # Menú con opciones de operación
        print("Seleccione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        # Obtención de la opción seleccionada por el usuario
        option = int(input("Ingresa tu opción: "))
        
        if option == 5:
            print("Apagando sistema...")  # Mensaje cuando se apaga el sistema
            break  # Sale del bucle y termina el programa
        
        if option in [1, 2, 3, 4]:
            # Solicita los dos números para la operación
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))
            
            # Dependiendo de la opción, realiza la operación seleccionada
            if option == 1:
                print(add(num1, num2))  # Muestra el resultado de la suma
                break  # Termina el programa después de la operación
            elif option == 2:
                print(substract(num1, num2))  # Muestra el resultado de la resta
                break
            elif option == 3:
                print(multiply(num1, num2))  # Muestra el resultado de la multiplicación
                break
            elif option == 4:
                print(divide(num1, num2))  # Muestra el resultado de la división
                break
