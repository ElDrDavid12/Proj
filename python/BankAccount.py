#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:59:18 2024

@author: david
"""

# Definición de la clase BankAccount
class BankAccount:
    def __init__(self, account_holder, balance):
        # Inicializa el titular de la cuenta y el saldo
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True  # La cuenta comienza activa
    
    def deposit(self, amount):
        # Método para depositar dinero
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar: Cuenta inactiva")
            
    def withdraw(self, amount):
        # Método para retirar dinero
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual: {self.balance}")
            else:
                print("Fondos insuficientes")
        else:
            print("No se puede retirar: Cuenta inactiva")
                
    def deactivate_account(self):
        # Método para desactivar la cuenta
        self.is_active = False
        print("La cuenta ha sido desactivada")
        
    def activate_account(self):
        # Método para activar la cuenta
        self.is_active = True
        print("La cuenta ha sido activada")

# Creación de una instancia de BankAccount
account = BankAccount("Augusto", 1_000_000)

# Bucle para interactuar con el usuario
while True:
    print("Métodos: [Depositar/Retiro/Activar cuenta/Desactivar cuenta]")
    choice = input("").lower()
    if choice in ['depositar', 'retiro', 'activar cuenta', 'desactivar cuenta']:
        if choice == 'depositar':
            depositar = float(input("¿Cuánto quieres depositar?: "))
            account.deposit(depositar)
        elif choice == 'retiro':
            withdrawal = float(input("¿Cuánto quieres retirar?: "))
            account.withdraw(withdrawal)
        elif choice == 'desactivar cuenta':
            account.deactivate_account()
        elif choice == 'activar cuenta':
            account.activate_account()
    else:
        print("Esa opción no existe, intenta otra vez...")
    
    # Pregunta si el usuario desea realizar otra operación
    abc = input("¿Quieres hacer otro método [yes/no]?: ").lower()
    if abc == "no":
        break
