import random
import matplotlib.pyplot as plt

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.previous_choices = set()  # To track past purchases and skips

    def work_and_earn(self, amount):
        self.budget += amount
        print(f"{self.name} worked and earned ${amount}. New budget: ${self.budget}")

    def buy_car(self, car):
        if self.budget >= car.price:
            self.budget -= car.price
            print(f"{self.name} bought a {car.brand} {car.model} for ${car.price}. Remaining budget: ${self.budget}")
            self.previous_choices.add((car.brand, car.model))
            return True
        else:
            print(f"{self.name} cannot afford the {car.brand} {car.model}. Budget: ${self.budget}, Price: ${car.price}")
            return False

    def choose_car(self, cars):
        affordable_cars = [car for car in cars if car.price <= self.budget and (car.brand, car.model) not in self.previous_choices]
        
        if not affordable_cars:
            print(f"{self.name} cannot afford any available car and has already skipped or purchased all possible options.")
            return None

        # Choose the most expensive car that can be afforded, encouraging customers to buy better cars if they have the budget
        chosen_car = max(affordable_cars, key=lambda car: car.price)
        print(f"{self.name} decided to buy {chosen_car}")
        return chosen_car

class CarDealership:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.sales_history = []
        self.sales_commission = 0.1

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added {car} to inventory.")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Registered customer: {customer.name} with a budget of ${customer.budget}.")

    def simulate_work(self):
        for customer in self.customers:
            earnings = random.randint(1000, 10000)
            customer.work_and_earn(earnings)

    def sell_cars(self):
        for customer in self.customers:
            print(f"\n{customer.name}'s available cars:")
            if not self.cars:
                print("No cars available for sale.")
                break

            # Show all available cars without filtering by brand
            for idx, car in enumerate(self.cars, 1):
                print(f"{idx}. {car}")

            print(f"0. Skip buying a car")
            
            # Simulate customer behavior
            chosen_car = customer.choose_car(self.cars)

            if not chosen_car:
                print(f"{customer.name} skipped buying a car.")
                self.sales_history.append((customer.name, None, None, 0, "Skipped purchasing"))
                continue

            # Proceed with buying the chosen car
            if customer.buy_car(chosen_car):
                self.sales_history.append((customer.name, chosen_car.brand, chosen_car.model, chosen_car.price, "Purchase successful"))
                self.cars.remove(chosen_car)
                commission = chosen_car.price * self.sales_commission
                print(f"Dealership earned a commission of ${commission:.2f}.")
            else:
                self.sales_history.append((customer.name, chosen_car.brand, chosen_car.model, chosen_car.price, "Insufficient budget"))

    def show_sales_summary(self):
        total_sales = len(self.sales_history)
        total_revenue = sum(sale[3] for sale in self.sales_history)
        total_commission = total_revenue * self.sales_commission

        print("\n=== Sales Summary ===")
        print(f"Total sales: {total_sales}")
        print(f"Total revenue: ${total_revenue}")
        print(f"Total commission earned by dealership: ${total_commission:.2f}")

        if self.sales_history:
            top_customer = max(self.customers, key=lambda c: c.budget)
            print(f"Top customer: {top_customer.name} with ${top_customer.budget} remaining budget.")
        else:
            print("No sales yet.")

    def show_sales_history(self):
        print("\n=== Sales History ===")
        if self.sales_history:
            for sale in self.sales_history:
                if sale[4] == "Purchase successful":
                    print(f"{sale[0]} bought {sale[1]} {sale[2]} for ${sale[3]}.")
                else:
                    print(f"{sale[0]} could not buy {sale[1]} {sale[2]} for ${sale[3]}. Reason: {sale[4]}")
        else:
            print("No sales have been made.")

    def plot_sales_graph(self):
        successful_sales = [sale for sale in self.sales_history if sale[4] == "Purchase successful"]
        failed_sales = [sale for sale in self.sales_history if sale[4] != "Purchase successful"]

        successful_count = len(successful_sales)
        failed_count = len(failed_sales)

        # Plotting the sales data
        labels = ['Successful Sales', 'Failed Sales']
        sizes = [successful_count, failed_count]
        colors = ['#4CAF50', '#FF5733']

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title("Sales Performance Overview")
        plt.axis('equal')
        plt.show()

# Example usage
if __name__ == "__main__":
    dealership = CarDealership()

    # Add cars
    dealership.add_car(Car("Toyota", "Corolla", 20000))
    dealership.add_car(Car("Honda", "Civic", 22000))
    dealership.add_car(Car("Ford", "Mustang", 35000))
    dealership.add_car(Car("Tesla", "Model 3", 50000))
    dealership.add_car(Car("BMW", "X5", 60000))
    dealership.add_car(Car("Audi", "A4", 45000))
    dealership.add_car(Car("Mercedes", "C-Class", 55000))
    dealership.add_car(Car("Chevrolet", "Impala", 25000))
    dealership.add_car(Car("Nissan", "Altima", 23000))
    dealership.add_car(Car("Hyundai", "Elantra", 18000))

    # Add customers
    dealership.add_customer(Customer("Alice", 15000))
    dealership.add_customer(Customer("Bob", 18000))
    dealership.add_customer(Customer("Charlie", 30000))
    dealership.add_customer(Customer("David", 10000))
    dealership.add_customer(Customer("Eve", 25000))
    dealership.add_customer(Customer("Frank", 40000))
    dealership.add_customer(Customer("Grace", 12000))
    dealership.add_customer(Customer("Hannah", 35000))
    dealership.add_customer(Customer("Ivy", 50000))
    dealership.add_customer(Customer("Jack", 20000))

    while True:
        print("\n=== Car Dealership Simulation ===")
        print("1. Simulate customers working and earning money")
        print("2. Attempt to sell cars")
        print("3. Show sales history")
        print("4. Show sales summary")
        print("5. Show sales performance graph")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            dealership.simulate_work()
        elif choice == "2":
            dealership.sell_cars()
        elif choice == "3":
            dealership.show_sales_history()
        elif choice == "4":
            dealership.show_sales_summary()
        elif choice == "5":
            dealership.plot_sales_graph()
        elif choice == "6":
            print("Exiting the simulation.")
            break
        else:
            print("Invalid choice. Please try again.")
