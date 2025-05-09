x = int(input("What's the number you want to check if it gives the same number? "))

for i in range(-100, 100):
    for z in range(-100, 100):
        if i + z == x:
            print(f"{i} + {z} = {x}")

for a in range(-100, 100):
    for b in range(-100, 100):
        if a - b == x:
            print(f"{a} - {b} = {x}")

for c in range(-100, 100):
    for d in range(-100, 100):
        if c / d == x:
            print(f"{c} / {d} = {x}")
            
for e in range(-100, 100):
    for f in range(-100, 100):
        if e * f == x:
            print(f"{e} * {f} = {x}")