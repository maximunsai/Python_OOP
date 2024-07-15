#Single Inheritance
class Parent:
    def fun1(self):
        print("This is Parent Class")

class Child(Parent):
    def fun2(self):
        print("This is Child Class")

obj = Child()
obj.fun1()
obj.fun2()

# Multilevel Inheritance

class GrandParent:
    def fun1(self):
        print("This is GrandParent Class")

class Parent(GrandParent):
    def fun2(self):
        print("This is Parent Class")

class Child(Parent):
    def fun3(self):
        print("This is Child Class")

obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()


# Hierarchey Inheritance
class GrandParent:
    def fun1(self):
        print("This is GrandParent Class")

class Parent(GrandParent):
    def fun2(self):
        print("This is Parent Class")

class Child(Parent):
    def fun3(self):
        print("This is Child Class")

class Child1(Parent):
    def fun4(self):
        print("This is Child1 Class")

obj = Child()   
obj.fun1()
obj.fun2()
obj.fun3()
obj = Child1()
obj.fun1()
obj.fun2()
obj.fun4()


# Multiple Inheritance
class Father:
    def func(self):
        print("This is Father Class")

class Mother:
    def func1(self):
        print("This is Mother Class")

class child(Father, Mother):
    def func(self):
        print("This is Child Class")

obj = child()
obj.func()
obj.func1()


# Super()

class Car:
    def __init__(self, Brand, Model, Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price

    def func(self):
        print(f"Brand : {self.Brand}, Model : {self.Model}, Price : {self.Price}")

class ExtendedCar(Car):
    def __init__(self, Brand, Model, Price, Year):
        super().__init__(Brand, Model, Price)
        self.Year = Year

    def ManufactureYear(self):
        print(f"ManufactureYear: Year")    

obj = ExtendedCar('Hond', 'Camry', '$2000', 2017)     
obj.func()
obj.ManufactureYear()




