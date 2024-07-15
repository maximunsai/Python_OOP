class Car:
    def __init__(self, brand, model, price):
        self.brand = brand         # Public attribute
        self._model = model        # Protected attribute
        self.__price = price       # Private attribute

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self._model}, Price: ${self.__price}")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price!")


car = Car("Toyota", "Camry", 30000)

# Accessing public attribute
print(car.brand)  

# Accessing protected attribute (not recommended)
print(car._model) 

# Trying to access private attribute directly (will raise an AttributeError)
try:
    print(car.__price)
except AttributeError as e:
    print(e)

# Using getter and setter methods to access private attribute
print(car.get_price())  
car.set_price(35000)
print(car.get_price())  
car.set_price(-5000)  

# Displaying information using the display_info method
car.display_info()  
