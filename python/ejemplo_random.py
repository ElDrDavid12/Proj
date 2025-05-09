import random

#generar un numero entero aleatorio
random_number = random.randint(1, 10)
print(random_number)

#eligir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lsta de cartas
cards = ['A', 'King', 'Queen', 'Jester', '10', '9', '8', '7', '6', '5', '4','3', '2', '1']
random.shuffle(cards)
print(cards)