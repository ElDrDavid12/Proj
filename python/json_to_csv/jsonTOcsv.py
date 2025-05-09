import json  # Importa el módulo json para trabajar con archivos JSON
import csv  # Importa el módulo csv para trabajar con archivos CSV
import os  # Importa os para verificar si el archivo CSV ya existe

# Ruta de los archivos
json_file_path = '/home/david/Projects/py/products.json'
csv_file_path = '/home/david/Downloads/csv/productos.csv'

# Lectura del archivo JSON
try:
    with open(json_file_path, mode='r') as file2:
        products = json.load(file2)  # Carga y convierte el contenido del archivo JSON en una lista de diccionarios
    print(f"Se cargaron {len(products)} productos desde {json_file_path}")
except Exception as e:
    print(f"Error al leer el archivo JSON: {e}")
    products = []

# Escribir los productos en un archivo CSV
if products:
    file_exists = os.path.exists(csv_file_path)
    
    try:
        with open(csv_file_path, mode='a', newline='') as file1:
            csv_writer = csv.DictWriter(file1, fieldnames=products[0].keys())

            # Escribe los encabezados solo si el archivo no existe o está vacío
            if not file_exists or os.stat(csv_file_path).st_size == 0:
                print("Escribiendo encabezados en el CSV...")
                csv_writer.writeheader()
            
            # Escribe cada producto en el archivo CSV
            for product in products:
                csv_writer.writerow(product)
                print(f"Escribiendo producto: {product['name']}")

        print(f"Productos escritos en {csv_file_path}")
    except Exception as e:
        print(f"Error al escribir en el archivo CSV: {e}")
else:
    print("No hay productos para escribir en el CSV.")
