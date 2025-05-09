x = 100

def local_function():
    x = 10 #Variable local
    print(f'El valor de la variable local es {x}')

def show_global():
    print(f"El valor de la variable global es {x}")

local_function()
#print(x) Genera error
show_global()