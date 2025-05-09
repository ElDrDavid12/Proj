import random
import matplotlib.pyplot as plt

class Car:
    def __init__(self, brand, model, price, car_type):
        self.brand = brand
        self.model = model
        self.price = price
        self.car_type = car_type

    def __repr__(self):
        return f"{self.brand} {self.model} ({self.car_type}) - ${self.price:,.2f}"

class Customer:
    def __init__(self, name, budget, preferred_type):
        self.name = name
        self.budget = budget
        self.preferred_type = preferred_type

    def work_and_earn(self, amount=None):
        if amount is None:
            amount = random.randint(500, 3000)
        self.budget += amount
        return amount

    def try_to_buy_car(self, cars):
        affordable_cars = [car for car in cars if car.price <= self.budget and car.car_type == self.preferred_type]
        if affordable_cars:
            return random.choice(affordable_cars)
        return None

    def change_preference(self):
        # Customer may change car preference after a few days
        car_types = ["Economy", "Sports", "Luxury"]
        current_index = car_types.index(self.preferred_type)
        self.preferred_type = car_types[(current_index + 1) % len(car_types)]
        print(f"{self.name} changed preference to {self.preferred_type}.")

class CarDealership:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.sales_history = []
        self.sales_commission = 0.1
        self.total_revenue = 0
        self.total_sales = 0
        self.balance = 100000  # Initial balance

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def simulate_day(self):
        earnings_summary = {}
        sales_today = 0  # Track sales for today
        for customer in self.customers:
            earnings = customer.work_and_earn()
            earnings_summary[customer.name] = earnings
            car = customer.try_to_buy_car(self.cars)
            if car:
                self.sales_history.append((customer.name, car.brand, car.model, car.price, "Purchase successful"))
                self.cars.remove(car)
                commission = car.price * self.sales_commission
                self.total_revenue += car.price
                self.total_sales += 1
                sales_today += car.price
            else:
                self.sales_history.append((customer.name, None, None, 0, "Could not afford a car"))
        
        return earnings_summary, sales_today

    def show_sales_summary(self):
        print("\n=== Sales Summary ===")
        print(f"Total Sales: {self.total_sales}")
        print(f"Total Revenue: ${self.total_revenue:,.2f}")
        print(f"Commission Earned: ${self.total_revenue * self.sales_commission:,.2f}")
        
        if self.total_sales:
            top_customer = max(self.customers, key=lambda c: c.budget)
            print(f"Top Customer: {top_customer.name} (Remaining Budget: ${top_customer.budget:,.2f})")
        else:
            print("No sales made yet.")
        print("-" * 40)

    def show_sales_history(self):
        print("\n=== Sales History ===")
        if not self.sales_history:
            print("No sales have been made.")
            return
        
        # Create a dictionary to group sales by customer
        sales_by_customer = {}
        
        # Group sales by customer
        for sale in self.sales_history:
            customer = sale[0]
            if customer not in sales_by_customer:
                sales_by_customer[customer] = {
                    'purchases': [],
                    'total_spent': 0
                }
            
            if sale[4] == "Purchase successful":
                sales_by_customer[customer]['purchases'].append(f"{sale[1]} {sale[2]} (${sale[3]:,.2f})")
                sales_by_customer[customer]['total_spent'] += sale[3]
            else:
                sales_by_customer[customer]['purchases'].append("Could not afford a car.")
        
        # Print the grouped sales summary
        for customer, data in sales_by_customer.items():
            print(f"{customer} made {len(data['purchases'])} purchase attempts.")
            for purchase in data['purchases']:
                print(f"  - {purchase}")
            print(f"  Total Spent: ${data['total_spent']:,.2f}")
            print("-" * 40)


    def plot_sales_graph(self, sales_per_day):
        days = list(range(1, len(sales_per_day) + 1))

        # Track customers' budgets per day
        customer_budgets_per_day = []
        for day in range(len(sales_per_day)):
            customer_budgets_per_day.append([customer.budget for customer in self.customers])

        # Track dealership balance per day
        dealership_balance_per_day = [self.balance] * len(sales_per_day)

        # Plot daily sales
        plt.subplot(3, 1, 1)
        plt.plot(days, sales_per_day, label="Daily Sales", color='b')
        plt.xlabel("Days")
        plt.ylabel("Sales ($)")
        plt.title("Sales Over Time")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()

        # Plot customers' budgets (average budget per day)
        avg_customer_budgets = [sum(budgets) / len(budgets) for budgets in customer_budgets_per_day]
        plt.subplot(3, 1, 2)
        plt.plot(days, avg_customer_budgets, label="Average Customers' Budgets", color='g')
        plt.xlabel("Days")
        plt.ylabel("Budget ($)")
        plt.title("Average Budget of Customers")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()

        # Plot dealership balance
        plt.subplot(3, 1, 3)
        plt.plot(days, dealership_balance_per_day, label="Dealership Balance", color='r')
        plt.xlabel("Days")
        plt.ylabel("Balance ($)")
        plt.title("Dealership Balance")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()

        plt.tight_layout()
        plt.show()

    def daily_report(self, day):
        total_sales = len(self.sales_history)
        total_revenue = sum(sale[3] for sale in self.sales_history)
        print(f"\n=== Day {day} Report ===")
        print(f"Sales Today: {total_sales}")
        print(f"Revenue Today: ${total_revenue:,.2f}")
        print(f"Dealership Balance: ${self.balance:,.2f}")
        print(f"Total Customers: {len(self.customers)}")
        print("-" * 40)
    
    def simulate_market_fluctuations(self):
        # Example: A random event that reduces car prices or increases customer earnings
        event = random.choice(["Price drop", "Customer bonus", "Nothing"])
        if event == "Price drop":
            discount = random.randint(5, 20)
            for car in self.cars:
                car.price -= car.price * discount / 100
            print(f"Market event: Price drop! All cars are now discounted by {discount}%.")
        elif event == "Customer bonus":
            bonus = random.randint(1000, 5000)
            customer = random.choice(self.customers)
            customer.work_and_earn(bonus)
            print(f"Market event: {customer.name} received a bonus of ${bonus}.")
        else:
            print("Market event: No changes.")
        print("-" * 40)

# Example usage
if __name__ == "__main__":
    dealership = CarDealership()

    # Add cars
    dealership.add_car(Car("Toyota", "Corolla", 20000, "Economy"))
    dealership.add_car(Car("Honda", "Civic", 22000, "Economy"))
    dealership.add_car(Car("Ford", "Mustang", 35000, "Sports"))
    dealership.add_car(Car("Tesla", "Model 3", 50000, "Luxury"))

    # Add customers
    dealership.add_customer(Customer("Alice", 15000, "Economy"))
    dealership.add_customer(Customer("Bob", 18000, "Economy"))
    dealership.add_customer(Customer("Charlie", 30000, "Luxury"))

    # Simulate multiple days
    sales_per_day = []  # List to track sales each day
    for day in range(10):  # Run for 10 days
        print(f"\n=== Day {day + 1} ===")
        dealership.simulate_market_fluctuations()
        earnings, sales_today = dealership.simulate_day()
        sales_per_day.append(sales_today)

        for name, earnings_amount in earnings.items():
            print(f"{name} worked and earned ${earnings_amount:,.2f}.")
        
        dealership.show_sales_history()

        # Daily report
        dealership.daily_report(day + 1)

    dealership.show_sales_summary()
    dealership.plot_sales_graph(sales_per_day)
