import csv  # Importa el módulo csv para trabajar con archivos CSV
import json  # Importa el módulo json para trabajar con archivos JSON

# Ruta del archivo CSV y el archivo JSON de salida
csv_file_path = '/home/david/Downloads/csv/products.csv'
json_file_path = '/home/david/Projects/py/productos.json'

# Leer archivo CSV
products = []
try:
    with open(csv_file_path, mode='r') as file1:
        csv_reader = csv.DictReader(file1)  # Lee el archivo CSV como diccionarios
        for row in csv_reader:
            products.append(row)  # Añade cada fila al listado de productos
    print(f"Se leyeron {len(products)} productos desde {csv_file_path}")
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")

# Escribir los productos en un archivo JSON
if products:
    try:
        with open(json_file_path, mode='w') as file2:
            json.dump(products, file2, indent=4)  # Convierte la lista de diccionarios a JSON
        print(f"Productos escritos en {json_file_path}")
    except Exception as e:
        print(f"Error al escribir en el archivo JSON: {e}")
else:
    print("No hay productos para escribir JSON.")
