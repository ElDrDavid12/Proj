import json  # Importa el módulo json para trabajar con archivos JSON

# Lectura del archivo JSON
with open('/home/david/Projects/py/products.json', mode='r') as file:
    products = json.load(file)  # Carga y convierte el contenido del archivo JSON en una lista de diccionarios

# Mostrar el contenido de cada producto
for product in products:
    # Imprime el nombre y el precio de cada producto
    print(f"Producto: {product['name']}, Precio: ${product['price']}")
