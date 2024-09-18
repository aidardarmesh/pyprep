"""
Factory is a creational design pattern that provides an interface
to create objects of different types without specifying instantiation of each one.
"""


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass



class Car(Vehicle):
    def create(self):
        return "Car created!"


class Bike(Vehicle):
    def create(self):
        return "Bike created!"


class Truck(Vehicle):
    def create(self):
        return "Truck created!"


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        match(vehicle_type):
            case "car":
                return Car()
            case "bike":
                return Bike()
            case "truck":
                return Truck()
            case _:
                raise ValueError(f"Unknown vehicle type: {vehicle_type}")


# Client code
if __name__ == "__main__":
    # Creating different vehicles using the factory
    vehicle_type = "car"  # Try changing this to 'bike' or 'truck'
    vehicle = VehicleFactory.get_vehicle(vehicle_type)
    print(vehicle.create())  # Output: Car created!
