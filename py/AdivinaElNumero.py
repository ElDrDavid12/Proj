# importando random
import random
# hacemos el numero que se quede asi alejandolo del loop
number = random.randint(1,10)
while True:
    print("=" * 10)
    num = int(input("Adivina el numero: "))
    if num == number:
        print(f"Felicidades, haz adivinado el numero {number}: ")
        again = input("Quieres jugar de nuevo [si/no]: ").lower()
    else:
        print("Intenta otra vez...")