class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

# Creating objects of the Car class
car1 = Car("Toyota", "Camry", 30000)
car2 = Car("Honda", "Civic", 25000)

# Displaying information about the cars
car1.display_info()
car2.display_info()