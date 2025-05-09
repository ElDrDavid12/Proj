with open('/home/david/Projects/Caperucita_roja.txt', 'r') as file:
    # Leer todo el contenido del archivo
    texto = file.read()
    
    # Dividir el contenido en párrafos
    parrafos = texto.split('\n\n')
    
    # Contar el número de párrafos
    print(f"El número de párrafos es: {len(parrafos)}")
