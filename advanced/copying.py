import copy


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __repr__(self):
        return f"Engine({self.horsepower} HP)"


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def __repr__(self):
        return f"Car(brand={self.brand}, engine={self.engine})"

# Shallow Copy Example

engine1 = Engine(150)
car1 = Car("Toyota", engine1)

# Shallow copy of car1
car2 = copy.copy(car1)

# Modify engine in car2
car2.engine.horsepower = 200

print("Original Car:", car1)
print("Shallow Copied Car:", car2)

# Deep Copy Example
engine1 = Engine(150)
car1 = Car("Toyota", engine1)

# Deep copy of car1
car2 = copy.deepcopy(car1)

# Modify engine in car2
car2.engine.horsepower = 200

print("Original Car:", car1)
print("Deep Copied Car:", car2)



