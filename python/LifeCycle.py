import random
import time

# Speed values for animals
speed_values = {
    "Cow": 3, "Giraffe": 4, "Deer": 7, "Elephant": 4, "Horse": 8, "Kangaroo": 7,
    "Antelope": 8, "Bison": 6, "Hippopotamus": 4, "Manatee": 3, "Panda": 3, "Beaver": 4,
    "Gorilla": 5, "Guinea pig": 2, "Koala": 2, "Mouse": 5, "Rabbit": 7, "Rhino": 4,
    "Camel": 6, "Caterpillar": 0.1, "Iguana": 3, "Parrot": 6, "Sheep": 4, "Snail": 0.01,
    "Bear": 5, "Cheetah": 10, "Arctic fox": 6, "Coyote": 8, "Dog": 6, "Hyena": 7,
    "Lion": 9, "Badger": 4, "Black bear": 5, "Bobcat": 7, "Civet": 5, "Cougar": 9,
    "Giant panda": 3, "Jaguar": 8, "Mongooses": 6, "Wolf": 8, "Bald eagle": 9,
    "Binturong": 4, "Cat": 6, "Leopard": 8, "Lynx": 7, "Otters": 6, "Polar bear": 5,
    "Raccoon": 4
}

# Classes for animals and plants
class Predator:
    def __init__(self, name, speed, camouflage, energy, reproduction_threshold):
        self.name = name
        self.speed = speed
        self.camouflage = camouflage
        self.energy = energy
        self.reproduction_threshold = reproduction_threshold

    def hunt(self, prey):
        if random.random() > self.camouflage:
            print(f"{self.name} is hunting {prey.name}...")
            if self.speed > prey.speed:
                print(f"{self.name} caught {prey.name}!")
                self.energy += 5  # Predator gains energy
                return True
        return False

    def reproduce(self):
        if self.energy >= self.reproduction_threshold:
            print(f"{self.name} is reproducing!")
            self.energy -= self.reproduction_threshold
            return True
        return False


class Prey:
    def __init__(self, name, speed, camouflage, energy, reproduction_threshold):
        self.name = name
        self.speed = speed
        self.camouflage = camouflage
        self.energy = energy
        self.reproduction_threshold = reproduction_threshold

    def reproduce(self):
        if self.energy >= self.reproduction_threshold:
            print(f"{self.name} is reproducing!")
            self.energy -= self.reproduction_threshold
            return True
        return False


class Plant:
    def __init__(self, name):
        self.name = name
        self.health = 10

    def grow(self):
        self.health += 1
        print(f"{self.name} is growing! Health: {self.health}")


class Environment:
    def __init__(self, predators, prey, plants):
        self.predators = predators
        self.prey = prey
        self.plants = plants

    def simulate_day(self):
        print("\n--- A new day starts! ---")

        # Plants grow
        for plant in self.plants:
            plant.grow()

        # Predators hunt prey
        for predator in self.predators:
            for target in self.prey:
                if predator.hunt(target):
                    self.prey.remove(target)

        # Prey reproduction
        for p in self.prey:
            if p.reproduce():
                self.prey.append(Prey(p.name, p.speed, p.camouflage, 10, 15))  # Add new prey

        # Predator reproduction
        for predator in self.predators:
            if predator.reproduce():
                self.predators.append(Predator(predator.name, predator.speed, predator.camouflage, 10, 20))  # Add new predator

    def simulate(self, days):
        for day in range(days):
            print(f"\nDay {day + 1}:")
            self.simulate_day()
            time.sleep(1)  # Pause for readability in the simulation


# Create the environment with initial predators, prey, and plants
predators = [
    Predator("Lion", speed=9, camouflage=0.3, energy=15, reproduction_threshold=20),
    Predator("Cheetah", speed=10, camouflage=0.2, energy=15, reproduction_threshold=20),
    Predator("Wolf", speed=8, camouflage=0.4, energy=15, reproduction_threshold=20),
    Predator("Jaguar", speed=8, camouflage=0.5, energy=15, reproduction_threshold=20)
]

prey = [
    Prey("Rabbit", speed=speed_values["Rabbit"], camouflage=0.5, energy=10, reproduction_threshold=15),
    Prey("Mouse", speed=speed_values["Mouse"], camouflage=0.7, energy=10, reproduction_threshold=15),
    Prey("Deer", speed=speed_values["Deer"], camouflage=0.4, energy=10, reproduction_threshold=15),
    Prey("Cow", speed=speed_values["Cow"], camouflage=0.3, energy=10, reproduction_threshold=15),
    Prey("Giraffe", speed=speed_values["Giraffe"], camouflage=0.5, energy=10, reproduction_threshold=15),
    Prey("Polar bear", speed=speed_values["Polar bear"], camouflage=0.6, energy=10, reproduction_threshold=15),
    Prey("Otters", speed=speed_values["Otters"], camouflage=0.5, energy=10, reproduction_threshold=15),
    Prey("Raccoon", speed=speed_values["Raccoon"], camouflage=0.5, energy=10, reproduction_threshold=15)
]

plants = [Plant("Grass") for _ in range(5)]

# Simulate the environment for 10 days
environment = Environment(predators, prey, plants)
environment.simulate(days=10)
