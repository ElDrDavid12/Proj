#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:19:20 2024

@author: david
"""

import matplotlib.pyplot as plt  # Importa la biblioteca para crear gráficos

# Datos
x = [0, 4, 8, 16, 32]  # Valores para el eje X
y = [0, 3, 6, 12, 24]  # Valores para el eje Y

# Crear el gráfico
plt.plot(x, y)  # Genera el gráfico de línea con los datos proporcionados
plt.title('Ejemplo de gráfico')  # Establece el título del gráfico
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y
plt.show()  # Muestra el gráfico en pantalla
