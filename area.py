while True:
    # choosing a type of shape group
    group = input("rectangular, triangle, parallelogram, or circle: ").lower()
    # rectangular equation & result of area
    if group == "rectangular":
        base = float(input("what is the width: "))
        height =float(input("what is the height: "))
        operation = base * height
        if base != height:
            shape = "rectangle"
        else:
            shape = "square"
        print(f"Area of {shape} is " + str(operation))
        break
    # trianlge equation & result of area
    elif group == "triangle":
            shape = "triangle"
            base = float(input("what is the width: "))
            height = float(input("what is the height: "))
            operation = (base * height) / 2
            print(f"Area of {shape} is " + str(operation))
            break
    # parallelogram equation and result of area
    elif group == "parallelogram":
            shape = "parallelogram"
            base = float(input("what is the width: "))
            height = float(input("what is the height: "))
            sides = input("does it have 2 triangle sides? [Y/n] ").lower()
            if sides == "y":
                operation_1 = base * height
                operation_2 = ((base * height) / 2) * 2
                operation = operation_1 + operation_2
            else: 
                operation = (base * height) + ((base * height) / 2)
            print(f"Area of {shape} is " + str(operation))
            break
    # circle equation and result of area
    elif group == "circle":
        shape = "circle"
        radius = float(input("what is the radius: "))
        operation = 3.14 * (radius**2)
        print(f"The area of {shape} is " + str(operation))
        break
    # if you mispell a word or you are an asshole
    else:
        print("try again...")
        