import json
import os

file_path = '/home/david/Projects/py/products.json'


new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

# Verificar si el archivo existe
if not os.path.exists(file_path):
    # Si no existe, crear el archivo con una lista vacía
    with open(file_path, mode='w') as file:
        json.dump([], file, indent=4)

# Leer los productos existentes
with open(file_path, mode='r') as file:
    products = json.load(file)

# Agregar el nuevo producto
products.append(new_product)

# Escribir los productos actualizados en el archivo
with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)
