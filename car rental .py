class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Rented"
        print(f"{self.car_id} - {self.brand} {self.model} | ₹{self.price_per_day}/day | {status}")


class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        print("\nAvailable Cars:")
        for car in self.cars:
            car.display_info()

    def rent_car(self, car_id, days):
        for car in self.cars:
            if car.car_id == car_id:
                if car.available:
                    total_cost = car.price_per_day * days
                    car.available = False
                    print(f"\nCar rented successfully!")
                    print(f"Total Cost: ₹{total_cost}")
                    return
                else:
                    print("\nCar is already rented.")
                    return

        print("\nCar not found.")

    def return_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                if not car.available:
                    car.available = True
                    print("\nCar returned successfully!")
                    return
                else:
                    print("\nThis car was not rented.")
                    return

        print("\nCar not found.")


# Create rental system
rental_system = CarRentalSystem()

# Add cars
rental_system.add_car(Car(1, "Toyota", "Innova", 5000))
rental_system.add_car(Car(2, "Hyundai", "Creta", 3000))
rental_system.add_car(Car(3, "Maruti", "Swift", 2000))

# Menu
while True:
    print("\n--- Car Rental System ---")
    print("1. Show Cars")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        rental_system.show_cars()

    elif choice == "2":
        car_id = int(input("Enter Car ID: "))
        days = int(input("Enter number of days: "))
        rental_system.rent_car(car_id, days)

    elif choice == "3":
        car_id = int(input("Enter Car ID: "))
        rental_system.return_car(car_id)

    elif choice == "4":
        print("Thank you for using Car Rental System.")
        break

    else:
        print("Invalid choice.")