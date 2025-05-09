#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:21:13 2025

@author: david
"""

class Vehículo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        """Vende el vehículo si está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} ha sido vendido.")
        else:
            print(f"El vehículo {self.marca} no está disponible.")

    def estado(self):
        """Retorna el estado de disponibilidad del vehículo."""
        return self.disponible

    def get_price(self):
        """Retorna el precio del vehículo."""
        return self.precio


class Auto(Vehículo):
    def start(self):
        """Enciende el motor del coche si está disponible."""
        if self.disponible:
            return f"El motor del coche {self.marca} está en marcha."
        else:
            return f"El coche {self.marca} no está disponible."

    def stop(self):
        """Detiene el motor del coche si está disponible."""
        if self.disponible:
            return f"El motor del coche {self.marca} se ha detenido."
        else:
            return f"El coche {self.marca} no está disponible."


class Bicicleta(Vehículo):
    def montar(self):
        """Prepara la bicicleta para ser montada si está disponible."""
        if self.disponible:
            return f"La bicicleta {self.marca} está lista para montar."
        else:
            return f"La bicicleta {self.marca} no está disponible."


class Camión(Vehículo):
    def cargar(self):
        """Prepara el camión para cargar mercancía si está disponible."""
        if self.disponible:
            return f"El camión {self.marca} está cargando mercancía."
        else:
            return f"El camión {self.marca} no está disponible."


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.autos = []

    def comprar_auto(self, auto):
        """Permite que el cliente compre un auto si está disponible."""
        if auto.estado():
            self.autos.append(auto)
            auto.vender()
        else:
            print(f"El auto {auto.marca} no está disponible.")


class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def añadir_auto(self, auto):
        """Añade un auto al inventario de la concesionaria."""
        self.inventario.append(auto)

    def registrar_cliente(self, cliente):
        """Registra un cliente en la concesionaria."""
        self.clientes.append(cliente)

    def mostrar_disponibles(self):
        """Muestra los autos disponibles para la venta en el inventario."""
        for auto in self.inventario:
            if auto.estado():
                print(f"{auto.marca} {auto.modelo} está disponible por {auto.get_price()}.")
            else:
                print(f"{auto.marca} {auto.modelo} ya no está disponible.")


# Crear instancias de vehículos
auto1 = Auto("Toyota", "Corolla", 20000)
bicicleta1 = Bicicleta("Trek", "Mountain", 500)
camion1 = Camión("Volvo", "FH", 80000)

# Crear instancia de cliente
cliente1 = Cliente("Juan")

# Crear concesionaria e inventario
concesionaria = Concesionaria()
concesionaria.añadir_auto(auto1)
concesionaria.añadir_auto(bicicleta1)
concesionaria.añadir_auto(camion1)

# Mostrar autos disponibles en la concesionaria
print("Autos disponibles en la concesionaria:")
concesionaria.mostrar_disponibles()

# El cliente compra un auto
cliente1.comprar_auto(auto1)

# Mostrar autos disponibles después de la compra
print("\nAutos disponibles después de la compra de Juan:")
concesionaria.mostrar_disponibles()

# Cliente intenta comprar un auto ya vendido
cliente1.comprar_auto(auto1)  # Intento de compra de auto ya vendido

# Mostrar el estado de los vehículos
print("\nEstado de los vehículos:")
print(auto1.start())  # Intento de arrancar un auto ya vendido
print(bicicleta1.montar())  # Intento de montar una bicicleta disponible
print(camion1.cargar())  # Intento de cargar un camión disponible
