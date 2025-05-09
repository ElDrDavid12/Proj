import os

#obtener el directorio actual
''''cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)'''

#listar los archivos .txt
'''py_files = [f for f in os.listdir('.')]
print(py_files)'''

#renombrar archivos'
os.rename('txt/', '.txt/')
print("Archivo renombrado")