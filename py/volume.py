while True:
    group = input("Cuboid, pyramid, parallelepiped, or sphere: ").lower()
    if group == "Cuboid":
        base = float(input("what is the width: "))
        height = float(input("what is the height: "))
        length = float(input("what is the length: "))
        operation = base * height * length
        if base != height:
            shape = ""
        else:
            shape = "square"
        print(f"Volume of {shape} is " + str(operation) + " cubic cm")
        break
    elif group == "pyramid":
            shape = "pyramid"
            base = float(input("what is the width: "))
            height = float(input("what is the height: "))
            Area = base * base
            operation = (1/3) * Area * height
            print(f"Volume of {shape} is " + str(operation))
            break
    elif group == "parallelepiped":
            shape = "parallelepiped"
            base = float(input("what is the width: "))
            height = float(input("what is the height: "))
            sides = input("does it have 2 sides? [Y/n] ").lower()
            if sides == "y":
                operation_1 = base * height * length
                operation_2 = ((base * height * length) / 2) * 2
                operation = operation_1 + operation_2
            else: 
                operation = (base * height * length) + ((base * height * length) / 2)
            print(f"Volume of {shape} is " + str(operation))
            break
    elif group == "sphere":
        shape = "sphere"
        radius = float(input("what is the radius: "))
        operation = (4/3) * 3.14 * (radius**3)
        print(f"Volume of {shape} is " + str(operation))
        break
    else:
        print("try again...")
        