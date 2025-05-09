import random  # Importa el módulo random para generar números aleatorios

number = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10

while True:  # Inicia un bucle infinito
    print("=" * 10)  # Imprime una línea de separación
    num = int(input("Adivina el número: "))  # Solicita al usuario que adivine el número y lo convierte a entero
    if num == number:  # Verifica si el número ingresado es igual al generado
        print(f"Felicidades, has adivinado el número {number}.")  # Felicita al usuario por adivinar correctamente
        again = input("¿Quieres jugar de nuevo [si/no]? ").lower()  # Pregunta si desea jugar nuevamente
        if again != 'si':  # Si la respuesta no es 'si'
            break  # Sale del bucle y termina el juego
        else:
            number = random.randint(1, 10)  # Genera un nuevo número aleatorio para el siguiente juego
    else:
        print("Intenta otra vez...")  # Indica que la suposición fue incorrecta
