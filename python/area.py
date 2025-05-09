while True:
    # Solicita al usuario que elija un tipo de figura geométrica
    group = input("rectángulo, triángulo, paralelogramo o círculo: ").lower()

    # Si el usuario elige "rectángulo"
    if group == "rectángulo":
        def Rectángulo():
            base = float(input("¿Cuál es el ancho?: "))
            altura = float(input("¿Cuál es la altura?: "))
            area = base * altura
            print(f"El área del rectángulo es {area}")
        Rectángulo()
        break

    # Si el usuario elige "triángulo"
    elif group == "triángulo":
        def Triángulo():
            base = float(input("¿Cuál es la base?: "))
            altura = float(input("¿Cuál es la altura?: "))
            area = (base * altura) / 2
            print(f"El área del triángulo es {area}")
        Triángulo()
        break

    # Si el usuario elige "paralelogramo"
    elif group == "paralelogramo":
        def Paralelogramo():
            base = float(input("¿Cuál es la base?: "))
            altura = float(input("¿Cuál es la altura?: "))
            area = base * altura
            print(f"El área del paralelogramo es {area}")
        Paralelogramo()
        break

    # Si el usuario elige "círculo"
    elif group == "círculo":
        def Círculo():
            radio = float(input("¿Cuál es el radio?: "))
            area = 3.14 * (radio ** 2)
            print(f"El área del círculo es {area}")
        Círculo()
        break

    # Si el usuario ingresa una opción no válida
    else:
        print("Opción no válida, intenta de nuevo...")
